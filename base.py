import os
from google.appengine.api import users 
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class BaseHandler(webapp.RequestHandler):
    def render_template(self, path = 'static/html/error.html', values={}):
        path = os.path.join(os.path.dirname(__file__), path)
        self.response.out.write(template.render(path, values))

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
        elif get_player(user) is None:
            self.redirect("/create_player")
        else:
            fn(self)
    return decorated_fn

