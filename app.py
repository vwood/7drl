#
# Main
#

import urllib
import wsgiref.handlers

from google.appengine.api import memcache 
from google.appengine.ext import db 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import base
import room
import player
import map
import debug
import score

class Play(base.BaseHandler):
    def get(self):
        self.render_template('static/html/play.html')
    get = base.require_login(get)

class Index(base.BaseHandler):
    def get(self):
        top_scores = memcache.get("top_scores")
        if top_scores is None:
            memcache.set("top_scores", score.render_top_scores(), 10)
        values = {'top_scores': top_scores}
        self.render_template('static/html/index.html', values)

application = webapp.WSGIApplication(
    [('/', Index),
     ('/index', Index),
     ('/play', Play),
     ('/create_player', player.CreatePlayer),
     ('/move', player.Move),
     ('/attack', player.Attack),
     ('/character_generation', player.CharacterGeneration),
     ('/room_editor', room.RoomEditor),
     ('/debug', debug.Debug),
     ('/random', room.RandomRoom),
     ('/room', room.GetRoom)],
    debug=True)

webapp.template.register_template_library("common.django_filters")

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
