def user_schema(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "id": user["id"],
        "nombre": user["nombre"],
        "username": user["username"],
        "password": user["password"]
    }

def users_schema(users) -> list:
    return [user_schema(user) for user in users]

def product_schema(product) -> dict:
    return {
        "_id": str(product["_id"]),
        "id": product["id"],
        "nombre": product["nombre"],
        "marca": product["marca"],
        "precio": product["precio"]
    }

def products_schema(products) -> list:
    return [product_schema(product) for product in products]