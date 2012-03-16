from google.appengine.api import users
from google.appengine.ext import db

import base
import map
import room
import images

class Player(db.Model):
    """Models a wonderful player of our humble game."""
    name = db.StringProperty()
    user = db.UserProperty()
    image = db.IntegerProperty()
    location = db.ReferenceProperty(room.Room)
    health = db.IntegerProperty()
    score = db.IntegerProperty()
    is_alive = db.BooleanProperty()
    has_moved = db.BooleanProperty()
    
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
            if player.has_moved:
                self.redirect('/room')
            target_exit = int(self.request.get('exit'))
            exits = player.location.exits 
            exit_keys = player.location.exit_keys
            if target_exit >= len(exits) or exits[target_exit] == -1:
                self.redirect('/room?error="Invalid Exit"')
            player.location = room.Room.get(exit_keys[exits[target_exit]])
            player.has_moved = True
            player.put()
            self.redirect('/room')
        except Exception as e:
            print e
            self.error(401)
    get = base.require_player(get)

class Attack(base.BaseHandler):
    # GET to workaround browser limitations and avoid further javascript
    def get(self):
        player = get_player()
        if player.has_moved:
            self.redirect('/room')
        target = self.request.get('target')
        possible_targets = player.location.monster_set.get() 
        if target not in possible_targets:        
            self.error(400)
        # Perform attack (using combat.py)
        # Perhaps the attack should be in the heartbeat update
        # OR - merely check that one move per turn per player
    get = base.require_player(get)

class CreatePlayer(base.BaseHandler):
    def post(self):
        user = users.get_current_user()
        if Player.gql("WHERE user = :1", user).get() is None:
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
