# pip install "fastapi[standard]"
# uvicorn main:app --host 0.0.0.0 --port 8000

from fastapi import FastAPI
from routers import musicians_router, songs_router

app = FastAPI()
app.include_router(musicians_router)
app.include_router(songs_router)
