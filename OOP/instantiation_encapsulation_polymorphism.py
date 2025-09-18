#---begin Python ---
class Car:
    def __init__(self, make, model, year, colour):
        # Constructor method to initialise car attributes
        self.make = make # Manufacturer of the car (e.g: Toyota, Ford)
        self.model = model # Car model type (e.g.: Civic, Camry, Mustang)
        self.year = year # Year of manufacture
        self.colour = colour # Colour of car

# Method is used to make the car start
    def start(self):
        print(f"{self.make} {self.model} is starting.")

# Method is used to make the car stop
    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

# Instantiating objects from the Car class
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2018, "Blue")
car3 = Car("Ford", "Mustang", 2021, "Black")

car1.start()  # Output: Toyota Camry is starting.
car2.stop()   # Output: Honda Civic is stopping.
car3.start()  # Output: Ford Mustang is starting.
car3.stop()   # Output: Ford Mustang is stopping.
print(f"Make: {car3.make}, Model: {car3.model}, Year: {car3.year}, Colour: {car3.colour}") # Output: Ford Mustang Full reference model using f-string making it simple to use.
#--- end python ---
