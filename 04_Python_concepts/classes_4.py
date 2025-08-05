import random


class Enemy:
    def __init__(self, atkl, atkh, hp=200):
        self.atkl = atkl
        self.atkh = atkh
        self.hp = hp

    def get_hp(self):
        return self.hp

    def get_atk(self):
        atk = random.randrange(self.atkl, self.atkh)
        return atk

    def __str__(self):
        return f'ATK: {self.atkl}-{self.atkh}, HP: {self.hp}'


'''
enemy1 = Enemy(60, 80)
print(f'Enemy 1: {enemy1}')
print(f'Enemy ATK {enemy1.get_atk()}')
print(f'Enemy HP {enemy1.get_hp()}')

enemy2 = Enemy(120, 160, 400)
print(f'Enemy 2: {enemy2}')
print(f'Enemy ATK {enemy2.get_atk()}')
print(f'Enemy HP {enemy2.get_hp()}')

enemy3 = Enemy(20, 60)
print(f'Enemy 3: {enemy3}')
print(f'Enemy ATK {enemy3.get_atk()}')
print(f'Enemy HP {enemy3.get_hp()}')

enemy4 = Enemy(200, 250, 1000)
print(f'Enemy 4: {enemy4}')
print(f'Enemy ATK {enemy4.get_atk()}')
print(f'Enemy HP {enemy4.get_hp()}')

print()
'''
enemies = []

enemy1 = Enemy(60, 80)
enemy2 = Enemy(120, 200, 400)
enemy3 = Enemy(40, 60, 100)
enemy4 = Enemy(200, 250, 300)
enemy5 = Enemy(400, 600, 1000)

enemies.append(enemy1)
enemies.append(enemy2)
enemies.append(enemy3)
enemies.append(enemy4)
enemies.append(enemy5)

for i, enemy in enumerate(enemies):
    print(f'Enemy {i + 1}: {enemy}')
    print(f'Enemy {i + 1}: \n\tATK {enemy.get_atk()} \n\tHP {enemy.get_hp()}\n')

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
