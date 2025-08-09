from pydantic import BaseModel

class ProductBase(BaseModel):
    code: str
    name: str
    features: str
    price_cop: float
    price_usd: float
    price_eur: float
    company_nit: str

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    class Config:
        from_attributes = True
