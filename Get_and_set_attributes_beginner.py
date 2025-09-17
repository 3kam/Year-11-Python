class Pet:
    # Constructor to initialise pet attributes
    def __init__(self, name, category, breed=None, age=0):
        self._name = name  # Public attribute for pet's name
        self.__category = category  # Private attribute for pet's category (e.g., Cat, Dog)
        self.__breed = breed  # Private attribute for pet's breed
        self.age = age  # Age of the pet
        self.__ccard = 'unknown'  # Private attribute for payment status
        self.vaccinated = False  # Boolean flag for vaccination status
        self.weight = 0  # Pet's weight, default is 0
    
    # Method to update the pet's name with validation
    def set_name(self, new_name):
        if isinstance(new_name, str):  # Ensuring input is a string
            self._name = new_name
        else:
            print('Please use a string as a name attribute')  # Error message for invalid input

    # Method to retrieve the pet's name
    def get_name(self): 
        return self._name
    
    # Method to retrieve the pet's weight
    def get_weight(self):
        return self.weight
    
    # Method to update pet's weight with validation
    def set_weight(self, new_weight):
        if isinstance(new_weight, (int, float)):  # Ensuring input is a number
            if new_weight > 0:  # Check for a positive value
                self.weight = new_weight
            else:
                print('Please enter a positive number for weight')  # Error message for invalid weight
        else:
            print('Please enter a number for weight')  # Error message for non-numeric input
    
    # Method to increase pet's age by 1 year
    def have_birthday(self):
        self.age += 1

    # String representation of pet details
    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:  # Checking if payment card is registered
            payment_status = 'registered'

        # Formatting pet details for display
        my_status = (
            'Name: ' + self._name + '\nCategory: ' + self.__category + 
            '\nAge: ' + str(self.age) + '\nPayment status: ' + payment_status +
            '\nVaccinated: ' + str(self.vaccinated)
        )
        return my_status

# Creating an instance of Pet
p1 = Pet(name='Bonnie', category='Cat', age=10)

# Setting weight for Bonnie
p1.set_weight(12)

# Printing Bonnie's weight
print('Bonnie’s weight: ', p1.weight)

# Attempting to change Bonnie’s name with invalid input (should trigger an error)
p1.set_name(56789876)

# Printing Bonnie's name after attempted update
print(p1.get_name())

# Printing Bonnie's details using the __str__ method
print(p1)