#
# Update
#

import player
import monster

monsters = monster.Monster.gql("WHERE is_alive = TRUE").run()
for m in monsters:
    move(m)

players = player.Player.gql("WHERE has_moved = TRUE AND is_alive = TRUE").run()
for p in players:
    p.has_moved = False
    p.put()

# Bring out your dead!
dead = player.Player.gql("WHERE is_alive = FALSE").run()
for dodo in dead:
    try:
        dodo.delete()
    except NotSavedError:
        # Guess it was just a ghost
        pass

dead = monster.Monster.gql("WHERE is_alive = FALSE").run()
for dodo in dead:
    try:
        dodo.delete()
    except NotSavedError:
        # Guess it was just a ghost
        pass
