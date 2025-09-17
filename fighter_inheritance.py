import random, time 

class Fighter:
    def __init__(self, name, starting_health, weapon, shield):
        self.name = name
        self._health = starting_health  # Health stat, kept protected but still accessible
        self.weapon = weapon  # Attack power comes from this weapon
        self.shield = shield  # Defensive gear to reduce damage

    def report(self):
        # Prints current health status
        print(self.name + ': Health:', self._health)

    def is_dead(self):
        # Checks if the fighter has run out of health
        return self._health <= 0

    def random_attack(self):
        # Generates a random attack power based on weapon strength
        attack_power = random.randint(int(self.weapon / 2), self.weapon * 2)  # Fixing int conversion issue
        print('Attack power:', attack_power)
        return attack_power

    def skill_attack(self):
        # Special attack that depends on the player's timing
        attack_power = random.randint(int(self.weapon / 2), self.weapon * 2)  # Same fix for int conversion
        target = random.randint(2, 6)  # Time window for attack
        print('Hit enter in exactly', target, 'seconds')

        tic = time.time()
        input()  # Player must press Enter within the given time frame
        toc = time.time()

        time_taken = toc - tic
        multiplier = 3 - abs(target - time_taken)  # Accuracy impacts attack strength

        if multiplier < 2: 
            multiplier = 0  # If too far off, attack fails

        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)

        return attack_power * multiplier

    def defend(self, attack_power):
        # Reduces incoming attack based on shield strength
        damage = attack_power - self.shield
        if damage > 0:
            self._health -= damage  # Corrected from __health to ensure it works properly
            print('Damage:', damage)
        else:
            print('No damage')  # Shield fully blocks the attack

class Wizard(Fighter):
    def __init__(self, name, starting_health, weapon, shield, magic):
        super().__init__(name, starting_health, weapon, shield)
        self.magic = magic  # Wizards have additional magic power

    def random_attack(self):
        # Generates a random attack but with added magic strength
        attack_power = random.randint(int(self.weapon / 2), self.weapon * 2)  
        print('Attack power:', attack_power)
        return attack_power + self.magic  # Magic boosts the attack

# Creating characters
you = Fighter('You', 100, 60, 20)
wiz = Wizard('The Grey Wizard', 100, 30, 10, 50)

# Displays starting stats
you.report()
wiz.report()

while True:
    # Player attacks first
    print('You attack the', wiz.name)
    wiz.defend(you.skill_attack())  # Wizard takes damage
    wiz.report()
    time.sleep(2)
    print('')

    # Check if the wizard has been defeated
    if wiz.is_dead():
        print('You win')  # Player victory message
        break

    # Wizard fights back
    print(wiz.name, 'attacks you . . . ')
    you.defend(wiz.random_attack())  # Player takes damage
    you.report()
    time.sleep(2)

    # Check if the player has lost
    if you.is_dead():
        print(wiz.name, 'wins')  # Corrected typo
        break
    print('')