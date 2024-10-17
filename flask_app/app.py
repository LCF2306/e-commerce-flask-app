from flask import Flask, render_template
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Create the Flask application
app = Flask(__name__)

# MongoDB Atlas connection string from environment variables
mongo_uri = os.getenv("MONGODB_URI")

# Connect to MongoDB
try:
    client = MongoClient(mongo_uri)
    db = client['shop_db']
    products_collection = db['products']
except Exception as e:
    print("Error connecting to MongoDB:", e)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)