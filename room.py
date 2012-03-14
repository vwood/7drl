#
# Room Module
#

import urllib
from random import randint

from random import shuffle

from google.appengine.ext import db 

from base import *
from tiles import *

class Room(db.Model):
    """Models a location (location ~= page)."""
    name = db.StringProperty()
    title = db.StringProperty()
    tiles = db.StringProperty()
    freespace = db.ListProperty(str)
    exits = db.ListProperty(db.Key)

def room_key(room_name=None):
    """Builds a datastore key for a Room entity with board_name."""
    return db.Key.from_path('Room', room_name or 'default_room')

class GetRoom(BaseHandler):
    def get(self):
        room_name = self.request.get('name')
        room = Room.gql("WHERE name = :1", room_name).get()

        if room is None:
            self.render_template('static/html/room_notfound.html')
        else:
            values = {'room': room, 'tiles': tile_string_to_arrays(room.tiles)}
            self.render_template('static/html/room.html', values)
    get = require_player(get)

class RoomEditor(BaseHandler):
    def get(self):
        all_room_keys = Room.all(keys_only=True).run()
        self.render_template('static/html/room_editor.html', {'room_keys' : all_room_keys})
    get = require_admin(get)

class RandomRoom(BaseHandler):
    def get(self):
        tiles = generate_room()
        title = generate_title()
        free_space = free_space_list(tiles)
        shuffle(free_space)
        items = [15, 16]
        exits = [[None,"/random"][randint(0,1)] for _ in range(5)]
        self.render_template('static/html/simple_room.html',
                             {'tiles' : tiles, 
                              'title' : title,
                              'free_space': free_space,
                              'items': items,
                              'exits': exits})
    get = require_admin(get)

def create_room(map, title=None):
    "Create an actual room object for a map."
    if title is None:
        title = generate_title()
    name = title.replace(" ", "_")
    room = Room(parent = map, key_name = name)
    room.name = name
    room.tiles = tile_arrays_to_string(generate_room())
    room.exits = []
    room.put()
    return room
    
def generate_title():
    "Generate the title of the room."
    return "Default Room"

def generate_room():
    "Generate the room layout."
    width, height = 7, 5

    floor = floors[randint(0, len(floors)-1)]
    wall = walls[randint(0, len(walls)-1)]

    result = [[floor for _ in range(height)] for _ in range(width)]

    for x in range(width):
        result[x][0] = wall
        result[x][height - 1] = wall

    for y in range(height):
        result[0][y] = wall
        result[width - 1][y] = wall

    for coords in [(x,y) for x in [1,2,4,5] for y in [1,3]]:
        if randint(0, 4) == 0:
            result[x][y] = wall

    return result

def link_rooms(room_a, room_b):
    "Join two rooms with exits."
    # Don't forget to change tiles so people don't sit on the stairs!
    pass

def tile_string_to_arrays(tile_string):
    return [[int(i) for i in row.split(",")]
            for row in tile_string.split("|")]

def tile_arrays_to_string(tile_arrays):
    return "|".join([",".join([str(i) for i in row])
                    for row in tile_arrays])

def free_space_list(tile_arrays):
    "Returns a list of free spaces in javascript encoded form (x_y)."
    free_list = []
    for i, row in enumerate(tile_arrays):
        for j, cell in enumerate(row):
            if not blocked[cell]:
                free_list.append("%s_%s" %  (i,j))
    return free_list

def get_creatures(room):
    return room.monster_set.get()
