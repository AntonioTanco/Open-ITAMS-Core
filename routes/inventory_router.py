from fastapi import APIRouter
from db.database import datebase
from models.assetModel import assetModel
from utils.generateAssetID import generate_uuid

inv_router = APIRouter()

# assets = {
#     "name": "Lenovo",
#     "model": "X1",
#     "assignedUser": "Alex Joe"
# }

@inv_router.get("/inventory/")
async def read_inventory():

    return {"Inventory": None}

@inv_router.post("/inventory/create")
async def create_inventory_record(asset : assetModel):

    id = generate_uuid()

    datebase['assets'].insert_one(asset.model_dump())

    return {"message": "new recorded created" , "laptop": asset, "id": id}