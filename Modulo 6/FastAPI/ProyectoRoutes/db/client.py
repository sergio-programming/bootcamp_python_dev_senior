from pymongo import MongoClient

MONGO_URI = "mongodb+srv://root:admin@cluster0.42fz9ia.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# db_client = MongoClient().API_Users - Para conexion a Mongo Local

# Conexion a base de datos Mongo en la nube
client = MongoClient(MONGO_URI)
db_client = client["API_Users"]
