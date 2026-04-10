from repository import database
from sqlalchemy import Column, Integer, String

class MilestoneModel(database.Base):
    
    __tablename__ = "milestone"
    
    id: int = Column(Integer, index=True, primary_key=True,autoincrement=True)
    name: str = Column(String,index=True,nullable=False)
    order: int = Column(Integer, index=True)
    project_id: int = Column(Integer,index=True)
    status: str = Column(String, index=True, nullable=False)
    
    class Config:
        orm_mode: True
    