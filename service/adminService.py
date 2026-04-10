from fastapi import status, HTTPException
from service import projectService, userService

def admin_dashboard_data(db):
    user_count = len(userService.fetch_all_user(db))
    project_count = len(projectService.get_projects(db))
    revenue = 0
    
    return {
        "users": user_count,
        "projects": project_count,
        "revenue": revenue
    }
    
def admin_users(db):
    return userService.fetch_all_user(db)
    
def admin_projects(db):
    return projectService.get_projects(db)

def payment_history(db):
    pass

def filter_project_by_status(status, db):
    return projectService.filter_project_by_status(status,db)


