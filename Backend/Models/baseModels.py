from pydantic import BaseModel
from typing import TypedDict

class Location(TypedDict):
    x:int
    y:int

class Item(BaseModel):
    id:int
    name:str
    price:int
    date:str
    location:dict = {"x": 0, "y": 0}




class UpdatedItem(BaseModel):
    id:int
    name:str
    price:int
