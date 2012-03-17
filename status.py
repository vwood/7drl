from google.appengine.api import memcache 

import player

player_count = memcache.get("player_count")
if player_count is None:
    player_count = player.Player.all().count()
    memcache.set("player_count", player_count, 120)

print player_count
