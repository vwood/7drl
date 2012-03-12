from base import *
from google.appengine.ext import db

class Item(db.Model):
    """Models some strange artefact of mystery and power."""
    name = db.StringProperty()
    location = db.ReferenceProperty(None)
    
def drop(item):
    if item.location.kind() == "Player":
        location = item.location.location
