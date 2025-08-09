from sqlalchemy import Column, String, Integer, Enum
from app.database import Base
import enum

class RoleEnum(enum.Enum):
    admin = "admin"
    externo = "externo"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
