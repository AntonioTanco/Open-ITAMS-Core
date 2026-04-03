from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
db_secret_user = os.getenv("DB_USERNAME")
db_secret_pass = os.getenv("DB_PASSWORD")


uri = f"mongodb+srv://{db_secret_user}:{db_secret_pass}@cluster0.hqwq2.mongodb.net/?appName=Cluster0"
# Create a new client and connectd to the server
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