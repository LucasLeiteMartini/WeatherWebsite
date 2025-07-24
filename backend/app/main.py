"""TODO add comentários"""

from fastapi import FastAPI

from .routes.map import map_router

app = FastAPI()

app.include_router(map_router)


@app.get("/")
async def root():
    """TODO add comentários"""

    return {"msg": "Hello World"}
