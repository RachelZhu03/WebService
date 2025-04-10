import csv
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_db"]
collection = db["products"]


with open("auto_products.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = []

    for row in reader:
        # name issue fix
        row = {k.strip(): v.strip() for k, v in row.items()}

        data.append({
            "ProductID": row["Product ID"],
            "Name": row["Name"],
            "UnitPrice": float(row["Unit Price"]),
            "StockQuantity": int(row["Stock Quantity"]),
            "Description": row["Description"]
        })

collection.insert_many(data)
print(f"{len(data)} products inserted into MongoDB ✅")
