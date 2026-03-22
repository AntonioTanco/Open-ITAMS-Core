from fastapi import APIRouter

inv_router = APIRouter()


@inv_router.get("/inventory/")
async def read_inventory():

    return {"Inventory": None}