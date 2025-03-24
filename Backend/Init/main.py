from fastapi import FastAPI
from uuid import UUID
from pydantic import BaseModel
from typing import TypedDict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message" : "test"}


@app.get("/test")
async def getTestObject():
    return {"Name" : "Luks", 
            "Age": 28,
            "Occupation" : "Student", 
            "IsinDHMaster" : True,
            }

@app.post("/test")
async def postObject():
    return None

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


items = {}


@app.get("/items")
def get_all_item():
    print("Get all Items triggered with: ", items)
    return items

@app.get("/items{id}")
def get_item(id: int):
    if id not in items:
        return {"error":"item not found"}
    return items[id]

@app.post("/items/new")
def post_item(item: Item ) -> dict:
    items[item.id] = item
    print(items)
    return {"data":"item added"}

"""
@app.put("/items/edit{id}")
async def update_item(id: int, item: UpdatedItem):
    if id not in items:
        return {"error", "item not found"}
    if item.name != None:
        items[id].name = item.name
    if item.price != None:
        items[id].price = item.price

"""
