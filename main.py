from fastapi import FastAPI

import uvicorn

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello_index():
    return {
        "message": "hello index",
    }


@app.get("/hello/")
def hello_name(name: str = "User"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.post("/calc/add/")
def add(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
