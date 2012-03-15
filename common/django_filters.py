from google.appengine.ext import webapp
register = webapp.template.create_template_register()

def divide(value, arg):
    return int(value) / int(arg)

register.filter(divide)

def mod(value, arg):
    return int(value) % int(arg)

register.filter(mod)
