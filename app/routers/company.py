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

@router.delete("/{nit}", response_model=CompanyResponse)
def delete_company(nit: str, db: Session = Depends(get_db), _: str = Depends(admin_required)):
    db_company = db.query(Company).filter(Company.nit == nit).first()
    if not db_company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    db.delete(db_company)
    db.commit()
    return db_company

@router.put("/{nit}", response_model=CompanyResponse)
def update_company(nit: str, company: CompanyCreate, db: Session = Depends(get_db), _: str = Depends(admin_required)):
    db_company = db.query(Company).filter(Company.nit == nit).first()
    if not db_company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    db_company.name = company.name
    db_company.address = company.address
    db_company.phone = company.phone
    db.commit()
    db.refresh(db_company)
    return db_company
