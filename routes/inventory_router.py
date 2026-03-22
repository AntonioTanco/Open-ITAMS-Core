from fastapi import APIRouter
from db.database import client

inv_router = APIRouter()


@inv_router.get("/inventory/")
async def read_inventory():

    return {"Inventory": None}

@inv_router.post("/inventory/create")
async def create_inventory_record():
    db_conn = client.list_database_names()
    return {db_conn}