from pydantic import BaseModel
from typing import Optional

class ResourceManagement(BaseModel):
    ingredient: Optional[str]
    amount: int
    unit: int

class ResourceManagementCreate(BaseModel):
    pass

class ResourceManagementUpdate(BaseModel):
    id: int


    class Config:
        from_attributes = True