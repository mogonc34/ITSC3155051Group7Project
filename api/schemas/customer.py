from pydantic import ConfigDict, BaseModel, EmailStr
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: Optional[str] = None
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class CustomerResponse(CustomerBase):
    customer_id: int
    model_config = ConfigDict(from_attributes=True)
