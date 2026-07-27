from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sample products (you can add more here later)
products = [
    {"id": 1, "name": "Wireless Headphones", "category": "Electronics", "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e", "link": "YOUR_AMAZON_LINK_1", "hashtags": "#TechDeals #HeadphoneLovers"},
    {"id": 2, "name": "Summer Dress", "category": "Fashion", "image": "https://images.unsplash.com/photo-1529139574466-a303027c1d8b", "link": "YOUR_AMAZON_LINK_2", "hashtags": "#FashionFinds #SummerStyle"},
    {"id": 3, "name": "Coffee Maker", "category": "Home", "image": "https://images.unsplash.com/photo-1582015752624-2e856f56ad90", "link": "YOUR_AMAZON_LINK_3", "hashtags": "#HomeEssentials #CoffeeLovers"},
]

# The webpage design
PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shop Awesome Deals</title>
    <style>
        body {
            background: linear-gradient(135deg, #ff6f61, #6b48ff);
            font-family: 'Arial', sans-serif;
            color: white;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
            font-size: 48px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            margin-bottom: 30px;
        }
        .filters {
            text-align: center;
            margin-bottom: 20px;
        }
        .filters button {
            background: #ffd700;
            color: black;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 25px;
            transition: transform 0.2s;
        }
        .filters button:hover {
            transform: scale(1.1);
            background: #ff4500;
            color: white;
        }
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        .product {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s;
        }
        .product:hover {
            transform: translateY(-10px);
        }
        .product img {
            max-width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 10px;
        }
        .product h3 {
            color: #ff4500;
            font-size: 20px;
            margin: 10px 0;
        }
        .product a {
            display: inline-block;
            background: #32cd32;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 20px;
            font-weight: bold;
            margin-top: 10px;
        }
        .product a:hover {
            background: #228b22;
        }
        .hashtags {
            color: #1e90ff;
            font-size: 14px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Shop Awesome Deals</h1>
        <div class="filters">
            <button onclick="filter('All')">All</button>
            <button onclick="filter('Electronics')">Electronics</button>
            <button onclick="filter('Fashion')">Fashion</button>
            <button onclick="filter('Home')">Home</button>
        </div>
        <div class="products" id="product-grid">
            {% for product in products %}
                <div class="product" data-category="{{ product.category }}">
                    <img src="{{ product.image }}" alt="{{ product.name }}">
                    <h3>{{ product.name }}</h3>
                    <a href="{{ product.link }}" target="_blank">Shop Now</a>
                    <p class="hashtags">{{ product.hashtags }}</p>
                </div>
            {% endfor %}
        </div>
    </div>
    <script>
        function filter(category) {
            const products = document.querySelectorAll('.product');
            products.forEach(product => {
                if (category === 'All' || product.dataset.category === category) {
                    product.style.display = 'block';
                } else {
                    product.style.display = 'none';
                }
            });
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(PAGE, products=products)

if __name__ == '__main__':
    app.run(debug=True)