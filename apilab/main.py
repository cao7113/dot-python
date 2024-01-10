from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import logging

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    logging.info('hello world')
    return {"Hello": "World"}

# http://127.0.0.1:8000/items/5?q=somequery
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: Item):
    logging.info("create item %s", item)
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    logging.info("delete item %s", item_id)
    return f"deleted {item_id}"