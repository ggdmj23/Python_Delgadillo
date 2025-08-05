import random


class Enemy:
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        return random.randrange(self.atkl, self.atkh)


enemy1 = Enemy(60, 80)
print(enemy1.getAtk())

enemy2 = Enemy(120, 160)
print(enemy2.getAtk())

enemy3 = Enemy(20, 60)
print(enemy3.getAtk())

'''
playerhp = 260
enemyatkl = 60
enemyatkh = 80
lowhp = 30

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= lowhp:
        playerhp = lowhp

    print("Enemy strikes for", dmg, "points of damage. Current hp:", playerhp)

    if playerhp > lowhp:
        continue

    print("You have low health. You've been teleported to the nearest inn.")
    break
'''
