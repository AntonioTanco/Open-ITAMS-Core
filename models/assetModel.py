from pydantic import BaseModel

class assetModel(BaseModel):
    name: str
    model: str
    serialNumber: str
    assignedUser: str