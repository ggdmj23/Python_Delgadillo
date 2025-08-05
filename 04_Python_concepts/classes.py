import random


class Enemy:
    atkl = 60
    atkh = 80

    def getAtk(self):
        return random.randrange(self.atkl, self.atkh)


enemy1 = Enemy()
print(enemy1.getAtk())

enemy2 = Enemy()
print(enemy2.getAtk())

enemy3 = Enemy()
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
