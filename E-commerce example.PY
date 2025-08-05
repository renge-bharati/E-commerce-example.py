# example.py
from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'

# In‑memory product catalog
PRODUCTS = {
    1: {'name': 'T‑shirt A', 'price': 20},
    2: {'name': 'Sneaker X', 'price': 55},
}

@app.route('/')
def index():
    return render_template_string('''
        <h1>Products</h1>
        <ul>
        {% for pid, prod in products.items() %}
          <li>{{ prod.name }} — ₹{{ prod.price }}
            <a href="{{ url_for('add_to_cart', product_id=pid) }}">Add to cart</a>
          </li>
        {% endfor %}
        </ul>
        <a href="{{ url_for('view_cart') }}">View Cart</a>
    ''', products=PRODUCTS)

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    items = [(PRODUCTS[pid], qty) for pid, qty in cart.items()]
    total = sum(prod['price'] * qty for prod, qty in items)
    return render_template_string('''
        <h1>Your Cart</h1>
        {% if items %}
          <ul>
          {% for prod, qty in items %}
            <li>{{ prod.name }} × {{ qty }} = ₹{{ prod.price * qty }}</li>
          {% endfor %}
          </ul>
          <p><strong>Total: ₹{{ total }}</strong></p>
          <form action="{{ url_for('checkout') }}" method="post">
            <button type="submit">Checkout</button>
          </form>
        {% else %}
          <p>Cart is empty.</p>
        {% endif %}
        <a href="{{ url_for('index') }}">Continue Shopping</a>
    ''', items=items, total=total)

@app.route('/checkout', methods=['POST'])
def checkout():
    session.pop('cart', None)
    return "<h1>Order placed! Thanks 🎉</h1><a href='/'>Back to shop</a>"

if __name__ == '__main__':
    app.run(debug=True)
