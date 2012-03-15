from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext import webapp
register = webapp.template.create_template_register()

def divide(value, arg):
    return int(value) / int(arg)

register.filter('divide', divide)

def mod(value, arg):
    return int(value) % int(arg)

register.filter('mod', mod)
