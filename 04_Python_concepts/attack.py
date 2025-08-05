"""
enemy_module.py

Description:
    This module defines the Enemy and Player classes used for game simulations.
    Each enemy has a name, health points (HP), and an attack range.
    The player can also attack and take damage. A simple battle loop is included.

Author: Gonzalo González
Version: 1.0
Date: 2025-07-28
Python Version: 3.10+

Usage:
    # Create and use an enemy
    enemy = Enemy("Goblin", 50, 80)
    print(enemy.get_atk())
    enemy.take_damage(20)
"""

import random  # Used to generate random attack values for both Enemy and Player


class Enemy:
    """
    Class representing an enemy character with attack range and health.
    """

    def __init__(self, name, atkl, atkh, hp=200):
        """
        Initializes an Enemy instance.

        Parameters:
        - name (str): The name of the enemy.
        - atkl (int): The minimum attack power.
        - atkh (int): The maximum attack power (exclusive in randrange).
        - hp (int, optional): The initial health points. Defaults to 200.
        """
        self.name = name
        self.atkl = atkl
        self.atkh = atkh
        self.hp = hp

    def get_hp(self):
        """
        Returns the current health points of the enemy.

        Returns:
        - int: Current HP
        """
        return self.hp

    def get_atk(self):
        """
        Generates and returns a random attack value within the enemy's attack range.

        Returns:
        - int: Random attack value
        """
        atk = random.randrange(self.atkl, self.atkh)
        return atk

    def take_damage(self, damage):
        """
        Reduces the enemy's HP by the specified damage value.
        Ensures that HP does not go below zero.

        Parameters:
        - damage (int): Amount of damage taken

        Returns:
        - int: Updated HP
        """
        self.hp = max(self.hp - damage, 0)
        return self.hp

    def __str__(self):
        """
        Returns a readable string representation of the enemy's stats.

        Returns:
        - str: Formatted enemy stats
        """
        return f'{self.name} → ATK: {self.atkl}-{self.atkh}, HP: {self.hp}'


'''
# Uncomment this block to test multiple enemy creation and stats display

# Create a list to store multiple enemy instances
enemies = []

# Instantiate several enemies with different attributes
enemy1 = Enemy("Goblin", 60, 80)
enemy2 = Enemy("Orc Brute", 120, 200, 400)
enemy3 = Enemy("Shadow Imp", 40, 60, 100)
enemy4 = Enemy("Doom Knight", 200, 250, 300)
enemy5 = Enemy("Elder Dragon", 400, 600, 1000)

# Add enemies to the list
enemies.append(enemy1)
enemies.append(enemy2)
enemies.append(enemy3)
enemies.append(enemy4)
enemies.append(enemy5)

# Display stats and a sample attack value for each enemy
for i, enemy in enumerate(enemies):
    print(f'Enemy {i + 1}: {enemy}')  # Uses __str__ to show basic info
    print(f'Enemy {i + 1}: \n\tATK {enemy.get_atk()} \n\tHP {enemy.get_hp()}\n')
'''


class Player:
    """
    Class representing the player character.
    The player can attack and take damage.
    """

    def __init__(self, hp=200):
        """
        Initializes the player with a given amount of HP.

        Parameters:
        - hp (int): Initial health points. Default is 400.
        """
        self.hp = hp

    def attack(self):
        """
        Generates a random attack value for the player.

        Returns:
        - int: Random attack value between 100 and 200
        """
        return random.randint(100, 200)

    def take_damage(self, damage):
        """
        Reduces the player's HP by the specified damage value.
        Ensures that HP does not go below zero.

        Parameters:
        - damage (int): Amount of damage taken

        Returns:
        - int: Updated HP
        """
        self.hp = max(self.hp - damage, 0)
        return self.hp


# --- Battle Simulation ---

# Create a single enemy for the simulation
enemy = Enemy("Warlord", 200, 250, 300)

# Create the player
player = Player(400)

# Initialize the round counter
round_number = 1

# Display battle start message
print(f"⚔️  Battle Begins: Player vs {enemy.name}\n")

# Begin the battle loop
while player.hp > 0 and enemy.hp > 0:
    print(f"🔁 Round {round_number}")

    # --- Player's Turn ---
    player_dmg = player.attack()  # Generate player's attack
    enemy.take_damage(player_dmg)  # Apply damage to enemy
    print(f"Player hits {enemy.name} for {player_dmg} damage! Enemy HP: {enemy.hp}")

    # Check if enemy is defeated
    if enemy.hp <= 0:
        print(f"🏆 {enemy.name} defeated!")
        break

    # --- Enemy's Turn ---
    enemy_dmg = enemy.get_atk()  # Generate enemy's attack
    player.take_damage(enemy_dmg)  # Apply damage to player
    print(f"{enemy.name} strikes back for {enemy_dmg} damage! Player HP: {player.hp}\n")

    # Check if player is defeated
    if player.hp <= 0:
        print("💀 You have been defeated...")
        break

    # Move to next round
    round_number += 1
