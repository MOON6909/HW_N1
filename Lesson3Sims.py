import random
class Human:
    def __init__(self, name=None, job=None, car=None):
        self.name = name
        self.job = job
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self, manage):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass
    def days_indexes(self, day):
        pass
    def is_alive(self):
        pass
    def Live(self, day):
        pass
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strenght = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']
brand_of_car = {
    'BMW'{'fuel'}