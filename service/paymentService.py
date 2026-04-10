from fastapi import HTTPException, status
from repository import database
import requests
from model import paymentModel
from service import projectService
import os
import dotenv

dotenv.load_dotenv()
PAYMENT_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY')

def init_payment(data, email, db):
    payload = {
        "email": email,
        "amount": str(data.amount)
    }
    headers = {
        "Content-Type":'application/json',
        "Authorization": f'Bearer {PAYMENT_SECRET_KEY}'
    }
    url = 'https://api.paystack.co/transaction/initialize'
    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    print(response_data)
 
    db_data = {
        "project_id": data.project_id,
        "url": response_data['data']['authorization_url'],
        "access_code": response_data['data']['access_code'],
        "reference": response_data['data']['reference'],
        "email": email
    }
    create_payment(db_data,db)
    
def create_payment(data,db):
    project_data = projectService.get_project_by_id(data['project_id'],db)
    if project_data:
        payment_data = paymentModel.PaymentModel(email=data.email, reference=data.reference, access_code=data.access_code, amount=data.amount, project_id = data.project_id)
        db.add(payment_data)
        db.commit()
        db.refresh(payment_data)
        
        return {
            "payment_url": data.url
        }
        
def verify_payment(reference,db):
    headers = {
        "Authorization": f'{PAYMENT_SECRET_KEY}'
    }
    url = f'https://api.paystack.co/transaction/verify/{reference}'
    response = requests.get(url, headers=headers)
    response_data = response.data
    update_payment_status(response_data.reference,db)
    return response_data

def update_payment_status(reference,db):
    payment_data = db.query(paymentModel.PaymentModel).filter(paymentModel.PaymentModel.referece == reference).first()
    if payment_data:
        payment_data.reference = reference
        db.commit()
        db.refresh(payment_data)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Payment not found')