from google.appengine.dist import use_library
use_library('django', '1.2')

import urllib
import wsgiref.handlers

from base import *
from google.appengine.ext import db 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Map(db.Model):
    """Currently just references the first room."""
    start = db.ReferenceProperty(Room)

class Play(BaseHandler):
    path = template_path('static/html/play.html')
    def get(self):
        render_template()
    get = require_login(get)

class Index(BaseHandler):
    path = template_path('static/html/index.html')
    def get(self):
        rooms = db.GqlQuery("SELECT * FROM Room").fetch(10)
        values = {'rooms': rooms}
        template_render(values))

application = webapp.WSGIApplication(
    [('/', Index),
     ('/index', Index),
     ('/play', Play),
     ('/create_room', CreateRoom),
     ('/create_player', CreatePlayer),
     ('/character_generation', CharacterGeneration),
     ('/room_editor', RoomEditor),
     ('/debug', Debug),
     ('/room', GetRoom)],
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
