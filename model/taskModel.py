from repository import database
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class TaskModel(database.Base):
    
    __tablename__ = "task"
    
    id: int = Column(Integer, primary_key=True,index=True, autoincrement=True)
    project_id: int = Column(Integer,index=True)
    title: str = Column(String, index=True, nullable=False)
    duedate: datetime = Column(DateTime, index=True)
    status: str = Column(String, index=True, nullable=False)
    
    class Config:
        orm_mode: True