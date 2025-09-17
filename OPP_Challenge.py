import random, time

class Fighter:
    def __init__(self, name, health, weapon, shield, abilities):
        self.name = name
        self.__health = health
        self.weapon = weapon
        self.shield = shield
        self.abilities = abilities

    def report(self):
        print(self.name+': Health:', self.__health)

    def is_dead(self):
        return self.__health <= 0

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2) + self.abilities.get('strength', 0)
        print('Attack power:', attack_power)
        return attack_power

    def skill_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        target = random.randint(2,6)
        print('Hit enter in exactly', target, 'seconds')
        tic = time.time()
        input()
        toc = time.time()
        multiplier = max(0, 3 - abs(target - (toc - tic)))
        strength_bonus = self.abilities.get('strength', 0)
        final_attack = int((attack_power + strength_bonus) * multiplier)
        print('Attack power:', final_attack)
        return final_attack

    def defend(self, attack_power):
        agility = self.abilities.get('agility', 0)
        if random.randint(0, 100) < agility:
            print(self.name, 'dodged the attack!')
            return
        damage = attack_power - self.shield - self.abilities.get('defence', 0)
        self.__health -= max(0, damage)
        print('Damage:', max(0, damage))


class Wizard(Fighter):
    def __init__(self, name, abilities):
        super().__init__(name, 80, 30, 10, abilities)
        self.magic = abilities.get('magic', 0)

    def random_attack(self):
        return super().random_attack() + self.magic


class Tank(Fighter):
    def __init__(self, name, abilities):
        super().__init__(name, 150, 20, 40, abilities)


class Ninja(Fighter):
    def __init__(self, name, abilities):
        super().__init__(name, 90, 50, 15, abilities)
        

    def random_attack(self):
        base = super().random_attack()
        if random.random() < 0.3:
            print("Critical hit!")
            base *= 2
        return base

class Brawler(Fighter):
    def __init__(self, name, abilities):
        super().__init__(name, 110, 35, 15, abilities)
        self.rage = 0

    def random_attack(self):
        base = super().random_attack() + self.rage
        self.rage += 5
        return base

class Elf_Archer(Fighter):
    def __init__(self, name, abilities):
        base = super().__init__(name, 80, 25, 15, abilities)
        if random.random() * 0.75:
            print("Critical hit!: Double shot applied")
            return base
        
class Palandin(Fighter):
    def __init__(self, name, abilities):
        super().__init__(name, 80, 30, 35, abilities)
        

class Assasssin(Fighter):
    def __init__(self, name, abilities):
        super().__init__(name, 70, 35, 10, abilities)
        
class Druid(Fighter):
    def __init__(self, name, abilities):
        super().__init__(name, 35, 15, 20, abilities)
        

class Berserker(Fighter):
    def __init__(self, name, abilities):
        super().__init__(name, 60, 45, 10, abilities)
        

class Enemy(Fighter):
    pass


class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 80, 30, 10, {'strength': 5})


class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 100, 40, 20, {'strength': 10})


class Lich(Enemy):
    def __init__(self):
        super().__init__("Lich", 70, 30, 10, {'magic': 20})
        self.has_rez = True

    def defend(self, incoming):
        super().defend(incoming)
        if self.is_dead() and self.has_rez:
            print("Lich resurrects from the grave!")
            self.__health = 50
            self.has_rez = False

class Goblin_Scout(Enemy):
    def __init__(self):
        super().__init__("Goblin Scout", 80, 30, 10, {'strength': 5})

class Necromancer(Enemy):
    def __init__(self):
        super().__init__("Goblin Scout", 80, 30, 10, {'strength': 5})

class Fire_Elemental(Enemy):
    def __init__(self):
        super().__init__("Goblin Scout", 80, 30, 10, {'strength': 5})

class Shadow_Assassin(Enemy):
    def __init__(self):
        super().__init__("Goblin Scout", 80, 30, 10, {'strength': 5})

def allocate_points():
    total = 100
    abilities = {'strength': 0, 'agility': 0, 'defence': 0, 'speed': 0, 'magic': 0}
    print("Allocate 100 ability points:")
    for key in abilities:
        while True:
            try:
                val = int(input(f"{key.capitalize()} (remaining: {total}): "))
                if 0 <= val <= total:
                    abilities[key] = val
                    total -= val
                    break
            except ValueError:
                continue
    return abilities


def choose_fighter():
    print("Choose your class:\n1. Wizard\n2. Tank\n3. Ninja\n4. Brawler")
    choice = input("Enter number: ")
    name = input("Enter your name: ")
    abilities = allocate_points()
    if choice == '1':
        return Wizard(name, abilities)
    elif choice == '2':
        return Tank(name, abilities)
    elif choice == '3':
        return Ninja(name, abilities)
    else:
        return Brawler(name, abilities)


def choose_enemy():
    return random.choice([Troll(), Orc(), Lich()])


player = choose_fighter()
enemy = choose_enemy()

print("\nA wild", enemy.name, "appears!\n")

while not player.is_dead() and not enemy.is_dead():
    if player.abilities.get('speed', 0) >= enemy.abilities.get('speed', 0):
        print("\nYour turn:")
        move = input("Choose attack: (r)andom or (s)kill: ")
        dmg = player.skill_attack() if move == 's' else player.random_attack()
        enemy.defend(dmg)
        enemy.report()
        if enemy.is_dead(): break

        time.sleep(1)
        print("\nEnemy attacks...")
        player.defend(enemy.random_attack())
        player.report()
    else:
        print("\nEnemy attacks first...")
        player.defend(enemy.random_attack())
        player.report()
        if player.is_dead(): break
        time.sleep(1)
        print("\nYour turn:")
        move = input("Choose attack: (r)andom or (s)kill: ")
        dmg = player.skill_attack() if move == 's' else player.random_attack()
        enemy.defend(dmg)
        enemy.report()

print("\nGAME OVER!")
print(enemy.name + " wins!" if player.is_dead() else player.name + " wins!")