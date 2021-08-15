from flask import render_template
import requests


from . import app, db
from .model import Character

@app.route('/')
def home():
    era = requests.get('http://service2:5000/get/era').text
    prof = requests.get('http://service3:5000/get/prof').text

    print(era, prof)

    char_random = {'eras': era, 'proff': prof}
    char = requests.post('http://service4:5000/post/char', json=char_random).json()

    order = Character(era=era, prof=prof, char=char)
    db.session.add(order)
    db.session.commit()

    order_history = Character.query.order_by(Character.id.desc()).limit(5).all()
        
    return render_template("home.html", orders=order_history, current_order=order)