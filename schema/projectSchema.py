from typing import List
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class ProjectStatus(str,Enum):
    planning = "PLANNING"
    in_progress = "IN_PROGRESS"
    paused = "PAUSED"
    completed = "COMPLETED"


class ProjectSchema(BaseModel):
    name: str
    client_id: int
    contractor_email: str
    location: str
    status: ProjectStatus
    start_date: datetime
    created_at: datetime = datetime.utcnow()
    client_email: str
    
class ProjectResponse(BaseModel):
    client_id: int
    name: str
    location: str
    contractor_id: int
    budget: str
    
class ProjectDashboard(BaseModel):
    total_projects: int
    active_projects: int
    pending_payments: int
    
class ProjectData(BaseModel):
    project_id: int
    project_name: str
    project_status: str
    progress: int
    
class ProjectList(BaseModel):
    status: str
    data: List[ProjectData]