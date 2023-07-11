from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id_int": item_id}

@app.get("/item/{item}")
async def read_item(item: str):
    return {"item_id_str": item}


@app.post("/items/")
async def create_item(item: Item):
    return item
# {
#     "name": "Foo",
#     "description": "An optional description",
#     "price": 45.2,
# }

