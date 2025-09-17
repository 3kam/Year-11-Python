class Pet:
    def __init__(self, name, category, age=0, ccard='unknown', vaccinated=False):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = ccard
        self.vaccinated = vaccinated

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\nPayment status: ' + payment_status + '\nVaccinated: ' + str(self.vaccinated)
        return my_status

p1 = Pet(category='Cat', name='Bonnie', age=6, ccard = '1234567890123456789', vaccinated=True)
p2 = Pet(category='Dog', name='Clyde', age=7, ccard = '0987654321987654321', vaccinated=True)
p3 = Pet(category='Rabbit', name='Ruby', age=13, ccard = '1122334455667788990', vaccinated=True)
p4 = Pet(category='Frog', name='Brain', age=6, ccard = '2224446668880001110', vaccinated=True)

pets = [p1, p2, p3, p4]

for pet in pets:
    print(pet)
    print('')

