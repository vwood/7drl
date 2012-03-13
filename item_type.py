from google.appengine.ext import db

from base import *

class ItemType(db.Model):
    """Models some strange artefact of mystery and power."""
    name = db.StringProperty()
