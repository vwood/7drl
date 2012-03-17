from random import randint

import monster
import room
import player

max_monsters = 100

monster_count = monster.Monster.all(keys_only=True).count(max_monsters)

# Create some monsters in the dungeon
if monster_count < max_monsters:
    all_rooms = set()
    for a_room in room.Room.all(keys_only=True):
        all_rooms.add(a_room)

    for a_player in player.Player.all():
        all_rooms.remove(a_player.location.key())

    while len(all_rooms) > 0 and monster_count < max_monsters:
        a_room = all_rooms.pop()
        if monster.Monster.all(keys_only=True).filter('location =', a_room).count() < 2:
            monster.generate_new_monster(a_room)
            monster_count += 1
