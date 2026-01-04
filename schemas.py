from typing import List, Optional
from pydantic import BaseModel

class CompanyProfile(BaseModel):
    website: str
    company_name: Optional[str] = None
    what_they_do: Optional[str] = None
    offerings: List[str] = []
    proof_signals: List[str] = []
    contact_page: Optional[str] = None
    careers_page: Optional[str] = None
