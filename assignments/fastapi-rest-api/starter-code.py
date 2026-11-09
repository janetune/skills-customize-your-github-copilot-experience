from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")

# In-memory storage
items = [
    {"id": 1, "name": "Read chapter 1", "done": False},
    {"id": 2, "name": "Practice Python", "done": True},
]


class ItemCreate(BaseModel):
    name: str
    done: bool = False


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API!"}


# Task 1: Add a GET /items route that returns all items


# Task 2: Add a GET /items/{item_id} route that returns one item


# Task 3: Add a POST /items route that creates a new item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
