# app/models/inventory.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String, ForeignKey("products.code"), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)

    product = relationship("Product")
