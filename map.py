#
# Map
#

from random import randint

from google.appengine.ext import db 

import room
import update2

final_depth = 5

class Map(db.Model):
    """Currently just references the first room."""
    depth = db.IntegerProperty()
    start = db.ReferenceProperty(room.Room)

def create_map(depth):
    m = Map(key=db.Key.from_path('Map', depth))
    m.depth = depth
    m.start = generate_map_layout(m)
    m.put()
    update2.update2()
    return m

def get_map(depth):
    m = Map.gql("WHERE depth = :1", depth).get()
    if m is None:
        return create_map(depth)
    return m

def generate_map_layout(map):
    all_rooms = []
    def empty_room():
        "An empty room structure."
        this_room = [room.create_room(map), None, None, None, None]
        all_rooms.append(this_room)
        return this_room
    def free_exit_count(a_room):
        "Return the number of free exits we have."
        return a_room.count(None)
    def pick_exit(this_room, free=True):
        "Find a free (if free=True) or a filled (if free=False) exit in a room."
        pick = randint(1,4)
        while (this_room[pick] != None) == free:
            pick += 1
            pick = ((pick - 1) % 4) + 1
        return pick
    def random_room():
        "Selects a random room."
        pick = randint(0, len(all_rooms) - 1)
        return all_rooms[pick]
    def link_rooms(room_a, room_b):
        "Joins two rooms with exits."
        if free_exit_count(room_a) == 0 or free_exit_count(room_b) == 0:
            return False
        pick_a = pick_exit(room_a)
        pick_b = pick_exit(room_b)
        room_a[pick_a] = room_b
        room_b[pick_b] = room_a
        return True
    
    layout = empty_room()

    cursor = layout
    for _ in range(randint(4,6)):
        new_room = empty_room()
        link_rooms(cursor, new_room)
        cursor = new_room
    end_room = cursor

    def add_loop():
        loop_start_join = random_room()
        loop_end_join = random_room()
        loop_start = empty_room()
        cursor = loop_start
        for _ in range(randint(2,3)):
            new_room = empty_room()
            link_rooms(cursor, new_room)
            cursor = new_room
        loop_end = cursor
        link_rooms(loop_start_join, loop_start)
        link_rooms(loop_end_join, loop_end)

    add_loop()
    if randint(0,1) == 0:
        add_loop()

    # Actually encode exits onto room objects
    for a_room in all_rooms:
        for i, room_exit in enumerate(a_room[1:]):
            if room_exit:
                a_room[0].exits[i] = len(a_room[0].exit_keys)
                a_room[0].exit_keys.append(room_exit[0].key())

        # Add stairs
        if a_room is end_room:
            a_room[0].exits[4] = len(a_room[0].exit_keys)
            # Don't encode a thingy here - we deal with stairs specially in Move()
        a_room[0].put()

    return layout[0]
