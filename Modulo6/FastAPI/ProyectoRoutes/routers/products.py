from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from models.products import Product, ProductUpdate
from db.client import db_client
from routers.utils import product_schema, products_schema


# products = []

router = APIRouter()

@router.get('/products/')
async def getProducts():
    products_db = db_client.products.find()
    products = products_schema(products_db)
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay productos registrados actualmente")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"productos": products})

@router.get('/products/{product_id}')
async def getProductById(product_id: int):
    product_db = db_client.products.find_one({"id": product_id})
    if not product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encontro un producto con id {product_id}")
    product = product_schema(product_db)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"product": product})

@router.post('/products/')
async def createProduct(product: Product):
    validatingProduct = db_client.products.find_one({"id": product.id})
    if validatingProduct:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"El producto {product.nombre} ya se encuentra registrado")
    product_dict = product.dict()
    db_client.products.insert_one(product_dict)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"mensaje": f"Producto con id {product.id} registrado exitosamente"})

@router.put('/products/{product_id}')
async def updateProduct(product_id: int, product: ProductUpdate):
    product_to_update = db_client.users.find_one({"id": product_id})
    if not product_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encontro un producto con id {product_id}")
    updated_product = product.dict()
    db_client.products.update_one(
        {"id": product_id},
        {"$set": updated_product}
    )
    return JSONResponse(status_code=status.HTTP_200_OK, content={"mensaje": f"Producto con id {product_id} actualizado exitosamente"})

@router.delete('/products/{product_id}')
async def deleteProduct(product_id: int):
    product = db_client.products.find_one({"id": product_id})
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encontro un producto con id {product_id}")
    db_client.products.delete_one({"id": product_id})
    return JSONResponse(status_code=status.HTTP_200_OK, content={"mensaje": f"Producto con id {product_id} eliminado exitosamente"})


"""
@router.get('/products/')
async def getProducts():
    if not products:
        raise HTTPException(status_code=404, detail="No hay productos registrados actualmente")
    return JSONResponse(status_code=200, content={"productos": [product.dict() for product in products]})

@router.get('/products/{product_id}')
async def getProductById(product_id: int):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail=f"No se encontro un producto con id {product_id}")
    return JSONResponse(status_code=200, content={"producto": product.dict()})

@router.post('/products/')
async def createProduct(product: Product):
    validatingProduct = next((p for p in products if p.id == product.id), None)
    if validatingProduct:
        raise HTTPException(status_code=409, detail=f"Ya se encuentra un producto registrado con el id {product.id}")
    products.append(product)
    return JSONResponse(status_code=201, content={"mensaje": f"Producto con id {product.id} registrado exitosamente"})

@router.put('/products/{product_id}')
async def updateProduct(product_id: int, product: ProductUpdate):
    product_to_update = next((p for p in products if p.id == product_id), None)
    if not product_to_update:
        raise HTTPException(status_code=404, detail=f"No se encontro un producto con id {product_id}")
    product_to_update.nombre = product.nombre
    product_to_update.marca = product.marca
    product_to_update.precio = product.precio
    return JSONResponse(status_code=200, content={"mensaje": f"Producto con id {product_id} actualizado exitosamente"})

@router.delete('/products/{product_id}')
async def deleteUser(product_id: int):
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail=f"No se encontro un producto con id {product_id}")
    products.remove(product)
    return JSONResponse(status_code=200, content={"mensaje": f"Producto con id {product_id} eliminado exitosamente"})
"""