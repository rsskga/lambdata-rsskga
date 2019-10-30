"""PyCharm sample Car module"""
# https://www.jetbrains.com/help/pycharm/choosing-your-testing-framework.html
# https://www.jetbrains.com/help/pycharm/pytest.html
# https://docs.pytest.org/en/latest/fixture.html#fixture

class Car:
    """This is a class docstring"""

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        """This is a method docstring"""
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        """This is a method docstring"""
        self.speed += 5

    def brake(self):
        """This is a method docstring"""
        self.speed -= 5

    def step(self):
        """This is a method docstring"""
        self.odometer += self.speed
        self.time += 1

    def average_speed(self): # pylint: disable=inconsistent-return-statements
        """This is a method docstring"""
        if self.time != 0:
            return self.odometer / self.time

    def speed_validate(self):
        """This is a method docstring"""
        return self.speed <= 160

if __name__ == '__main__':

    MY_CAR = Car()
    print("I'm a car!")
    while True:
        ACTION = input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?").upper()
        if ACTION not in "ABOS" or len(ACTION) != 1:
            print("I don't know how to do that")
            continue
        if ACTION == 'A':
            MY_CAR.accelerate()
        elif ACTION == 'B':
            MY_CAR.brake()
        elif ACTION == 'O':
            print("The car has driven {} kilometers".format(MY_CAR.odometer))
        elif ACTION == 'S':
            print("The car's average speed was {} kph".format(MY_CAR.average_speed()))
        MY_CAR.step()
        MY_CAR.say_state()
