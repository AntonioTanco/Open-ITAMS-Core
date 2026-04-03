from fastapi import FastAPI

from routes.inventory_router import inv_router
from utils.generateAssetID import generate_uuid

app = FastAPI()

app.include_router(inv_router)

@app.get('/')
async def root():

    genID = generate_uuid()

    print(genID)
    return {f"Dev Status": "test", "id": {genID}}