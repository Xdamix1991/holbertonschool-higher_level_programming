from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def read_csv(filename):
    products = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["price"] = float(row["price"])
            row["id"] = int(row["id"])
            products.append(row)
    return products


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []
    return render_template('items.html', items=items)


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        try:
            products = read_json('products.json')
        except FileNotFoundError:
            error = "JSON file not found."
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except FileNotFoundError:
            error = "CSV file not found."
    else:
        error = "Wrong source. Please specify 'json' or 'csv'."

    if not error and product_id:
        products = [product for product in products if product.get("id") == product_id]
        if not products:
            error = "Product not found."

    return render_template("product_display.html", products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
