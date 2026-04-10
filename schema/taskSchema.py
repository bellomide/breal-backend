from datetime import datetime
from pydantic import BaseModel
from enum import Enum
class TaskStatus(str,Enum):
    pending = "PENDING"
    completed = "COMPLETED"

class TaskSchema(BaseModel):
    title: str
    duedate: datetime
    status: str