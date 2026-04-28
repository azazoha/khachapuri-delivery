from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.orders import orders_router
from db.base import Base
from db.session import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Database initialized")

    yield
    engine.dispose()
    print("Application stopped")

app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health():
    return { "status": "ok" }


app.include_router(orders_router)