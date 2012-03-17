from google.appengine.api import users
from google.appengine.ext import db

from base import *

class Score(db.Model):
    """Models a highscore."""
    name = db.StringProperty()
    user = db.UserProperty()
    score = db.IntegerProperty()

class Win(base.BaseHandler):
    def get(self):
        # Check player really has won, calc score + add to highscore + delete player object
        pass

def calculate_score(player, winning):
    score = 0
    # levels decended
    # items found
    # perhaps a partial score while playing (gold etc.)
    if winning:
        score += 10
        score *= 2
    return score

def add_score(player, winning = False):
    score_value = calculate_score(player, winning)
    # TODO: check we beat the top ten?
    if score_value <= 0:
        return
    score = Score()
    score.name = player.name
    score.user = player.user
    score.score = score_value
    score.post
