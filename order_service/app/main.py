from fastapi import FastAPI
from api.orders import orders_router

app = FastAPI()

@app.get("/health")
async def health():
    return { "status": "ok" }


app.include_router(orders_router)