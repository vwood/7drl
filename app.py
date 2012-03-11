from google.appengine.dist import use_library
use_library('django', '1.2')

import os
import cgi
import datetime
import urllib
import wsgiref.handlers

from google.appengine.api import users 
from google.appengine.ext import db 
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class Room(db.Model):
    """Models a location (location ~= page)."""
    name = db.StringProperty()
    title = db.StringProperty()
    image_url = db.StringProperty()
    exits = db.ListProperty(db.Key)

class Map(db.Model):
    """Currently just references the first room."""
    start = db.ReferenceProperty(Room)

class Player(db.Model):
    """Models a wonderful player of our humble game."""
    name = db.StringProperty()
    user = db.UserProperty()
    location = db.ReferenceProperty(Room)

def room_key(room_name=None):
    """Builds a datastore key for a Room entity with board_name."""
    return db.Key.from_path('Room', room_name or 'default_room')

class BaseHandler(webapp.RequestHandler):
    def get_user_or_redirect(self):
        """Ensure a user is logged in."""
        user = users.get_current_user()
        if user is None:
            self.redirect(users.create_login_url(self.request.url))
        else:
            return user

def require_admin(fn):
    "'Decorate' (because of python 2.5) a method to require an admin login"
    def decorated_fn(self):
        if not users.is_current_user_admin():
            self.error(403)
        else:
            fn(self)
    return decorated_fn

def require_login(fn):
    "'Decorate' (because of python 2.5) a method to require a login"
    def decorated_fn(self):
        if users.get_current_user() is None:
            self.redirect(users.create_login_url(self.request.url))
        else:
            fn(self)
    return decorated_fn

### Room ###
class CreateRoom(webapp.RequestHandler):
    def post(self):
        room_name = self.request.get('title').replace(" ", "_")
        room = Room()
        room.title = self.request.get('title')
        room.image_url = self.request.get('image_url')
        room.put()
        self.redirect('/room?' + urllib.urlencode({'name': thread_name}))
    post = require_admin(post)

# TODO: Decorator for this...
class GetRoom(webapp.RequestHandler):
    def get(self):
        room_name = self.request.get('name')
        room = Room.gql("WHERE link = :1", room_name).get()

        if room is None:
            path = os.path.join(os.path.dirname(__file__), 'static/html/room_notfound.html')
            self.response.out.write(template.render(path, {}))
        else:
            values = {'room': room, 'user': user}
            path = os.path.join(os.path.dirname(__file__), 'static/html/room.html')
            self.response.out.write(template.render(path, values))
    get = require_login(get)

class RoomEditor(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'static/html/room_editor.html')
        self.response.out.write(template.render(path, {}))
    get = require_admin(get)

class Debug(webapp.RequestHandler):
    def post(self):
        path = os.path.join(os.path.dirname(__file__), 'static/html/debug.html')
        self.response.out.write(template.render(path, {'debug': self.request}))

class Play(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'static/html/play.html')
        self.response.out.write(template.render(path, {}))
    get = require_login(get)

class Index(webapp.RequestHandler):
    def get(self):
        rooms = db.GqlQuery("SELECT * FROM Room").fetch(10)

        values = {'rooms': rooms}
        path = os.path.join(os.path.dirname(__file__), 'static/html/index.html')
        self.response.out.write(template.render(path, values))

application = webapp.WSGIApplication(
    [('/', Index),
     ('/index', Index),
     ('/play', Play),
     ('/create_room', CreateRoom),
     ('/room_editor', RoomEditor),
     ('/debug', Debug),
     ('/room', GetRoom)],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
