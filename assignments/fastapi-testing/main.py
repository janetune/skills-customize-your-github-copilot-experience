from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")

INITIAL_ITEMS = [
    {"id": 1, "name": "Read chapter 1", "done": False},
    {"id": 2, "name": "Practice Python", "done": True},
]
items = [item.copy() for item in INITIAL_ITEMS]


class ItemCreate(BaseModel):
    name: str
    done: bool = False


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API!"}


@app.get("/items")
def read_items():
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    new_item = {"id": max((item["id"] for item in items), default=0) + 1, **item.model_dump()}
    items.append(new_item)
    return new_item
