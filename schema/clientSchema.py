from pydantic import BaseModel


class ClientProfileSchema(BaseModel):
    full_name: str
    country: str
    phone: str
    preferred_currency: str
    
class UpdateClientProfileSchema(BaseModel):
    full_name: str
    phone: str
    preferred_currency: str
    
    