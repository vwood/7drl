import os

from google.appengine.api import users 
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class BaseHandler(webapp.RequestHandler):
    def render_template(self, path = 'static/html/error.html', values={}):
        path = os.path.join(os.path.dirname(__file__), path)
        values['login'] = self.get_login()
        self.response.out.write(template.render(path, values))

    def get_login(self):
        user = users.get_current_user()
        if user is None:
            return "<a href=\"%s\">login</a>" % users.create_login_url(self.request.url)
        else:
            return "G'day, <strong>%s</strong> <a href=\"%s\">logout</a>" % (user.nickname(),
                                                                             users.create_logout_url("/"))

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

def require_player(fn):
    """'Decorate' (because of python 2.5) a method to require a playing user.
    This means the user has an associated player object."""
    def decorated_fn(self):
        user = users.get_current_user()
        if user is None:
            self.redirect(users.create_login_url(self.request.url))
        elif player.get_player(user) is None:
            self.redirect("/character_generation")
        else:
            fn(self)
    return decorated_fn

import player
