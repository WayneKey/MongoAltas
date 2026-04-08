from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://waynecheangk8_db_user:qAL9dyVZTkLAELxR@cluster0.v5cnxco.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["school_db"]
    students = db["students"]
    results = students.find()
    print("Query result:")
    for result in results:
        print(result)

except Exception as e:
    print(e)