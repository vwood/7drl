from google.appengine.ext import db

import base
from item_type import *
import player

class Item(db.Model):
    """Models a particular instance of some strange
    artefact of mystery and power."""
    item_type = db.IntegerProperty()
    location = db.ReferenceProperty(None)
    
class Use(base.BaseHandler):
    """Handles the usage of items"""
    def post(self):
        # check player has item
        player = player.get_player()
        item = Item.get(self.request.get_by_key_name('item'))
        if item.location != player:
            self.error(400)
        elif item.item_type == 0:
            # Wand of Digg
            self.redirect("http://digg.com")
            # Book of Faces
            # Tube of You
            # Spellapedia (learn a random spell?)
        else:
            pass
    post = base.require_player(post)

    
def drop(item):
    if item.location.kind() == "Player":
        location = item.location.location
