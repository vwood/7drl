import os
from google.appengine.api import users 
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class BaseHandler(webapp.RequestHandler):
    path = template_path('static/html/error.html')
    notfound_path = template_path('static/html/error.html')
    def render_template(self, values={}):
        self.response.out.write(template.render(path, values))
    def render_notfound_template(self, values={}):
        self.response.out.write(template.render(notfound_path, values))

def template_path(path):
    return os.path.join(os.path.dirname(__file__), path)

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
