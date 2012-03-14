from random import randint

from google.appengine.ext import db

from base import *
from room import *


class Monster(db.Model):
    """Models some hideous creature."""
    name = db.StringProperty()
    location = db.ReferenceProperty(Room)
    health = db.IntegerProperty()
    is_alive = db.BooleanProperty()
    
def move(monster):
    # is a player here?
    # dispatch based on what kind of monster I am...
    if randint(0,1) == 0:
        return
    exits = monster.location.exits
    target = randint(0, len(exits)-1)
    if exits[target] is not None:
        monster.location = exits[target]
        monster.put()

def attack():
    pass

def generate_new_monster(name):
    pass
