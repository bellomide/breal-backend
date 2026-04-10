from fastapi import HTTPException, status
from service import projectService
from model import milestoneModel
from repository import database

milestoneModel.database.Base.metadata.create_all(database.engine)


def create_milestone(data,db,project_id):
    project_data = projectService.get_project_by_id(project_id,db)
    if project_data:
        milestone_data = milestoneModel.MilestoneModel(name=data.name, order=data.order, project_id=project_id, status=data.status)
        db.add(milestone_data)
        db.commit()
        db.refresh(milestone_data)
        return {
            "milestone_id": milestone_data.id,
            "status": milestone_data.status
        }
        
def get_timeline(project_id,db):
    milestones = db.query(milestoneModel.MilestoneModel).filter(milestoneModel.MilestoneModel.project_id == project_id).all()
    return milestones

def update_milestone(milestone_id,db,status):
    milestone = db.query(milestoneModel.MilestoneModel).filter(milestoneModel.MilestoneModel.id == milestone_id).first()
    if milestone:
        milestone.status = status
        db.commit()
        db.refresh(milestone)
        return {
            "message": "Mileston updated"
        }
        
def delete_milestone(milestone_id,db):
    milestone = db.query(milestoneModel.MilestoneModel).filter(milestoneModel.MilestoneModel.id == milestone_id).first()
    if milestone:
        db.delete(milestone)
        return {
            "message":"Milestone deleted"
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Milestone not found')
    
    
    