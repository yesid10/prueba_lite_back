from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.utils.deps import admin_required

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db), _: str = Depends(admin_required)):
    db_product = db.query(Product).filter(Product.code == product.code).first()
    if db_product:
        raise HTTPException(status_code=400, detail="Producto ya existe")
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.put("/{code}", response_model=ProductResponse)
def update_product(code: str, product: ProductCreate, db: Session = Depends(get_db), _: str = Depends(admin_required)):
    db_product = db.query(Product).filter(Product.code == code).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db_product.name = product.name
    db_product.features = product.features
    db_product.price_cop = product.price_cop
    db_product.price_usd = product.price_usd
    db_product.price_eur = product.price_eur
    db_product.company_nit = product.company_nit
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/{code}", response_model=ProductResponse)
def delete_product(code: str, db: Session = Depends(get_db), _: str = Depends(admin_required)):
    db_product = db.query(Product).filter(Product.code == code).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(db_product)
    db.commit()
    return db_product
