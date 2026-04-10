from enum import Enum
from pydantic import BaseModel


class ContractorStatus(str, Enum):
    approved = "APPROVED"
    failed = "FAILED"
    
class ContractorSchema(BaseModel):
    first_name: str
    last_name: str
    nin: str
    email: str
    approval_status: ContractorStatus
    
class ContractorProfileSchema(BaseModel):
    company_name: str
    rating: float
    approval_status: str
    
class UpdateContractorProfile(BaseModel):
    company_name: str
    years_experience: int
    
