import random
import time
import datetime

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_of_car))
        self.fuel = brand_list[self.brand]['fuel']
        self.strenght = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

        # Урок 3-4:
    def driver(self):
            if self.strenght > 0 and self.consumption:
                self.fuel -= self.consumption
                self.strenght -= 1
                return True
            else:
                print('Машина не може рухатись.')
                return False

brand_of_car = {
    'BMW':{'fuel':100, 'strength':100, 'consumption':6},
    'Lada':{'fuel': 50, 'strength': 40, 'consumption': 10},
    'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
    'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
}
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
class Job:
    def __init__(self, job_list):
        self.job=random.choice((list(job_list)))
        self.salary=job_list[self.job]['salary']
        self.gladness_less=job_list[self.job]['gladness.less']
    job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    'Python developer':{"salary": 40, "gladness_less": 3},
    'C++ developer': {"salary": 45, "gladness_less": 25},
    'Rust developer': {"salary": 70, "gladness_less": 1},
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
        self.home=House()
        self.money-=5

    def get_car(self):
        self.car=Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job=Job(job_list)

    def eat(self):
        if self.home.food<=0:
            self.shopping('food')
        else:
            if self.satiety>=100:
                self.satiety=100
                return
            self.satiety+=5
            self.home.food=-5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money+=self.job.salary
        self.gladness-=self.job.gladness_less
        self.satiety-=4
        self.tired +=60

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<20:
                manage='fuel'
            else:
                self.to_repair()
                return
        if manage=='fuel':
            print('Купив пальне')
            self.money-=100
        elif manage=='food':
            print('Купив їжу')
            self.money-=50
            self.home.food+=50
        elif manage=='delicious':
            print("Ура! Смачненьке!")
            self.satiety+=2
            self.gladness+=10
            self.money-=15

    def chill(self):
        self.gladness +=10
        self.home.mess+=5

    def clean_home(self):
        self.gladness -=5
        self.home.mess=0
        self.tired +=20

    def to_repair(self):
        self.car.strength+=100
        self.money -=50

    def days_indexes(self, day):
        day=f'today the {day} of {self.name} a life'
        print(f'{day:=^50}', '\n')
        human_indexes=self.name + 's indexes'
        print(f'{human_indexes:^50}', '\n')
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        home_indexes='Home indexes'
        print(f'{home_indexes:^50}', '\n')
        print(f'Food - {self.home.food}:')
        print(f'Mess - {self.home.mess}')
        car_indexes=f'{self.car.brand} car indexes'
        print(f'Car - {self.home.mess}')
        print(f'Fuel - {self.car.strenght}')

    def is_alive(self):
        if self.gladness<0:
            print('Депресія')
            return False
        if self.satiety<0:
            print('Голод')
            return False
        if self.money<-500:
            print('Банкрот')
            return False

    def live(self, day):
        if self.is_alive()==False:
            return False
        if self.home is None:
            print('Переселися в будинок')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f'Я купив машину {self.car.brand}')
        if self.job is None:
            self.get_job()
            print(f'У мене немає роботи, тому я йду отримувати її {self.job.job} з зарплатою {self.job.salary}')
        self.days_indexes()
        dice=random.randint(1, 4)
        if self.satiety<20:
            print('Я йду їсти')
            self.eat()
        elif self.gladness<20:
            if self.home>15:
                print('Я хочу відпочити, але в будинку брудно. \n Тож я піду прибирати будинок :(')
            else:
                print('Я відпочиваю')
                self.chill()
        elif self.money<0:
            print('Я йду працювати.')
            self.work()
        elif self.car.strength<15:
            print('Мені потрібно відремонтувати машину.')
            self.to_repair()
        elif dice==1:
            print('Відпочиньмо')
            self.chill()
        elif dice==2:
            print('Початок роботи')
            self.work()
        elif dice==3:
            print('Час прибирання.')
            self.clean_home()
        elif dice==4:
            print('Час смачненького :3 ЮПІІ')
            self.shopping(manage='delicacies')

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
nick=Human(name='Nick')
for day in range(1,8):
    if nick.live(day)==False:
        break
