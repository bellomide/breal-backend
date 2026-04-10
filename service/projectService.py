from typing import List
from fastapi import HTTPException, status
from model import projectModel
from service import userService, contractorService
from repository import database
from schema import projectSchema

projectModel.database.Base.metadata.create_all(database.engine)

def create_project(data,db):
    if data:
        client_data = userService.get_user(data.client_email,"CLIENT",db)
        contractor_data = contractorService.fetchContractor(data.contractor_email,db)
        project = projectModel.ProjectModel(name=data.name, client_id=client_data.id, contractor_id=contractor_data.id,location=data.location, status=data.status, start_date = data.start_date, created_at = data.created_at)
        db.add(project)
        db.commit()
        db.refresh(project)
        
        print("project created by admin")
        return {
            "project_id": project.id,
            "status": "CREATED"
        }
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Invalid details')
        
def fetch_dashboard_project_info(data,db):
    projects = db.query(projectModel.ProjectModel).all()
    total_projects = len(projects)
    active_count = 0
    for project in projects:
       if project.status == projectSchema.ProjectStatus.in_progress:
            active_count+=1
    return {
        "status":"success",
        "data": {
            "total_projects": total_projects,
            "active_projects": active_count,
            "pending_payments": "not yet set"
        }
    }

def get_projects(db):
    project_list = db.query(projectModel.ProjectModel).all()
    list_response = List[projectSchema.ProjectData]
    for project in project_list:
        project_data = projectSchema.ProjectData(project_id=project.id,  project_name=project.name, status = project.status, progress=65)
        list_response.append(project_data)
    return projectSchema.ProjectList(status="success",data=list_response)

def get_project_by_id(id,db):
    project_data = db.query(projectModel.ProjectModel).filter(projectModel.ProjectModel.id == id).first()
    contractor_data = contractorService.fetchContractorByID(project_data.contractor_id,db)
    if project_data:
        return {
            "status": "success",
            "data": {
                "project_name":project_data.name,
                "location": project_data.location,
                "contractor": {
                    "name": contractor_data.name,
                    "kyc_status": contractor_data.kyc_status
                }
            }
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid project id')
    
def update_project(id, data,db):
    project_data = db.query(projectModel.ProjectModel).filter(projectModel.ProjectModel.id == id).first()
    if project_data:
        project_data.status = data.status
        db.commit()
        db.refresh(project_data)
        return {
            "message": "Project Updated"
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Project not found')
    
    
def unassign_contractor(id,db):
    project_data = db.query(projectModel.ProjectModel).filter(projectModel.ProjectModel.contractor_id == id).first()
    if project_data:
        project_data.contractor_id = -1
        db.commit()
        db.refresh(project_data)
        return {
            "messsage":"Contractor unassigned"
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Contractor not found')
    
    
def filter_project_by_status(status,db):
    project_list = db.query(projectModel.ProjectModel).filter(projectModel.ProjectModel.status == status).all()
    return project_list
