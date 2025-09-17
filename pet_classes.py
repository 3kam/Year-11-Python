class Pet:
    def __init__(self, name, category, age, vaccinated, ccard, address, owner, balance, species, animalname, animalvaccinated):
        self.name = name
        self.category = category
        self.age = age
        self.vaccinated = vaccinated
        self.ccard = ccard
        self.address = address
        self.owner = owner
        self.balance = balance
        self.species = species
        self.animalname = animalname
        self.animalvaccinated = animalvaccinated
    

p1 = Pet('Bonnie', 'Cat', 3, 'True', '3254 6879 5732 2169', '17 Park Drive, The Shire 369', 'Annie Jenkins', 0, 'Dog', 'Foxy', 'True')

print('name:', p1.name)
print('category:', p1.category)
print('age:', p1.age)
print('ccard:', p1.ccard)
print('Vaccinated:', p1.vaccinated)
print('address:', p1.address)
print('balance:', p1.balance)
print('other animal category:',p1.species)
print('other animal name:', p1.animalvaccinated)

name = 'Bonnie'
animal_category = 'Cat'
age = 3 #integer
vaccinated = True
ccard = '3254 6879 5732 2169'
billing_address = '17 Park Drive, The Shire 3695'
owner_name = 'Annie Jenkins'
account_balance = 0
