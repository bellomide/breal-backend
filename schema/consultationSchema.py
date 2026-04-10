from pydantic import BaseModel
from enum import Enum
class ConsultationStatus(str,Enum):
    pending = "PENDING"
    approved = "APPROVED"

class ConsultationSchema(BaseModel):
    type: str
    scheduled_at: str
    project_stage: str
    site_location: str
    budget_range: str
    key_concerns: str
class UpdateConsultation(BaseModel):
    status: ConsultationStatus
    admin_note: str