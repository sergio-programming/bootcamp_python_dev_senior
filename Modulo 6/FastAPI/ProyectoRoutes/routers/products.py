from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    nombre: str
    marca: str
    precio: int

class ProductUpdate(BaseModel):
    nombre: str
    marca: str
    precio: int

products = []

router = APIRouter()

@router.get('/')
async def getProducts():
    if not products:
        raise HTTPException(status_code=404, detail="No hay productos registrados actualmente")
    return JSONResponse(status_code=200, content={"productos": [product.dict() for product in products]})

@router.get('/{product_id}')
async def getProductById(product_id: int):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail=f"No se encontro un producto con id {product_id}")
    return JSONResponse(status_code=200, content={"producto": product.dict()})

@router.post('/')
async def createProduct(product: Product):
    validatingProduct = next((p for p in products if p.id == product.id), None)
    if validatingProduct:
        raise HTTPException(status_code=409, detail=f"Ya se encuentra un producto registrado con el id {product.id}")
    products.append(product)
    return JSONResponse(status_code=201, content={"mensaje": f"Producto con id {product.id} registrado exitosamente"})

@router.put('/{product_id}')
async def updateProduct(product_id: int, product: ProductUpdate):
    product_to_update = next((p for p in products if p.id == product_id), None)
    if not product_to_update:
        raise HTTPException(status_code=404, detail=f"No se encontro un producto con id {product_id}")
    product_to_update.nombre = product.nombre
    product_to_update.marca = product.marca
    product_to_update.precio = product.precio
    return JSONResponse(status_code=200, content={"mensaje": f"Producto con id {product_id} actualizado exitosamente"})

@router.delete('/{product_id}')
async def deleteUser(product_id: int):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail=f"No se encontro un producto con id {product_id}")
    products.remove(product)
    return JSONResponse(status_code=200, content={"mensaje": f"Producto con id {product_id} eliminado exitosamente"})