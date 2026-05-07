from pydantic import BaseModel, Field
import uuid

class assetModel(BaseModel):
    name: str
    model: str
    serialNumber: str
    assignedUser: str

# Class inherts K,V from assetModel Dataclass
class assetResponseModel(assetModel):
    uuid: str 