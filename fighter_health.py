import random, time 

# Define a class for a fighter in the battle
class Fighter:
    def __init__(self, name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health  # Health is private and can't be changed directly
        self.weapon = weapon             # Weapon strength affects attack power
        self.shield = shield             # Shield helps reduce incoming damage

    # Print out the fighter's current health
    def report(self):
        print(self.name + ': Health: ' + str(self.__health))

    # Check if the fighter has been defeated
    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    # Generate a random attack strength based on weapon
    def random_attack(self):
        attack_power = random.randint(self.weapon // 2, self.weapon * 2)
        print('Attack power:', attack_power)
        return attack_power

    # Defend against an incoming attack, reducing health if damage gets through
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')  # Shield fully absorbed the attack

# Create the player and enemy (troll) fighters with their stats
you = Fighter('You', 100, 60, 20)
troll = Fighter('Troll', 200, 30, 10)

# Display initial health for both fighters
you.report()
troll.report()

# Main game loop – continues until one fighter is defeated
while True:
    print('You attack the troll')
    troll.defend(you.random_attack())  # Player attacks troll
    troll.report()
    time.sleep(2)
    print('')

    # Check if troll has been defeated
    if troll.is_dead():
        print('You win')
        break

    # Troll's turn to attack
    print('The troll attacks you . . . ')
    you.defend(troll.random_attack())
    you.report()
    time.sleep(2)

    # Check if player has been defeated
    if you.is_dead():
        print('The troll wins')
        break
    print('')
