import random, time 

# Define the Fighter class to represent a player or enemy in the battle
class Fighter:
    def __init__(self, name, starting_health, weapon, shield):
        # Set up the fighter's basic stats
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

    # Display current health status
    def report(self):
        print(self.name + ' : Health: ' + str(self.health))

    # Generate a random attack power based on the weapon strength
    def random_attack(self):
        attack_power = random.randint(self.weapon // 2, self.weapon * 2)
        print('Attack power:', attack_power)
        return attack_power

    # Handle defence against an incoming attack
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            self.health -= damage  # Take damage if it exceeds the shield
            print('Damage:', damage)
        else:
            print('No damage')  # Shield fully absorbs the attack

# Create the player and the enemy (troll) with stats
you = Fighter('You', 100, 60, 20)
troll = Fighter('Troll', 200, 30, 10)

# Report initial health
you.report()
troll.report()

# Main battle loop
while True: 
    print('You attack the troll')
    troll.defend(you.random_attack())  # Player attacks troll
    troll.report()
    time.sleep(1)
    print('')
    if troll.health <= 0:
        print('You win')  # End the game if troll is defeated
        break

    print('The troll attacks you . . .')
    you.defend(troll.random_attack())  # Troll attacks player
    you.report()
    time.sleep(1)
    if you.health <= 0:
        print('The troll wins')  # End the game if player is defeated
        break
    print('')
