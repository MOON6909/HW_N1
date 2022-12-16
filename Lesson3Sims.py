import random
import time
import datetime

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_of_car))
        self.fuel = brand_list[self.brand]['fuel']
        self.strenght = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

brand_of_car = {
    'BMW':{'fuel':100, 'strength':100, 'consumption':6},
    'Lada':{'fuel': 50, 'strength': 40, 'consumption': 10},
    'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
    'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
}
class Human:
    def __init__(self, name=None, job=None, car=None):
        self.name = name
        self.job = job
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.tired = 0
    def get_home(self):
        self.money-=5
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        self.satiety +=50
    def work(self):
        self.money +=25
        self.tired +=60
    def shopping(self):
        self.money -=10
    def chill(self):
        self.gladness +=30
    def clean_home(self):
        self.tired +=20
        self.gladness =+20
    def to_repair(self):
        self.money -=30
    def days_indexes(self, day):
        self.days_lived += 1
    def is_alive(self):
        pass
    def Live(self, day):
        pass
# class Job:
#     def __init__(self, job_list):
#         self.job = random.choice(list(job_list))
#         self.get_money = job_list[self.job]['money']
#         self.gladness = job_list[self.job]['gladness']
# job_listt = {
#     'Cleaner':{'money':+25, 'gladness':-30},
#     'Factory_worker': {'money': +50, 'gladness': -40}
# }
class A_job:
    def __init__(self, brand, name=None):
        self.company = brand
        self.worker = []
        self.name = name
    def working(self, human):
        self.worker.append(human)
    def print_workers_names(self):
        for passenger in self.worker:
            print(passenger.name)
        if self.worker != []:
            print(f'є працівниками «{self.company}»')
Soya=Human('Soya')
Tom = Human('Tom')
job = A_job('The best company ever')
job.working(Soya)
job.working(Tom)
job.print_workers_names()
job1 = A_job('Just a company')
job1.print_workers_names()
start_time = time.time()


#Перевіряти характеристики класів тут через Сою та Тома ↓↓↓.
print(Soya.money)
Soya.work()
Soya.shopping()
print(Soya.money)
print(Soya.car)




#Перевіряти характеристики класів тут через Сою та Тома ↑↑↑.
def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)

        print(timer, end="\r")

        time.sleep(1)

        total_seconds -= 1

    print("Життя обірвалось.")

# Часу до смерті :D
h = input("Годин до смерті: ")
m = input("Хвилин до смерті: ")
s = input("Секунд до смерті: ")
countdown(int(h), int(m), int(s))