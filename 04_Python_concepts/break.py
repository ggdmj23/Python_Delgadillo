import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 0:
        playerhp = 0
        # break

    print("Enemy strikes for", dmg, "points of damage. Current hp:", playerhp)

    if playerhp == 0:
        print("You have died. You cannot respawn, as you are dead.")
