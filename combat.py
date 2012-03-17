from random import randint

restv = (6, 15)
hurtv = (8, 30)
atirev = (6, 10)
dtirev = (3, 10)

def new():
    return (20,100)

def rest(i):
    a, d = i
    a += restv[0]
    d += restv[1]
    if a > 10: a = 0
    if d > 100: d = 100
    return (a, d)

def hit(a, d):
    aa, _ = a
    _, dd = d
    roll = randint(0, 100)
    roll += aa
    roll -= dd
    return roll > 0

def hurt(i):
    a, d = i
    a -= hurtv[0]
    d -= hurtv[1] 
    return (a, d)

def atire(i):
    a, d = i
    a -= atirev[0]
    d -= atirev[1]
    return (a, d)

def dtire(i):
    a, d = i
    a -= dtirev[0]
    d -= dtirev[1]
    return (a, d)

# spells should be self tire + autohit?
# different kinds of damage:
#   Pure curse (harder for enemy to hit)
#   Pure Damage

def round(lst, aa=True, ba=True):
    ahit, bhit = False, False
    if aa and hit(lst[0], lst[1]):
        ahit = True
    if ba and hit(lst[1], lst[0]):
        bhit = True
    if aa:
        lst[0] = atire(lst[0])
        lst[1] = dtire(lst[1])
    if ba:
        lst[1] = atire(lst[1])
        lst[0] = dtire(lst[0])
    if ahit:
        lst[1] = hurt(lst[1])
    else:
        lst[0] = rest(lst[0])   
    if bhit:
        lst[0] = hurt(lst[0])
    else:
        lst[1] = rest(lst[1])   
    if lst[0][1] <= 0:
        print "A is dead"
    if lst[1][1] <= 0:
        print "B is dead"
    if lst[0][1] <= 0 or lst[1][1] <= 0:
        return False
    return True

if __name__ == '__main__':
    c = [new(), new()]
    count = 0
    while round(c):
        count += 1
    print "in %d rounds" % count


import player
import monster

def attack(source, target):
    a = source.attack 
    d = target.attack 
    if randint(0, 50) + a - d > 25:
        target.health -= min(a - d / 2, 4)
        source.health -= min(d - a, 2)
        source.put()
        target.put()

