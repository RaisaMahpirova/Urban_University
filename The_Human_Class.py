class Human:
    def __init__(self, name = 'J. Doe', age = 0):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, теперь мне {self.age}')


Den = Human('Денис', 22)
Tom = Human('Том', 15)
Jane_Doe = Human(age=31)



