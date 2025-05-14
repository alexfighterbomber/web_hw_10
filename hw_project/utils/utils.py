from pymongo import MongoClient

def get_mongo_db():
    # client = MongoClient('mongodb+srv://GOIT_hw_08:pass@cluster0.vunzj2k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    client = MongoClient('mongodb+srv://GOIT_hw_08:pass@cluster0.vunzj2k.mongodb.net/admin?retryWrites=true&loadBalanced=false&replicaSet=atlas-q8eni0-shard-0&readPreference=primary&srvServiceName=mongodb&connectTimeoutMS=10000&w=majority&authSource=admin&authMechanism=SCRAM-SHA-1')
    db =  client["authors&quotes"]
    return db
