from google.appengine.api import users
from google.appengine.ext import db

import base
import player

class Score(db.Model):
    """Models a highscore."""
    name = db.StringProperty()
    user = db.UserProperty()
    image = db.IntegerProperty()
    score = db.IntegerProperty()
    won = db.BooleanProperty()

class Win(base.BaseHandler):
    def get(self):
        p = player.get_player()
        if not p.has_won:
            self.redirect('/room?error=You did not win.')
            return
        add_score(p, winning=True)
        self.render_template('static/html/win.html', {'player':p})

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

def render_top_scores():
    top_scores = Score.all().order('-score').fetch(10)
    if len(top_scores) == 0:
        top_scores = ["<h2>No one :(</h2>"]
    else:
        top_scores = ["%s %s as %s <img src=\"replace_%d\" class=\"imgalign\"/> : %s" 
                      % (score.user.nickname(),
                         "won" if score.won else "lost",
                         score.name,
                         score.image,
                         score.score)
                      for score in top_scores]
    return "<div>%s</div>" % "</div> <div>".join(top_scores)
