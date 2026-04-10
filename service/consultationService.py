from model import consultationModel
from fastapi import HTTPException, status
from schema import consultationSchema
from repository import database

consultationModel.database.Base.metadata.create_all(database.engine)


def create_consultation(email,data,db):
    consultation_data = consultationModel.ConsultationModel(type=data.type,scheduled_at = data.scheduled_at, project_stage=data.project_stage, site_location=data.site_location, budget_range = data.budget_range, key_concerns=data.key_concerns, status=consultationSchema.ConsultationStatus.pending, client_email=email)
    db.add(consultation_data)
    db.commit()
    db.refresh(consultation_data)
    
    return {
        "consultation_id": consultation_data.id,
        "status":consultation_data.status
    }
    
def get_my_consultations(email,db):
    consultation_list = db.query(consultationModel.ConsultationModel).filter(consultationModel.ConsultationModel.client_email == email).all()
    return consultation_list

def get_consultations(db):
    consultation_list = db.query(consultationModel.ConsultationModel).all()
    return consultation_list

def update_consultation(id, data, db):
    consultation_data = db.query(consultationModel.ConsultationModel).filter(consultationModel.ConsultationModel.id == id).first()
    if consultation_data:
        consultation_data.status = data.status
        db.commit()
        db.refresh(consultation_data)
        return {
            "message": "Consultation updated"
        } 
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Consultation Not found')
    
    

