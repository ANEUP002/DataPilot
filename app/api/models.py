from datetime import datetime
from typing import Optional, List, Dict, Any
from sqlmodel import Field, SQLModel

# Helper model for schema columns
class ColumnSchema(SQLModel):
    column: str
    type: str

class Dataset(SQLModel, table=True):
    id: str = Field(primary_key=True)
    filename: str
    table_name_duckdb: str
    schema_info: str  # Storing JSON schema as string for simplicity
    row_count: int
    created_at: datetime = Field(default_factory=datetime.utcnow)

class QueryHistory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    dataset_id: str = Field(foreign_key="dataset.id")
    question: str
    sql_query: str
    answer: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Pydantic models for API responses (inheriting from SQLModel where possible or separate)
class UploadResponse(SQLModel):
    dataset_id: str
    table_name: str
    schema: Any # Changed from schema_info to schema to match existing code
    row_count: int
    message: str

class AskRequest(SQLModel):
    dataset_id: str
    question: str

class AskResponse(SQLModel):
    answer: str
    sql_query: str
    data: List[Dict[str, Any]]
    message: str
