#
# Map
#

from google.appengine.ext import db 

from room import *

class Map(db.Model):
    """Currently just references the first room."""
    start = db.ReferenceProperty(Room)

