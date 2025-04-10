from fastapi import FastAPI, Query
from pymongo import MongoClient
import requests
from pydantic import BaseModel


app = FastAPI()

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_db"]
products = db["products"]

# /getAll
@app.get("/getAll")
def get_all():
    return list(products.find({}, {"_id": 0}))

# /getSingleProduct?id=AUTO0001
@app.get("/getSingleProduct")
def get_single(id: str):
    product = products.find_one({"ProductID": id}, {"_id": 0})
    return product if product else {"error": "Product not found"}

# /addNew
@app.get("/addNew")
def add_new(ProductID: str, Name: str, UnitPrice: float, StockQuantity: int, Description: str):
    new_product = {
        "ProductID": ProductID,
        "Name": Name,
        "UnitPrice": UnitPrice,
        "StockQuantity": StockQuantity,
        "Description": Description
    }
    products.insert_one(new_product)
    return {"status": "inserted"}

# /deleteOne
@app.get("/deleteOne")
def delete_one(id: str):
    result = products.delete_one({"ProductID": id})
    return {"status": "deleted"} if result.deleted_count else {"error": "Product not found"}

# /startsWith
@app.get("/startsWith")
def starts_with(letter: str):
    result = list(products.find({"Name": {"$regex": f"^{letter}", "$options": "i"}}, {"_id": 0}))
    return result

# /paginate
@app.get("/paginate")
def paginate(start: str, end: str):
    result = list(products.find(
        {"ProductID": {"$gte": start, "$lte": end}},
        {"_id": 0}
    ).limit(10))
    return result

# /convert
@app.get("/convert")
def convert_price(id: str = Query(..., description="Product ID to convert price")):
    product = products.find_one({"ProductID": id}, {"_id": 0})
    if not product:
        return {"error": "Product not found"}
    try:
        # Using Frankfurter (no API key required)
        res = requests.get("https://api.frankfurter.app/latest?from=USD&to=EUR")
        rate = res.json()["rates"]["EUR"]
        euro = round(product["UnitPrice"] * rate, 2)
        return {"ProductID": id, "PriceEuro": euro}
    except:
        return {"error": "Conversion failed"}
