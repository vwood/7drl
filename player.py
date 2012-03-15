import urllib

from google.appengine.api import users
from google.appengine.ext import db

import base
import map
import room

# TODO: perhaps user should be the parent

class Player(db.Model):
    """Models a wonderful player of our humble game."""
    name = db.StringProperty()
    user = db.UserProperty()
    location = db.ReferenceProperty(room.Room)
    health = db.IntegerProperty()
    score = db.IntegerProperty()
    is_alive = db.BooleanProperty()
    
def get_player(user = None):
    "Gets the player model of a current user."
    if not user:
        user = users.get_current_user()
    return Player.gql("WHERE user = :1", user).get()
    
class Move(base.BaseHandler):
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
    post = base.require_player(post)

class CreatePlayer(base.BaseHandler):
    def post(self):
        player = Player()
        player.user = users.get_current_user()
        player.is_alive = True
        player.location = map.get_map(1).start
        player.put()
        self.redirect('/room?' + urllib.urlencode({'name': player.location.name}))
    post = base.require_login(post)
    
class CharacterGeneration(base.BaseHandler):
    def get(self):
        self.render_template('static/html/character_generation.html')
    get = base.require_login(get)
