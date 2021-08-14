from application import db
from application.model import Character

#Destroys previous database and creates a new one
db.drop_all()
db.create_all()

character = Character(era="French Revolution", prof="Military Leader", char = "Napolean Bonaparte")

#Adds first entry to Orders table
db.session.add(character)

#Commits the changes
db.session.commit()