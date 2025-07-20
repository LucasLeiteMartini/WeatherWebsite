"""TODO add comentários"""

if __name__ == "__main__":
    import os

    import uvicorn

    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", "8000"))

    uvicorn.run("app.main:app", host=HOST, port=PORT, timeout_keep_alive=600)
