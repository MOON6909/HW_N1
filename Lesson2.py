class Student:
    # print('Hi!')
    def __init__(self):
        self.height = 160
        # print('I am alive!!!')
        self.color = 'green'
        self.smh = ''
        self.ok = 'OKAY'
        self.age = 5
        #Important:
        self.money = 100
        self.satiety = 50
        self.gladness = 50
        self.grade = 12
        if self.money <=20:
            def work(self):
                self.money = +35
        if self.grade <=2:
            def studying(self):
                self.grade = +5
        if self.grade >=12:
            def control_studying(self):
                self.grade = 12
        if self.grade >=100:
            def control_gladness(self):
                self.grade = 100

    def printer(self):
            print(self.height)
            print(self.smh)
    def holiday(self):
        self.money =-5

Yaroslav = Student()
# Olexandra = Student()
# A = Student()
# B = Student()
# C = Student()
# D = Student()
# Yaroslav.printer()
# Olexandra.printer()
# A.printer()
# B.printer()
# C.printer()
# D.printer()
# print(Yaroslav.height)
# print(Olexandra.height)
# Yaroslav.height = 159
# Olexandra.height = 157
# print(Yaroslav.height)
# print(Olexandra.height)
# Student.__init__(self=Olexandra)

#Перевірка прінтом усіх характеристик:
print(Yaroslav.money)
print(Yaroslav.satiety)
print(Yaroslav.gladness)
print(Yaroslav.grade)