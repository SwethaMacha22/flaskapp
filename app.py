from flask import Flask, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Atlas connection URI
MONGO_URI = "your_mongodb_atlas_connection_string"

# Initialize MongoDB client
client = MongoClient(MONGO_URI)

# Access the shop_db database and products collection
db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    # Fetch all products from the collection
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
