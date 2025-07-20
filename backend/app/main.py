"""TODO add comentários"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """TODO add comentários"""

    return {"msg": "Hello World"}
