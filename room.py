#
# Room Module
#

import urllib
from random import randint

from google.appengine.ext import db 

from base import *


class Room(db.Model):
    """Models a location (location ~= page)."""
    name = db.StringProperty()
    title = db.StringProperty()
    image_url = db.StringProperty()
    exits = db.ListProperty(db.Key)

def room_key(room_name=None):
    """Builds a datastore key for a Room entity with board_name."""
    return db.Key.from_path('Room', room_name or 'default_room')

class CreateRoom(BaseHandler):
    def post(self):
        room_name = self.request.get('title').replace(" ", "_")
        room = Room()
        room.title = self.request.get('title')
        room.image_url = self.request.get('image_url')
        room.put()
        self.redirect('/room?' + urllib.urlencode({'name': thread_name}))
    post = require_admin(post)

class GetRoom(BaseHandler):
    def get(self):
        room_name = self.request.get('name')
        room = Room.gql("WHERE link = :1", room_name).get()

        if room is None:
            self.render_template('static/html/room_notfound.html')
        else:
            values = {'room': room, 'user': user}
            self.render_template('static/html/room.html', values)
    get = require_login(get)

class RoomEditor(BaseHandler):
    def get(self):
        all_room_keys = Room.all(keys_only=True).run()
        self.render_template('static/html/room_editor.html', {'room_keys' : all_room_keys})
    get = require_admin(get)
