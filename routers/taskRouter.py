from datetime import datetime
from fastapi import APIRouter,status,Depends
from fastapi.security import HTTPAuthorizationCredentials
from schema import taskSchema
from security import securityConfig
from sqlalchemy.orm import Session
from repository import database
from service import taskService
task_router = APIRouter()

@task_router.post('/projects/{project_id}/tasks')
def create_task(project_id, data: taskSchema.TaskSchema, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return taskService.create_task(data,id,db)
    
@task_router.get('/projects/{project_id}/tasks')
def get_all_task(project_id,db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return taskService.get_tasks(project_id,db)

@task_router.patch('/task/{task_id}')
def update_task(duedate: datetime, task_id, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    data = {
        "duedate": duedate
    }
    return taskService.update_task(data,task_id,db)

@task_router.post('/task/{task_id}/complete')
def complete_task(task_id, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return taskService.complete_task(task_id,db)
