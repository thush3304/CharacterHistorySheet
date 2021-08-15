from flask import Flask
import random

app = Flask(__name__)

era = ["French Revolution", "Chola Dynasty", "WWII", "Modern", "DBZ", "Victorian"]

@app.route('/get/era')
def get_era():
    return random.choice(era)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
