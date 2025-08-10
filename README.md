# 🚀 Backend Prueba Lite

Sistema de gestión de inventario y productos con autenticación y autorización basado en roles.

## 📋 Descripción del Proyecto

Este es un backend desarrollado en **FastAPI** que proporciona una API REST completa para la gestión de:
- **Usuarios** con sistema de autenticación JWT
- **Empresas** con información de contacto y ubicación
- **Productos** con precios en múltiples monedas
- **Inventario** para el control de stock

## 🏗️ Arquitectura del Proyecto

```
back/
├── app/
│   ├── models/          # Modelos de base de datos SQLAlchemy
│   ├── schemas/         # Esquemas Pydantic para validación
│   ├── routers/         # Endpoints de la API
│   ├── services/        # Lógica de negocio
│   ├── utils/           # Utilidades (autenticación, dependencias)
│   ├── config.py        # Configuración del proyecto
│   ├── database.py      # Configuración de base de datos
│   └── main.py          # Punto de entrada de la aplicación
└── requirements.txt     # Dependencias del proyecto
```

## 🛠️ Tecnologías Utilizadas

- **FastAPI** - Framework web moderno y rápido para Python
- **SQLAlchemy** - ORM para base de datos
- **PostgreSQL** - Base de datos relacional
- **Pydantic** - Validación de datos y serialización
- **JWT** - Autenticación basada en tokens
- **bcrypt** - Encriptación de contraseñas
- **Uvicorn** - Servidor ASGI

## 📦 Dependencias Principales

- `fastapi==0.116.1` - Framework web
- `sqlalchemy==2.0.42` - ORM
- `psycopg2-binary==2.9.10` - Driver de PostgreSQL
- `pydantic==2.11.7` - Validación de datos
- `PyJWT==2.10.1` - Manejo de tokens JWT
- `bcrypt==4.3.0` - Encriptación
- `uvicorn==0.35.0` - Servidor ASGI

## 🚀 Instalación y Configuración

### 1. Prerrequisitos

- Python 3.8 o superior
- PostgreSQL instalado y ejecutándose
- pip (gestor de paquetes de Python)

### 2. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd back
```

### 3. Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
# Base de datos
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_base_datos

# JWT
SECRET_KEY=tu_clave_secreta_muy_larga_y_segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Configuración de la aplicación
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### 6. Configurar Base de Datos

```sql
-- Crear base de datos
CREATE DATABASE nombre_base_datos;

-- Crear usuario (opcional)
CREATE USER usuario WITH PASSWORD 'contraseña';
GRANT ALL PRIVILEGES ON DATABASE nombre_base_datos TO usuario;
```

## 🏃‍♂️ Ejecutar la Aplicación

### Desarrollo

```bash
# Opción 1: Usando Python directamente
python app/main.py

# Opción 2: Usando Uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Producción

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 📚 Documentación de la API

Una vez ejecutada la aplicación, puedes acceder a:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/health`

## 🔐 Sistema de Autenticación

### Roles de Usuario

- **admin**: Acceso completo a todas las funcionalidades
- **externo**: Acceso limitado a ciertas operaciones

### Endpoints de Autenticación

- `POST /auth/register` - Registro de usuarios
- `POST /auth/login` - Inicio de sesión

### Uso de Tokens

```bash
# Ejemplo de uso con curl
curl -H "Authorization: Bearer tu_token_jwt" \
     http://localhost:8000/companies
```

## 🏢 Modelos de Datos

### Usuario (User)
- `id`: Identificador único
- `email`: Correo electrónico (único)
- `password`: Contraseña encriptada
- `role`: Rol del usuario (admin/externo)

### Empresa (Company)
- `nit`: Número de identificación tributaria (clave primaria)
- `name`: Nombre de la empresa
- `address`: Dirección
- `phone`: Teléfono
- `email`: Correo electrónico


### Producto (Product)
- `code`: Código del producto (clave primaria)
- `name`: Nombre del producto
- `features`: Características del producto
- `price_cop`: Precio en pesos colombianos
- `price_usd`: Precio en dólares estadounidenses
- `price_eur`: Precio en euros
- `company_nit`: NIT de la empresa (clave foránea)

### Inventario (Inventory)
- `id`: Identificador único
- `product_code`: Código del producto (clave foránea)
- `quantity`: Cantidad en stock

## 🔌 Endpoints Disponibles

### Autenticación
- `POST /auth/register` - Registro de usuarios
- `POST /auth/login` - Inicio de sesión

### Empresas
- `GET /companies` - Listar todas las empresas
- `GET /companies/{nit}` - Obtener empresa por NIT
- `POST /companies` - Crear nueva empresa
- `PUT /companies/{nit}` - Actualizar empresa
- `DELETE /companies/{nit}` - Eliminar empresa

### Productos
- `GET /products` - Listar todos los productos
- `GET /products/{code}` - Obtener producto por código
- `POST /products` - Crear nuevo producto
- `PUT /products/{code}` - Actualizar producto
- `DELETE /products/{code}` - Eliminar producto

### Inventario
- `GET /inventory` - Listar todo el inventario
- `GET /inventory/{id}` - Obtener item de inventario
- `POST /inventory` - Crear nuevo item de inventario
- `PUT /inventory/{id}` - Actualizar item de inventario
- `DELETE /inventory/{id}` - Eliminar item de inventario


## 📊 Base de Datos

### Crear Tablas

Las tablas se crean automáticamente al ejecutar la aplicación gracias a:

```python
Base.metadata.create_all(bind=engine)
```
---

**¡Disfruta desarrollando con Backend Prueba Lite! 🎉**
