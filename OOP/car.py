class Car:
    def __init__(self, Model, Engine, Transmission, Tyres, Brakes, Suspensions, Battery, Alternator, Radiator, Exhaust, Fuel, Dashboard, Steering):
        self.model = Model
        self.engine = Engine
        self.transmission = Transmission
        self.tyres = Tyres
        self.brakes = Brakes
        self.suspensions = Suspensions
        self.battery = Battery
        self.alternator = Alternator
        self.radiator = Radiator
        self.exhaust = Exhaust
        self.fuel = Fuel
        self.dashboard = Dashboard
        self.steering = Steering

p2 = Car('Toyota camry 2008', '3.5-liter V6 engine (2GR-FE)', 'Automatic', '215/60 R16', 'Brake pads', 'Camery-Suspensions', '12V lead acid car battery', 'OEX Alternator 12V 80A Denso Style', 'ACV40 Automatic 4cyl 2.4L 2AZ-FE', 'Camry Exhaust', 'unleaded petrol', 'Camery Dashboard', 'Camery Steeringw wheel')

print('car model:', p2.model)
print('engine:', p2.engine)
print('transmission:', p2.transmission)
print('tyres:', p2.tyres)
print('brakes:', p2.brakes)
print('suspensions:', p2.suspensions)
print('battery:', p2.battery)
print('alternator:', p2.alternator)
print('radiator:', p2.radiator)
print('exhaust:', p2.exhaust)
print('fuel:', p2.fuel)
print('dashboard:', p2.dashboard)
print('steering:', p2.steering)


