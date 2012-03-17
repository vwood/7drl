from google.appengine.api import users
from google.appengine.ext import db

from base import *

class Score(db.Model):
    """Models a highscore."""
    name = db.StringProperty()
    user = db.UserProperty()
    image = db.IntegerProperty()
    score = db.IntegerProperty()
    won = db.BooleanProperty()

class Win(base.BaseHandler):
    def get(self):
        # Check player really has won, calc score + add to highscore + delete player object
        pass

def calculate_score(player, winning):
    score = player.score
    score += player.health / 10
    score *= player.level
    if winning:
        score += 10
        score *= 2
    return score

def add_score(player, winning = False):
    score_value = calculate_score(player, winning)
    if score_value <= 0:
        return
    top_scores = Score.all().order('-score').fetch(10)
    if score > top_scores[-1].score:
        score = Score()
        score.name = player.name
        score.user = player.user
        score.image = player.image
        score.score = score_value
        score.won = winning
        score.put()
