#
# Map
#

from google.appengine.ext import db 

from room import *

final_depth = 5

class Map(db.Model):
    """Currently just references the first room."""
    depth = db.IntegerProperty()
    start = db.ReferenceProperty(Room)

def create_map(depth):
    m = Map(key=db.Key.from_path('Map', depth))
    m.depth = depth
    m.start = create_room(m)
    m.put()
    return m

def get_map(depth):
    m = Map.gql("WHERE depth = :1", depth).get()
    if m is None:
        return create_map(depth)
    return m

def generate_map_layout():
    def empty_room():
        return [None, None, None, None, None]
    layout = empty_room()

    # TODO: generate a random graph
    
    return layout
