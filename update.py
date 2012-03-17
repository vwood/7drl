#
# Update
#

import player
import monster

def update():
    monsters = monster.Monster.gql("WHERE is_alive = TRUE").run()
    for m in monsters:
        monster.move(m)

    # Kill idle players > 10 minutes
    players = player.Player.gql("WHERE has_moved = FALSE AND is_alive = TRUE").run()
    for p in players:
        p.idle_out = p.idle_out + 1
        p.health = p.health + 1
        if p.idle_out > 10 * 2:
            p.is_alive = False
        p.messages.append("")
        if len(p.messages) > 5:
            p.messages = p.messages[-5:]
        p.put()

    players = player.Player.gql("WHERE has_moved = TRUE AND is_alive = TRUE").run()
    for p in players:
        p.has_moved = False
        p.messages.append("")
        if len(p.messages) > 5:
            p.messages = p.messages[-5:]
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

if __name__ == '__main__':
    update()
