"""
enemy_module.py

Description:
    This module defines the Enemy class used for game simulations.
    Each enemy has a name, health points (HP), and an attack range.
    Provides methods for getting stats, attacking, and taking damage.

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

import random  # Importing the random module to generate random attack values


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
        Reduces the enemy's HP by the specified damage value,
        ensuring HP does not go below zero.

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
