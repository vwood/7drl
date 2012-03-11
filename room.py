#
# Room Module
#

from base import *
import urllib
from google.appengine.ext import db 

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

# TODO: Decorator for this...
class GetRoom(BaseHandler):
    path = template_path('static/html/room.html')
    notfound_path = template_path('static/html/room_notfound.html')
    def get(self):
        room_name = self.request.get('name')
        room = Room.gql("WHERE link = :1", room_name).get()

        if room is None:
            render_notfound_template()
        else:
            values = {'room': room, 'user': user}
            render_template(values)
    get = require_login(get)

class RoomEditor(BaseHandler):
    path = template_path('static/html/room_editor.html')
    def get(self):
        render_template()
    get = require_admin(get)
