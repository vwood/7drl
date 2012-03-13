from google.appengine.ext import db

from base import *
from item_type import *

class Item(db.Model):
    """Models a particular instance of some strange
    artefact of mystery and power."""
    item_type = db.ReferenceProperty(ItemType)
    location = db.ReferenceProperty(None)
    
def drop(item):
    if item.location.kind() == "Player":
        location = item.location.location
