from base import *

class Debug(BaseHandler):
    def post(self):
        self.render_template('static/html/debug.html', {'debug': self.request})
