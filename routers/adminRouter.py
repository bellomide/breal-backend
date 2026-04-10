from fastapi import status, HTTPException, Depends, APIRouter
from service import adminService, userService
from security import securityConfig
from schema import userSchema
from sqlalchemy.orm import Session
from repository import database
from fastapi.security import HTTPAuthorizationCredentials


admin_router = APIRouter()

def is_admin(email,db):
    user_data = userService.get_user(email, userSchema.UserRole.admin,db)
    return user_data

@admin_router.get('/admin/dashboard')
def fetch_admin_data(db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    if is_admin(email,db) is not None:
        return adminService.admin_dashboard_data(db)
    

@admin_router.get('/admin/users')
def fetch_all_users(db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    if is_admin(email,db) is not None:
        return adminService.admin_users(db)
    
@admin_router.get('/admin/projects')
def fetch_all_projects(db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    if is_admin(email,db) is not None:
        return adminService.admin_projects(db)
    
@admin_router.get('/search/projects')
def filter_project_by_status(status: str, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return adminService.filter_project_by_status(status,db)
    