import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Пора навчатися.")
        self.progress += 0.2
        self.gladness -= 5
        self.money -= 10

    def to_sleep(self):
        print("Йду спатки...")
        self.gladness += 3

    def to_chill(self):
        print("Відпочинок!")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 20
        if random.randint(1, 5) == 1:
            self.gladness += 3
            print("Відпочинок вдався особливо добре")

    def to_work(self):
        print("Час працювати!")
        self.money += 50
        self.gladness -= 7

    def is_alive(self):
        if self.progress < -1:
            print("Вигнали...")
            self.alive = False
        elif self.gladness <= 0:
            print("Депресняк...")
            self.alive = False

    def end_of_day(self):
        print(f"Радість = {self.gladness}")
        print(f"Прогрес = {round(self.progress, 2)}")
        print(f"Гроші = {self.money}")

    def live(self, day):
        print(f"{'День ' + str(day):=^50}")

        if self.money < 0:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        elif self.gladness < 30:
            self.to_chill()
        else:
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_chill()
            else:
                self.to_sleep()

        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")

for day in range(1, 366):
    if not nick.alive:
        print("Тобі кранти")
        break
    nick.live(day)
    if nick.alive:
        print("Живем, живем. Живем, живем!")
if nick.alive:
    print("Я живий!!!")