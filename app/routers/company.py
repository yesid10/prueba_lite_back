from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyResponse
from app.utils.deps import admin_required

router = APIRouter()

@router.post("/", response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db), _: str = Depends(admin_required)):
    db_company = db.query(Company).filter(Company.nit == company.nit).first()
    if db_company:
        raise HTTPException(status_code=400, detail="Empresa ya existe")
    new_company = Company(**company.dict())
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

@router.get("/", response_model=list[CompanyResponse])
def get_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()
