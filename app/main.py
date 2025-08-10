from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import auth, company, product, inventory


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend Prueba Lite")

# Habilitar CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],  # Cambia esto por los dominios permitidos si es necesario
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)



app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(company.router, prefix="/companies", tags=["Companies"])
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)