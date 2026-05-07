from fastapi import APIRouter
from db.database import datebase
from models.assetModel import assetModel, assetResponseModel
from utils.generateAssetID import generate_uuid

inv_router = APIRouter()

laptop = {
    "name": "Lenovo",
    "model": "X1",
    "assignedUser": "Alex Joe"
}

@inv_router.get("/inventory/")
async def read_inventory():

    return {"Inventory": None}

@inv_router.post("/inventory/create")
async def create_inventory_record(asset : assetModel):

    id = generate_uuid()

    # asset.uuid = str(id)

    response_1 = assetResponseModel(uuid=id, name=asset.name, model=asset.model, serialNumber=asset.serialNumber, assignedUser=asset.assignedUser).model_dump()


    try:
        response = asset.model_dump()

        print(response)
        datebase["assets"].insert_one(response_1)
        print(response_1)

        return response

    except Exception as e:
        
        return {e}

    # return {"message": "new recorded created" , "laptop": asset}

@inv_router.get("/inventory/{id}")
async def find_inventory_record(assetID : str):

    try:

        found_asset = datebase["assets"].find_one({"uuid": assetID})
        
        asset = found_asset["name"]

        return asset

    except Exception as e:
        
        return {e}
    
@inv_router.post("/inventory/{id}")
async def modify_inventory_record(assetID : str, new_name: str):

    try:

        datebase["assets"].update_one({"uuid": assetID}, { "$set": {"name": new_name}})

        found_asset = datebase["assets"].find_one({"uuid": assetID})

        return found_asset["name"]
    
    except Exception as e:
        
        return {e}