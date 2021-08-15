from flask import Flask
import random

app = Flask(__name__)

prof = ["General", "Genius", "Leader", "Villain", "Creator", "Artist"]

@app.route('/get/prof')
def get_profession():
    return random.choice(prof)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)