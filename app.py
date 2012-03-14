#
# Main
#

import urllib
import wsgiref.handlers

from google.appengine.ext import db 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from base import *
from room import *
from player import *
from map import *
from debug import *


class Play(BaseHandler):
    def get(self):
        self.render_template('static/html/play.html')
    get = require_login(get)

class Index(BaseHandler):
    def get(self):
        rooms = db.GqlQuery("SELECT * FROM Room").fetch(10)
        values = {'rooms': rooms}
        self.render_template('static/html/index.html', values)

application = webapp.WSGIApplication(
    [('/', Index),
     ('/index', Index),
     ('/play', Play),
     ('/create_player', CreatePlayer),
     ('/character_generation', CharacterGeneration),
     ('/room_editor', RoomEditor),
     ('/debug', Debug),
     ('/random', RandomRoom),
     ('/room', GetRoom)],
    
    debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
