from pydantic import BaseModel

class MilestoneSchema(BaseModel):
    name: str
    order: int
    project_id: int
    status: str