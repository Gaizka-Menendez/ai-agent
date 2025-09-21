import os
from pydantic import BaseModel, Field


class EmailMessageSchema(BaseModel):
    subjects: str
    contents: str
    invalid_request: bool | None = Field(default=False)