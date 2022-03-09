"""
Minimal FastAPI application taken directly from the tutorial.
https://fastapi.tiangolo.com/
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World!"}


@app.get("/new")
def read_root():
    return {"New!!": "Path!"}


@app.get("/new-features")
def read_root():
    return {"New!!!!!": "Path!!!!!!"}


@app.get("/new-feature2")
def read_root():
    return {"New!!": "Path!"}


@app.get("/new-path3123")
def read_root():
    return {"Another New!!!": "Path!"}


@app.get("/another-refactor")
def read_root():
    return {"Another New!!!!": "Path!!"}


@app.get("/new-path")
def read_root():
    return {"Another New!!!!!": "Path!!"}


@app.get("/new-path-2")
def read_root():
    return {"Another New!!!!!!!": "Path!!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
