import random

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

    if playerhp == lowhp:
        print("You have low health. You've been teleported to the nearest inn.")
        break
