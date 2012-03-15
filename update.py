#
# Update
#

from player import *
from monster import *

monsters = Monster.gql("WHERE is_alive = TRUE").run()
for monster in monsters:
    move(monster)

players = Player.gql("WHERE has_moved = TRUE AND is_alive = TRUE").run()
for player in players:
    player.has_moved = False
    player.put()

# Bring out your dead!
dead = Player.gql("WHERE is_alive = FALSE").run()
for dodo in dead:
    try:
        dodo.delete()
    except NotSavedError:
        # Guess it was just a ghost
        pass

dead = Monster.gql("WHERE is_alive = FALSE").run()
for dodo in dead:
    try:
        dodo.delete()
    except NotSavedError:
        # Guess it was just a ghost
        pass
