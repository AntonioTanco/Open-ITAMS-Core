from fastapi import FastAPI

from routes.inventory_router import inv_router

app = FastAPI()

app.include_router(inv_router)

@app.get('/')
async def root():

    return {"Dev Status": "W.i.P"}