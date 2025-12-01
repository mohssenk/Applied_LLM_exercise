from pydantic import BaseModel
from typing import Optional

class LLMOutput(BaseModel):
    is_match_correct: bool
    corrected_query: str = ""
