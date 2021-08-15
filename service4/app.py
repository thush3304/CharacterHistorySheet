from flask import Flask, request, jsonify

app = Flask(__name__)

chara = {
    'eras': {
        'French Revolution': 1,
        'WWII': 4,
        'Modern': 7,
        'Victorian': 10
    },
    'proff': {
        'General': 5,
        'Genius': 6,
        'Villain': 7
    }
}

@app.route('/post/char', methods=['POST'])
def post_order():
    era = request.json['eras']
    prof = request.json['proff']

    charav = chara['eras'][era] + chara['proff'][prof]
    if charav == 6:
        charac = "Napolean Bonaparte, was a French military leader and emperor who conquered much of Europe in the early 19th century."
    elif charav == 7:
        charac = "Jean-Jacques Rousseau, Swiss-born philosopher, writer, and political theorist whose treatises and novels inspired the leaders of the French Revolution and the Romantic generation."
    elif charav == 8:
        charac = "Maximilien Robespierre, a radical democrat and key figure in the French Revolution of 1789."
    elif charav == 9:
        charac = "Field Marshal Bernard Law Montgomery was one of the most prominent and successful British commanders of the Second World War"
    elif charav == 10:
        charac = "Alan Mathison Turing OBE FRS was an English mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist."
    elif charav == 11:
        charac = "Adolf Hitler was an Austrian-born German politician who was the dictator of Germany from 1933 to 1945."
    elif charav == 12:
        charac = "N/A"
    elif charav == 13:
        charac = "Elon Reeve Musk FRS is an entrepreneur and business magnate."
    elif charav == 14:
        charac = "Donald John Trump is an American media personality, businessman, and politician who served as the 45th president of the United States from 2017 to 2021."
    elif charav == 15:
        charac = "Major General Sir Geoffrey Barton: Commanded the 6th Infantry Brigade during the Second Boer War."
    elif charav == 16:
        charac = "Sir Francis Galton, was an English Victorian era polymath"
    elif charav == 17:
        charac = "Jack the Ripper was an unidentified serial killer active in the largely impoverished areas in and around the Whitechapel district of London in 1888."
    return jsonify(charac)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
    