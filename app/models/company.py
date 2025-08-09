from sqlalchemy import Column, String
from app.database import Base

class Company(Base):
    __tablename__ = "companies"
    nit = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
