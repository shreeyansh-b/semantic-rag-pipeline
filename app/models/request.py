from typing import List
from pydantic import BaseModel


class IngestRequest(BaseModel):
    file_content: str


class QueryRequest(BaseModel):
    query_txt: str
