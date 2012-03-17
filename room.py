#
# Room Module
#

from random import randint, shuffle

from google.appengine.ext import db 

import images
import base

class Room(db.Model):
    """Models a location (location ~= page)."""
    title = db.StringProperty()
    tiles = db.ListProperty(int)
    width = db.IntegerProperty()
    free_space = db.ListProperty(int)
    messages = db.ListProperty(str)
    exits = db.ListProperty(int)
    exit_keys = db.ListProperty(db.Key)


# Python can't do these circular imports - what a stupid language
import player
import monster

def room_key(room_name=None):
    """Builds a datastore key for a Room entity with board_name."""
    return db.Key.from_path('Room', room_name or 'default_room')

class GetRoom(base.BaseHandler):
    def get(self):
        user = player.get_player()
        room = user.location

        players = player.Player.gql("WHERE location = :1", room).run()
        monsters = monster.Monster.gql("WHERE location = :1", room).run()
        items = list(players) + list(monsters)

        if room is None:
            self.render_template('static/html/room_notfound.html')
        else:
            values = {'player': user,
                      'room': room,
                      'items': items,
                      'error': self.request.get('error')}
            self.render_template('static/html/room.html', values)
    get = base.require_player(get)

class RoomEditor(base.BaseHandler):
    def get(self):
        all_room_keys = Room.all(keys_only=True).run()
        self.render_template('static/html/room_editor.html', {'room_keys' : all_room_keys})
    get = base.require_admin(get)

class RandomRoom(base.BaseHandler):
    def get(self):
        width, tiles = generate_room()
        title = generate_title()
        free_space = free_space_list(tiles)
        shuffle(free_space)
        items = [15, 16]
        exits = [[None,"/random"][randint(0,1)] for _ in range(5)]
        self.render_template('static/html/simple_room.html',
                             {'width': width,
                              'tiles' : tiles, 
                              'title' : title,
                              'free_space': free_space,
                              'items': items,
                              'exits': exits})
    get = base.require_admin(get)

def create_room(map, title=None):
    """Create an actual room object for a map.
    DOES NOT PUT ONTO DATASTORE."""
    room = Room(parent = map, key_name = None)
    room.title, room.width, room.tiles = generate_room()
    if title is not None:
        room.title = title
    room.free_space = free_space_list(room.tiles)
    room.exits = [-1, -1, -1, -1, -1]
    room.exit_keys = []
    room.put()
    return room

def generate_title(floor, wall):
    floor_names = images.floor_names[floor]
    wall_names = images.wall_names[wall]
    floor_name = floor_names[randint(0, len(floor_names)-1)]
    wall_name = wall_names[randint(0, len(wall_names)-1)]
    return wall_name + floor_name

def generate_room():
    "Generate the room layout."
    width, height = 7, 5

    floor = randint(0, len(images.floors)-1)
    wall = randint(0, len(images.walls)-1)
    title = generate_title(floor, wall)
    floor = images.floors[floor]
    wall = images.walls[wall]

    result = [[floor for _ in range(width)] for _ in range(height)]

    # Add walls
    for x in range(width):
        result[0][x] = wall
        result[height - 1][x] = wall

    for y in range(height):
        result[y][0] = wall
        result[y][width - 1] = wall

    for x,y in [(x,y) for x in [1,2,4,5] for y in [1,3]]:
        if randint(0, 4) == 0:
            result[y][x] = wall

    # Sometimes, add a splash of a different kind of floor + wall
    if randint(0,1) == 0:
        second_floor = images.floors[randint(0, len(images.floors)-1)]
        second_wall = images.walls[randint(0, len(images.walls)-1)]
        cx, cy = randint(0, width - 1), randint(0, height - 1)
        for x,y in [(x,y)
                    for x in range(max(cx-2,0), min(cx+3,width))
                    for y in range(max(cy-2,0), min(cy+3,height))]:
            if randint(0,3) != 0:
                if result[y][x] == floor:
                    result[y][x] = second_floor
                else:
                    result[y][x] = second_wall

    # Flatten tile array
    result = [cell for row in result for cell in row]

    return (title, width, result)

def link_rooms(room_a, room_b):
    "Join two rooms with exits."
    # Don't forget to change tiles so people don't sit on the stairs!
    pass

def free_space_list(tiles):
    "Returns a list of free spaces in javascript encoded form (x_y)."
    free_list = []
    for i, cell in enumerate(tiles):
        if not images.blocked[cell]:
            free_list.append(i)
    shuffle(free_list)
    return free_list

def get_creatures(room):
    return room.monster_set.get()
