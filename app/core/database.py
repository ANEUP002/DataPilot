from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path
import duckdb

# ========================================
# SQLite (for metadata persistence)
# ========================================
DB_PATH = Path(__file__).parent.parent.parent / "datapilot.db"
sqlite_url = f"sqlite:///{DB_PATH}"

# Create engine
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    """Create the database and tables."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency to provide a database session."""
    with Session(engine) as session:
        yield session

# ========================================
# DuckDB (for CSV data / OLAP queries)
# ========================================
DUCKDB_PATH = Path(__file__).parent.parent.parent / "data" / "datapilot.duckdb"
DUCKDB_PATH.parent.mkdir(parents=True, exist_ok=True)

def get_connection():
    """Get a DuckDB connection for OLAP queries."""
    return duckdb.connect(str(DUCKDB_PATH))

def execute_query(sql: str) -> list[dict]:
    """Execute a SQL query and return results as list of dicts."""
    conn = get_connection()
    try:
        result = conn.execute(sql).fetchdf()
        return result.to_dict(orient='records')
    finally:
        conn.close()
