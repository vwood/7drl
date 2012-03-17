from random import randint

from google.appengine.ext import db

import base
import room
import images
import player
import combat

class Monster(db.Model):
    """Models some hideous creature."""
    name = db.StringProperty()
    creature_type = db.IntegerProperty()
    image = db.IntegerProperty()
    location = db.ReferenceProperty(room.Room)
    health = db.IntegerProperty()
    attack = db.IntegerProperty()
    is_alive = db.BooleanProperty()
    is_hostile = db.BooleanProperty()
    has_moved = db.BooleanProperty()
    
def move(monster):
    # is a player here?
    # dispatch based on what kind of monster I am...

    if monster.has_moved:
        monster.has_moved == False
        monster.put()
        return

    if monster.is_hostile:
        players = player.Player.all(keys_only=True).filter("location =", monster.location.key())
        players = list(players)
        if len(players) > 0:
            target = player.Player.get(players[randint(0, len(players) - 1)])
            combat.monster_attack(monster, target)
            return

    if randint(0,1) == 0:
        return

    exits = monster.location.exits
    exit_keys = monster.location.exit_keys
    target = randint(0, len(exits)-1)
    if exits[target] != -1 and target != 4:
        monster.location = exit_keys[exits[target]]
        monster.put()

def generate_new_monster(room):
    m = Monster()
    m.creature_type = randint(0, len(images.creatures) - 1)
    m.image = images.creatures[m.creature_type]
    m.name = images.images[m.image].replace(".png", "").replace("_", " ")
    m.health = images.monster_health[m.creature_type]
    m.attack = images.monster_attack[m.creature_type]
    m.is_hostile = images.monster_is_hostile[m.creature_type]
    m.location = room
    m.is_alive = True
    m.has_moved = False
    m.put()
