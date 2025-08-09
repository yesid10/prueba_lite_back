# app/schemas/inventory.py
from pydantic import BaseModel

class InventoryBase(BaseModel):
    product_code: str
    quantity: int

class InventoryCreate(InventoryBase):
    pass

class InventoryResponse(InventoryBase):
    id: int
    class Config:
        from_attributes = True
