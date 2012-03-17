from google.appengine.api import users
from google.appengine.ext import db

import base
import map
import room
import images
import monster

class Player(db.Model):
    """Models a wonderful player of our humble game."""
    name = db.StringProperty()
    user = db.UserProperty()
    image = db.IntegerProperty()
    location = db.ReferenceProperty(room.Room)
    health = db.IntegerProperty()
    level = db.IntegerProperty()
    score = db.IntegerProperty()
    is_alive = db.BooleanProperty()
    has_moved = db.BooleanProperty()
    has_won = db.BooleanProperty()
    idle_out = db.IntegerProperty()
    
def get_player(user = None):
    "Gets the player model of a current user."
    if not user:
        user = users.get_current_user()
    return Player.gql("WHERE user = :1", user).get()
    
class Move(base.BaseHandler):
    # TODO: limit to one a turn
    # TODO: enemies should occasionally block your move (and attack you)
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
                self.redirect('/room?error=Invalid Exit')
                return
            if target_exit == 4:
                # Go down stairs
                depth = player.location.parent().depth
                player.level = player.level + 1
                if depth == map.final_depth:
                    player.has_won = True
                    player.put()
                    self.redirect('/win')
                    return
                player.health = min(100, player.health + 10)
                player.location = map.get_map(depth + 1).start
            else:
                player.location = room.Room.get(exit_keys[exits[target_exit]])
            player.has_moved = True
            player.put()
            self.redirect('/room')
        except Exception, e:
            self.redirect('/room?error=Python Error:' + str(e))
    get = base.require_player(get)

class Attack(base.BaseHandler):
    # GET to workaround browser limitations and avoid further javascript
    def get(self):
        player = get_player()
        #if player.has_moved:
        #    self.redirect('/room?error=Already Moved')
        target = self.request.get('target')
        try:
            target = monster.Monster.get(target)
        except BadKeyError:
            self.redirect('/room?error=Target Not Found')

        if target is None or target.location.key() != player.location.key():
            self.redirect('/room?error=Target Not Found')
        
        # Perform attack (using combat.py)
        # OR - merely check that one move per turn per player
    get = base.require_player(get)

class CreatePlayer(base.BaseHandler):
    def post(self):
        user = users.get_current_user()
        old_player = Player.gql("WHERE user = :1", user).get()
        if old_player is None or old_player.is_alive == False:
            player = Player()
            player.user = users.get_current_user()
            player.is_alive = True
            player.location = map.get_map(1).start
            player.image = images.player[int(self.request.get('class'))]
            player.name = self.request.get('name')
            player.health = 100
            player.level = 1
            player.score = 0
            player.has_won = False
            player.idle_out = 0
            player.put()
        self.redirect('/room')
    post = base.require_login(post)
    
class CharacterGeneration(base.BaseHandler):
    def get(self):
        self.render_template('static/html/character_generation.html')
    get = base.require_login(get)
