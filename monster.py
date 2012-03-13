from google.appengine.ext import db

from base import *
from room import *

class Monster(db.Model):
    """Models some hideous creature."""
    name = db.StringProperty()
    location = db.ReferenceProperty(Room)
    is_alive = db.BooleanProperty()
    
def move():
    pass

def attack():
    pass

def generate_new_monster(name):
    pass
