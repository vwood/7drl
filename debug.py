from base import *

class Debug(BaseHandler):
    path = template_path('static/html/debug.html')
    def post(self):
        self.render_template({'debug': self.request})
