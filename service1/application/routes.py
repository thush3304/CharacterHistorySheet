from flask import render_template
import requests


from . import app, db
from .model import Character

@app.route('/')
def home():
    dama = requests.get('http://service-2:5000/get/dama').text
    accessory = requests.get('http://service-3:5000/get/accessories').text

    print(dama, accessory)

    price_request = {'damas': dama, 'accessories': accessory}
    price = requests.post('http://service-4:5000/post/order', json=price_request).json()

    order = Character(dama=dama, accessory=accessory, price=price)
    db.session.add(order)
    db.session.commit()

    order_history = Character.query.order_by(Character.id.desc()).limit(5).all()
        
    return render_template("home.html", orders=order_history, current_order=order)