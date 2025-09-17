import random, time  # Importing the random and time modules for gameplay mechanics

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        # Initialising the fighter's attributes: name, health, weapon power, and shield defence
        self.name = name
        self.__health = starting_health  # Health is kept private to restrict direct modification
        self.weapon = weapon  # Weapon strength determines attack power
        self.shield = shield  # Shield helps absorb incoming attacks

    def report(self):
        # Prints the fighter’s current health status
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self):
        # Checks if health has dropped to zero or below, indicating defeat
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        # Generates an attack power within a range based on weapon strength
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power

    def skill_attack(self):
        # A skill-based attack where timing is crucial for maximum impact
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        target = random.randint(2,6)  # Randomised target time for hitting enter
        print('Hit enter in exactly', target, 'Seconds')

        tic = time.time()  # Start timing
        input()  # Waits for player input
        toc = time.time()  # End timing
        time_taken = toc - tic  # Calculates reaction time

        multiplier = 3 - abs(target - time_taken)  # Adjusts attack power based on timing accuracy
        if multiplier < 2:
            multiplier = 0  # Penalises mistimed hits

        print('Attack power:', attack_power)
        print('Multiplier:', round(multiplier, 2))
        return int(attack_power * multiplier)

    def defend(self, attack_power):
        # Calculates damage taken after applying shield protection
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage  # Reduces health based on actual damage received
            print('Damage:', damage)
        else:
            print('No damage')  # Attack was completely absorbed by the shield


# Creating two fighters: the player and the troll opponent
you = Fighter('You',100,60,20)
troll = Fighter('Troll',300,30,10)

# Displaying initial health status of both fighters
you.report()
troll.report() 

# Main combat loop
while True:
    print('You attack the troll')
    troll.defend(you.skill_attack())  # Player attacks using a skill-based method
    troll.report()
    time.sleep(2)  # Adding a short pause for pacing
    print('')

    if troll.is_dead():  # Checking if the troll has been defeated
        print('You win')
        break

    print('The troll attacks you . . . ')
    you.defend(troll.random_attack())  # Troll counterattacks with a random strike
    you.report()
    time.sleep(2)  # Short pause before the next round

    if you.is_dead():  # Checking if the player has been defeated
        print('The troll wins')
        break
    print('')