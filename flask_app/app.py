from flask import Flask, render_template
from pymongo import MongoClient

# Create the Flask application
app = Flask(__name__)

# MongoDB Atlas connection string
mongo_uri = "mongodb+srv://RpdCyclone:actionsoverwords@shopcluster.tnrgm.mongodb.net/?retryWrites=true&w=majority&appName=ShopCluster"

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