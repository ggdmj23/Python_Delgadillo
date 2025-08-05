import random


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getHp(self):
        return f'Hp is {self.hp}'

    def getAtk(self):
        atk = random.randrange(self.atkl, self.atkh)
        return f'Atk is {atk}'


enemy1 = Enemy(60, 80)
print(enemy1.getAtk())
print(enemy1.getHp())

enemy2 = Enemy(120, 160)
print(enemy2.getAtk())
print(enemy2.getHp())

enemy3 = Enemy(20, 60)
print(enemy3.getAtk())
print(enemy3.getHp())

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
