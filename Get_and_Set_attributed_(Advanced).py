class Pet:
    # Constructor to initialise pet attributes
    def __init__(self, name, category, breed=None, age=0):
        self._name = name  # Public attribute for name
        self.__category = category  # Private attribute for category
        self.__breed = breed  # Private attribute for breed
        self.age = age  # Age attribute
        self.__ccard = 'unknown'  # Private attribute for payment card status
        self.vaccinated = False  # Vaccination status
        self.weight = 0  # Default weight
    
    # Method to update pet name
    def set_name(self, new_name):
        if isinstance(new_name, str):  # Ensuring name is a string
            self._name = new_name
        else:
            print('Please use a string as a name attribute')

    # Method to retrieve pet name
    def get_name(self):
        return self._name
    
    # Method to retrieve pet weight
    def get_weight(self):
        return self.weight

    # Method to retrieve pet category
    def get_category(self):
        return self.__category
    
    # Method to update pet weight with validation
    def set_weight(self, new_weight):
        if isinstance(new_weight, (int, float)):
            if new_weight > 0:
                self.weight = new_weight
            else:
                print('Please enter a positive number for weight')
        else:
            print('Please enter a number for weight')

    # String representation of the pet object
    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:  # Checking if card is registered
            payment_status = 'registered'

        # Formatting the pet details
        my_status = 'Name: ' + self._name + '\nCategory: ' + self.__category + '\nAge: ' + str(self.age) + '\nPayment status: ' + payment_status + '\nVaccinated: ' + str(self.vaccinated)
        return my_status


# Creating initial pet objects
p1 = Pet(name='Bonnie', category='Dog')
p2 = Pet('Clyde', 'Cat', 'Persian', 12)
p3 = Pet('Cindy', 'Dog', age=3)
p4 = Pet('Rocky', 'Dog', 'Labrador', 5)  # New dog added
p5 = Pet('Whiskers', 'Cat', 'Siamese')  # New cat added

# Creating a list of pets
pets = [p1, p2, p3]

# Increasing each pet's age by 1 year
for pet in pets:
    pet.age += 1

# Adding new pets to the list
pets.append(p4)
pets.append(p5)

# Printing details of only the dogs
print('\n--- Dog Information ---')
for pet in pets:
    if pet.get_category() == 'Dog':  # Filtering for dogs only
        print(pet)
        print('------------')  # Separator for readability