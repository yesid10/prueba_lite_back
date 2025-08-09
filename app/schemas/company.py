from pydantic import BaseModel

class CompanyBase(BaseModel):
    nit: str
    name: str
    address: str
    phone: str

class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    class Config:
        from_attributes = True
