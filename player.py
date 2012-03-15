from google.appengine.api import users
from google.appengine.ext import db

import base
import map
import room
import images

# TODO: perhaps user should be the parent

class Player(db.Model):
    """Models a wonderful player of our humble game."""
    name = db.StringProperty()
    user = db.UserProperty()
    image = db.IntegerProperty()
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
    # TODO: limit to one a turn
    # GET to workaround browser limitations and avoid further javascript
    def get(self):
        player = get_player()
        try:
            # Ensure this operation is idempotent
            if player.location != self.request.get('current'):
                self.redirect('/room')
            target_exit = int(self.request.get('exit'))
            exits = player.location.exits
            if target_exit >= len(exits) or exits[target_exit] is None:
                self.error(400)
        except:
            self.error(400)
        player.location = exits[target_exit]
        player.put()
    post = base.require_player(post)

class CreatePlayer(base.BaseHandler):
    def post(self):
        user = users.get_current_user()
        # This check is being ignored, why?
        if Player.gql("WHERE user = :1", user).get() is not None:
            self.redirect('/room')
        player = Player()
        player.user = users.get_current_user()
        player.is_alive = True
        player.location = map.get_map(1).start
        player.image = images.player[int(self.request.get('class'))]
        player.name = self.request.get('name')
        player.put()
        self.redirect('/room')
    post = base.require_login(post)
    
class CharacterGeneration(base.BaseHandler):
    def get(self):
        self.render_template('static/html/character_generation.html')
    get = base.require_login(get)
