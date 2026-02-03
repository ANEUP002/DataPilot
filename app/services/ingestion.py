"""
Ingestion service: CSV/Excel -> DuckDB with clean SQL-safe columns
"""

import uuid
import re
from pathlib import Path
import pandas as pd

from app.core.database import get_connection


# ======================================
# Clean column names (VERY IMPORTANT)
# ======================================
def _clean_col(name: str) -> str:
    """
    Convert messy column names into SQL-safe snake_case

    Examples:
      "South Korea" -> "south_korea"
      "Gas Price ($)" -> "gas_price"
      "2023 Sales" -> "c_2023_sales"
    """
    name = str(name).strip().lower()
    name = re.sub(r"\s+", "_", name)          # spaces -> _
    name = re.sub(r"[^a-z0-9_]", "", name)    # remove punctuation
    name = re.sub(r"_+", "_", name)           # collapse __
    name = name.strip("_")

    if not name:
        name = "col"

    if name[0].isdigit():
        name = f"c_{name}"

    return name


# ======================================
# Main ingestion function
# ======================================
def ingest_file(file_path: Path, table_name: str | None = None) -> dict:
    """
    Load CSV or Excel into DuckDB with cleaned columns
    """

    if table_name is None:
        table_name = f"dataset_{uuid.uuid4().hex[:8]}"

    ext = file_path.suffix.lower()
    if ext not in [".csv", ".xlsx", ".xls"]:
        raise ValueError("Only CSV or Excel supported")

    # -----------------------
    # Load file into pandas
    # -----------------------
    if ext == ".csv":
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    # -----------------------
    # Clean column names
    # -----------------------
    original_cols = list(df.columns)
    cleaned_cols = [_clean_col(c) for c in original_cols]

    # ensure uniqueness
    seen = {}
    final_cols = []
    for c in cleaned_cols:
        if c not in seen:
            seen[c] = 0
            final_cols.append(c)
        else:
            seen[c] += 1
            final_cols.append(f"{c}_{seen[c]}")

    df.columns = final_cols

    column_mapping = [
        {"original": o, "clean": c}
        for o, c in zip(original_cols, final_cols)
    ]

    # -----------------------
    # Write into DuckDB
    # -----------------------
    conn = get_connection()

    try:
        conn.register("tmp_df", df)

        conn.execute(f"""
            CREATE OR REPLACE TABLE {table_name}
            AS SELECT * FROM tmp_df
        """)

        schema_rows = conn.execute(f"DESCRIBE {table_name}").fetchall()
        row_count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]

    finally:
        conn.close()

    schema = [{"column": r[0], "type": r[1]} for r in schema_rows]

    return {
        "dataset_id": table_name,
        "table_name": table_name,
        "schema": schema,
        "row_count": row_count,
        "column_mapping": column_mapping,
        "message": "Upload successful",
    }
