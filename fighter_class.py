import random

class Fighter:
    def __init__(self, name, starting_health, weapon, shield):
        self.name = name  # Fighter's name
        self.__health = starting_health  # Private health attribute
        self.weapon = weapon  # Attack strength
        self.shield = shield  # Defence power

    def report(self):
        print(f"{self.name}: Health: {self.__health}")  # Displays fighter's health

    def random_attack(self):  
        attack_power = random.randint(self.weapon // 2, self.weapon * 2)
        return attack_power

    def take_damage(self, damage):  
        effective_damage = max(damage - self.shield, 0)  # Ensure damage is not negative
        self.__health -= effective_damage  
        print(f"{self.name} takes {effective_damage} damage! Remaining health: {self.__health}")

    def is_alive(self):
        return self.__health > 0  # Check if the fighter is still alive


# Creating fighter objects
you = Fighter('You', 100, 60, 20)
troll = Fighter('Troll', 200, 30, 10)

# Reporting initial health
you.report()
troll.report()

# Fight loop
while you.is_alive() and troll.is_alive():
    print("\nYou attack the troll!")
    troll.take_damage(you.random_attack())

    if not troll.is_alive():
        print("\nTroll has been defeated! You win!")
        break

    print("\nTroll attacks you!")
    you.take_damage(troll.random_attack())

    if not you.is_alive():
        print("\nYou have been defeated! Troll wins!")

# Final health report
you.report()
troll.report()