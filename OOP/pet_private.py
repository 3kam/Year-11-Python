class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category  # private attribute
        self.__breed = breed        # added private attribute for breed
        self.age = age
        self.__ccard = 'unknown'    # private attribute for payment card
        self.vaccinated = False     # public attribute

    def have_birthday(self):
        self.age += 1

    def get_category(self):        # getter for category
        return self.__category

    def get_breed(self):           # getter for breed
        return self.__breed

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

# create pet object
p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)

# test direct category change (will not affect actual __category)
p1.__category = 'Dog'  # this won't change the real __category

# print object info
print(p1)

# verify private category not changed
print('Accessed with getter:', p1.get_category())
