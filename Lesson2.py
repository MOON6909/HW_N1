class Student:
    print('Hi!')
    def __init__(self):
        self.height = 160
        print('I am alive!!!')
        self.color = 'green'
        self.smh = ''
        self.ok = 'OKAY'
        self.age = 5
        self.money = 100

    def printer(self):
            print(self.height)
            print(self.smh)
    def holiday(self):
        self.money =-5

    def work(self):
        self.money =+1


Yaroslav = Student()
Olexandra = Student()
A = Student()
B = Student()
C = Student()
D = Student()
Yaroslav.printer()
Olexandra.printer()
A.printer()
B.printer()
C.printer()
D.printer()
print(Yaroslav.height)
print(Olexandra.height)
Yaroslav.height = 159
Olexandra.height = 157
print(Yaroslav.height)
print(Olexandra.height)
Student.__init__(self=Olexandra)
