from fastapi import APIRouter
from db.database import datebase
from models.assetModel import assetModel

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

    return {"message": "new recorded created" , "laptop": asset}