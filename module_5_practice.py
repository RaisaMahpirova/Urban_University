class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password_):
        self.data[username] = password_

    def verification(self, username, password_):
        is_confirm = False
        counter = 1
        while not is_confirm:
            if counter == 3:
                print("Попробуйте в другой раз")
                exit()
            elif self.data[username] == password_:
                is_confirm = True
                print("Вход выполнен успешно!")
            else:
                print(f"Неверный пароль. Попыток осталось: {3 - counter}")
                counter += 1
                password_ = input("Введите пароль: ")

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        is_confirm = False
        while not is_confirm:
#            if len(password) < 8:
#                print("Пароль должен содержать 8 знаков")
#                password = input("Введите пароль: ")
#                password_confirm = input("Повторите пароль: ")
            if password_confirm == password:
                self.password = password
                is_confirm = True
            else:
                print(f"Пароли не совпадают. Попробуйте снова.")
                password = input("Введите пароль: ")
                password_confirm = input("Повторите пароль: ")


if __name__ == '__main__':
    database = Database()
    failed = False
    while True:
        if not failed:
            print("Добро пожаловать!", end=' ')
        choice = int(input("Выберите действие:\n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            if login in database.data:
                password1 = input("Введите пароль: ")
                if password1 == database.data[login]:
                    failed = False
                    print("Вход выполнен успешно!")
                else:
                    database.verification(login, password1)
            else:
                failed = True
                print("Пользователь с таким логином не найден! Зарегестрируйтесь или попробуйте снова.")

        if choice == 2:
            name = input("Введите логин: ")
            if name in database.data:
                failed = True
                print("Пользователь с таким логином уже существует. Выберите другой логин или войдите.")
                continue
            else:
                enter_password = input("Введите пароль: ")
                while len(enter_password) < 8:
                    print("Пароль должен содержать минимум 8 символов")
                    enter_password = input("Введите пароль: ")
                repeat_password = input("Повторите пароль: ")
                user = User(name, enter_password, repeat_password)
                failed = False
                database.add_user(user.username, user.password)
                print("Вы успешно зарегестрировались!")
