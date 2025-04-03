from typing import Dict, Any, List
from pydantic import BaseModel

class AnalysisState(BaseModel):
    data: Dict[str, Any] = {}
    narrativa: str = ""
    tema: str = "dummy"
    errors: List[str] = []
