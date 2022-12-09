class Human:
    def __init__(self, name = 'Human'):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passangers = []
    def add_passanger(self, human):
        self.passangers.append(human)
    def print_passangers_names(self):
        if self.passangers != []:
            print(f'Names of {self.brand} passangers:')
            for passenger in self.passangers:
                print(passenger.name)
        else:
            print(f'There are no passangers in {self.brand}')
Max = Human('Maxim')
Sviatoslav = Human('Sviatoslav')
Maxim = Human('Maxim')
car = Auto('Mercedes')
car.add_passanger(Max)
car.add_passanger(Sviatoslav)
car.add_passanger(Maxim)
car.print_passangers_names()
car1 = Auto('Tesla')
car1.print_passangers_names()
print()

