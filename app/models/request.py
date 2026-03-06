from typing import List
from pydantic import BaseModel


class IngestRequest(BaseModel):
    sentences: List[str]
