from fastapi import APIRouter

orders_router = APIRouter(prefix="/orders", tags=["orders"])

@orders_router.post("/")
async def create_order():
    return "not implemented yet"

@orders_router.get("/")
async def orders():
    return []