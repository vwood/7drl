#
# Update
#

from player import *
from monster import *

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
