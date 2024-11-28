from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int

products = []

@app.get("/cart")
async def view_cart():
    return products

@app.delete("/cancel")
async def cancel():
    products = []

@app.post("/add")
async def add_item(product: Item):
    products.append(product)
