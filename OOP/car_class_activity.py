class Car:
    def __init__(self, make, model, year, price=None, for_sale=True):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_sale = for_sale

    def __str__(self):
        return f"|Make: {self.make}, Model: {self.model}, For sale: {self.for_sale}|"

c1 = Car('Mazda', '6', 2005, price=10000, for_sale=True)
c2 = Car('Toyota', 'Camry', 2008, for_sale=True)
c3 = Car('BatMobile', 'Lincoln Futura', 1939, for_sale=False)
c4 = Car('Tesla', 'Model Y', 2025, for_sale=True)
cars = [c1, c2, c3, c4]

for car in cars:
    print(car)