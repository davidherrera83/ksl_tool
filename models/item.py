from pydantic import BaseModel
from typing import List

class ItemModel(BaseModel):
    name: str
    photoPaths: List[str]
