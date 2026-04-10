from fastapi import APIRouter,status, Depends
from sqlalchemy.orm import Session
from repository import database
from service import projectService
from schema import projectSchema
from fastapi.security import HTTPAuthorizationCredentials
from security import securityConfig
project_router = APIRouter()


@project_router.get('/client/projects')
def get_client_projects(db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return projectService.get_projects(db)

@project_router.get('client/projects/{project_id}')
def get_client_project_by_id(project_id, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return projectService.get_project_by_id(project_id,db)

@project_router.get('/client/dashboard', status_code=status.HTTP_200_OK)
def get_dashboard_info(db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return projectService.fetch_dashboard_project_info(db)

@project_router.post('/projects')
def create_project(data: projectSchema.ProjectSchema, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return projectService.create_project(data,db)

@project_router.patch('/projects/{project_id}')
def update_project(project_id, status: projectSchema.ProjectStatus, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    data = {
        "status": status
    }
    return projectService.update_project(project_id,data,db)
