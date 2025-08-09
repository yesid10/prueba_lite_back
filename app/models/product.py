from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    code = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    features = Column(String)
    price_cop = Column(Float, nullable=False)
    price_usd = Column(Float, nullable=False)
    price_eur = Column(Float, nullable=False)
    company_nit = Column(String, ForeignKey("companies.nit"), nullable=False)

    company = relationship("Company")
