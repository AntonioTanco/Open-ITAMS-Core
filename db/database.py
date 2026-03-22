from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
DB_SECRET_USER = os.getenv("DB_USERNAME")
DB_SECRET_PASS = os.getenv("DB_PASSWORD")

print(DB_SECRET_USER)
print(DB_SECRET_PASS)

uri = f"mongodb+srv://{DB_SECRET_USER}:{DB_SECRET_PASS}@cluster0.hqwq2.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')

    print("Pinged your deployment. You successfully connected to MongoDB!")

    print("Creating DB Collection....")

    datebase = client["openITAMS"]

    datebase.create_collection("assets")
    

except Exception as e:
    print(e)