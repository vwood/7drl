from google.appengine.ext import db

from base import *
from room import *

class Player(db.Model):
    """Models a wonderful player of our humble game."""
    name = db.StringProperty()
    user = db.UserProperty()
    location = db.ReferenceProperty(Room)
    is_alive = db.BooleanProperty()
    
def get_player(user):
    "Gets the player model of a current user."
    return Player.gql("WHERE user = :1", user).get()
    
class Move(BaseHandler):
    def post(self):
        pass
    post = require_player(post)

class CreatePlayer(BaseHandler):
    def post(self):
        player = Player()
        player.is_alive = True
        player.location = World.start
        player.put()

class CharacterGeneration(BaseHandler):
    def get(self):
        pass
