from service import projectService
from model import taskModel
from fastapi import HTTPException, status
from schema import taskSchema
from repository import database

taskModel.database.Base.metadata.create_all(database.engine)


def create_task(data, id,db):
    project_data  = projectService.get_project_by_id(id)
    if project_data:
        task = taskModel.TaskModel(title=data.title, duedate=data.duedate, project_id=project_data.id,status=data.status)
        db.add(task)
        db.commit()
        db.refresh(task)
        
        return {
            "task_id": task.id,
            "status": task.status
        }
        
def get_tasks(project_id,db):
    task_list = db.query(taskModel.TaskModel).filter(taskModel.TaskModel.project_id == project_id).all()
    if task_list:
        return task_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    
def update_task(data,task_id,db):
    task_data = db.query(taskModel.TaskModel).filter(taskModel.TaskModel.id == task_id).first()
    if task_data:
        if data.duedate:
            task_data.duedate = data.duedate
        if data.status:
            task_data.status= data.status
        return {
            "message": "Task updated"
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    
def complete_task(task_id,db):
    task_data = db.query(taskModel.TaskModel).filter(taskModel.TaskModel.id == task_id).first()
    if task_data.status.upper() == taskSchema.TaskStatus.completed:
        task_data.status = taskSchema.TaskStatus.completed
        db.commit()
        db.refresh(task_data)
        return {
            "message":"Task completed",
            "payment_status": "UNDER_REVIEW"
        }
        
    
def reject_task():
    pass