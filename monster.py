from random import randint

from google.appengine.ext import db

import base
import room
import images
import player

class Monster(db.Model):
    """Models some hideous creature."""
    name = db.StringProperty()
    creature_type = db.IntegerProperty()
    image = db.IntegerProperty()
    location = db.ReferenceProperty(room.Room)
    health = db.IntegerProperty()
    attack = db.IntegerProperty()
    is_alive = db.BooleanProperty()
    has_moved = db.BooleanProperty()
    
def move(monster):
    # is a player here?
    # dispatch based on what kind of monster I am...

    if monster.has_moved:
        monster.has_moved == False
        monster.put()
        return

    players = player.Player.all(keys_only=True).filter("location =", monster.location.key())
    if len(players) > 0:
        target = players[randint(0, len(players) - 1)]
        combat.monster_attack(monster, target)
        return

    if randint(0,1) == 0:
        return

    exits = monster.location.exits
    target = randint(0, len(exits)-1)
    if exits[target] is not None:
        monster.location = exits[target]
        monster.put()

def generate_new_monster(room):
    m = Monster()
    m.creature_type = randint(0, len(images.creatures) - 1)
    m.image = images.creatures[m.creature_type]
    m.name = images.images[m.image].replace(".png", "").replace("_", " ")
    m.health = images.monster_health[m.creature_type]
    m.attack = images.monster_attack[m.creature_type]
    m.location = room
    m.is_alive = True
    m.has_moved = False
    m.put()
