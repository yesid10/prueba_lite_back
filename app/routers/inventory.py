# app/routers/inventory.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.inventory import Inventory
from app.models.product import Product
from app.schemas.inventory import InventoryCreate, InventoryResponse
from app.utils.deps import admin_required
from app.models.company import Company

router = APIRouter()

@router.post("/", response_model=InventoryResponse)
def add_inventory(item: InventoryCreate, db: Session = Depends(get_db), _: str = Depends(admin_required)):
    product = db.query(Product).filter(Product.code == item.product_code).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    inv = db.query(Inventory).filter(Inventory.product_code == item.product_code).first()
    if inv:
        inv.quantity += item.quantity
    else:
        inv = Inventory(product_code=item.product_code, quantity=item.quantity)
        db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv

@router.get("/")
def get_full_inventory(db: Session = Depends(get_db)):
    results = (
        db.query(
            Inventory.id,
            Inventory.quantity,
            Product.code,
            Product.name.label("product_name"),
            Product.price_cop,
            Product.price_usd,
            Product.price_eur,
            Company.nit.label("company_nit"),
            Company.name.label("company_name")
        )
        .join(Product, Inventory.product_code == Product.code)
        .join(Company, Product.company_nit == Company.nit)
        .all()
    )

    return [
        {
            "id": r.id,
            "product_code": r.code,
            "product_name": r.product_name,
            "price_cop": r.price_cop,
            "price_usd": r.price_usd,
            "price_eur": r.price_eur,
            "company_nit": r.company_nit,
            "company_name": r.company_name,
            "quantity": r.quantity
        }
        for r in results
    ]
