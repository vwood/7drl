from google.appengine.api import users
from google.appengine.ext import db

from base import *
from room import *

class Player(db.Model):
    """Models a wonderful player of our humble game."""
    name = db.StringProperty()
    user = db.UserProperty()
    location = db.ReferenceProperty(Room)
    is_alive = db.BooleanProperty()
    
def get_player(user = None):
    "Gets the player model of a current user."
    if not user:
        user = users.get_current_user()
    return Player.gql("WHERE user = :1", user).get()
    
class Move(BaseHandler):
    def post(self):
        player = get_player()
        try:
            target_exit = int(self.request.get('exit'))
            exits = player.location.exits
            if target_exit >= len(exits):
                self.error(400)
        except:
            self.error(400)
        player.location = exits[target_exit]
        player.put()
    post = require_player(post)

class CreatePlayer(BaseHandler):
    def post(self):
        player = Player()
        player.user = users.get_current_user()
        player.is_alive = True
        player.location = World.start
        player.put()
    post = require_user(post)
    
class CharacterGeneration(BaseHandler):
    def get(self):
        self.render_template('static/html/character_generation.html')
    get = require_user(get)
