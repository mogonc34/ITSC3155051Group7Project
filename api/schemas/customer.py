from pydantic import BaseModel, EmailStr
from typing import Optional, List

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: Optional[str]
    address: Optional[str]

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True
