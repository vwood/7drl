from random import randint

from google.appengine.ext import db

import base
import room
import images

class Monster(db.Model):
    """Models some hideous creature."""
    name = db.StringProperty()
    creature_type = db.IntegerProperty()
    image = db.IntegerProperty()
    location = db.ReferenceProperty(room.Room)
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

def generate_new_monster(room):
    m = Monster()
    m.creature_type = randint(0, len(images.creatures) - 1)
    m.image = images.creatures[m.creature_type]
    m.name = images.images[m.image].replace(".png", "")
    m.health = images.monster_health[m.creature_type]
    m.location = room
    m.is_alive = True
    m.put()
