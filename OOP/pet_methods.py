# Define the Pet class
class Pet:
    def __init__(self, name, category, age=0, dog_to_human_age=0, cat_to_human_age=0):
        # Initialize pet attributes
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'  # Initialize ccard
        self.vaccinated = False  # Initialize vaccinated
        self.account_balance = 0  # Added attribute for account balance

        # Set human-equivalent age based on category
        self.dog_to_human_age = age * 7 if category.lower() == "dog" else "N/A"
        self.cat_to_human_age = age * 6 if category.lower() == "cat" else "N/A"

    def have_birthday(self):
        # Increment age and recalculate human-equivalent age
        self.age += 1
        if self.category.lower() == 'dog': 
            self.dog_to_human_age = self.age * 7
        elif self.category.lower() == 'cat':
            self.cat_to_human_age = self.age * 6

    def vaccinate(self):
        """Vaccinate the pet and confirm with a print statement"""
        self.vaccinated = True
        print(f"{self.name} has been vaccinated.")

    def clear_balance(self):
        """Clear the pet's account balance and confirm"""
        self.account_balance = 0
        print(f"{self.name}'s account balance has been cleared.")

    def print_human_age(self):
        """Print the pet's age in human years"""
        if self.category.lower() == "dog":
            print(f"{self.name}'s age in human years: {self.dog_to_human_age}")
        elif self.category.lower() == "cat":
            print(f"{self.name}'s age in human years: {self.cat_to_human_age}")
        else:
            print(f"Human-age conversion is not available for {self.name}.")

    def __str__(self):
        # Improved payment status validation
        payment_status = "unregistered"
        if self.ccard.isdigit() and len(self.ccard) in [16, 19]:  
            payment_status = "registered"

        # Return formatted string of pet status
        my_status = f"Name: {self.name}\nCategory: {self.category}\nAge: {self.age}\nPayment status: {payment_status}\nVaccinated: {self.vaccinated}\nDog age to Human Age: {self.dog_to_human_age}\nCat age to Human Age: {self.cat_to_human_age}"
        return my_status

# Object creation and updates after initialization
p1 = Pet(name='Dino', category="Cat", age=10)  # Create pet instance
p1.ccard = '1234567890123456789'  # Set ccard after object creation
p1.vaccinate()  # Vaccinate pet
p1.clear_balance()  # Clear pet's account balance
p1.print_human_age()  # Print pet's human-equivalent age
p1.have_birthday()  # Celebrate birthday

print(p1)  # Print final pet details
