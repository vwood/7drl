#
# Room Module
#

import urllib
from random import randint

from google.appengine.ext import db 

from base import *
from tiles import *

class Room(db.Model):
    """Models a location (location ~= page)."""
    name = db.StringProperty()
    title = db.StringProperty()
    tiles = db.StringProperty()
    exits = db.ListProperty(db.Key)

def room_key(room_name=None):
    """Builds a datastore key for a Room entity with board_name."""
    return db.Key.from_path('Room', room_name or 'default_room')

class CreateRoom(BaseHandler):
    def post(self):
        room_name = self.request.get('title').replace(" ", "_")
        room = Room()
        room.title = self.request.get('title')
        room.image_url = self.request.get('image_url')
        room.put()
        self.redirect('/room?' + urllib.urlencode({'name': thread_name}))
    post = require_admin(post)

class GetRoom(BaseHandler):
    def get(self):
        room_name = self.request.get('name')
        room = Room.gql("WHERE link = :1", room_name).get()

        if room is None:
            self.render_template('static/html/room_notfound.html')
        else:
            values = {'room': room, 'user': user}
            self.render_template('static/html/room.html', values)
    get = require_login(get)

class RoomEditor(BaseHandler):
    def get(self):
        all_room_keys = Room.all(keys_only=True).run()
        self.render_template('static/html/room_editor.html', {'room_keys' : all_room_keys})
    get = require_admin(get)

class RandomRoom(BaseHandler):
    def get(self):
        tiles = generate_room()
        self.render_template('static/html/simple_room.html', {'tiles' : tiles})
    get = require_admin(get)
    
def generate_room():
    width, height = 7, 5

    floor = floors[randint(0, len(floor)-1)]
    wall = walls[randint(0, len(floor)-1)]

    result = [[floor for _ in width] for _ in height]

    for x in width:
        result[x][0] = wall
        result[x][height - 1] = wall

    for y in height:
        result[0][y] = wall
        result[width - 1][y] = wall

    if randint(0, 4) == 0:
        result[1][1] = wall
        result[2][1] = wall

    if randint(0, 4) == 0:
        result[4][1] = wall
        result[5][1] = wall

    if randint(0, 4) == 0:
        result[1][3] = wall
        result[2][3] = wall

    if randint(0, 4) == 0:
        result[4][3] = wall
        result[5][3] = wall

    return result

def tile_string_to_arrays(tile_string):
    return [[int(i) for i in row.split(",")]
            for row in tile_string.split("|")]

def tile_arrays_to_string(tile_arrays):
    return "|".join([",".join([str(i) for i in row]))
                    for row in tile_arrays])
