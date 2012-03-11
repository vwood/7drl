from google.appengine.ext import db

class Player(db.Model):
    """Models a wonderful player of our humble game."""
    name = db.StringProperty()
    user = db.UserProperty()
    location = db.ReferenceProperty(Room)

