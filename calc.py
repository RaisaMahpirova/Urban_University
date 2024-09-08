import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def deg():
    num1, num2 = get_values()
    res = num1 ** num2
    insert_values(res)


def del_():
    answer_entry.delete(0, 'end')
    number1_entry.delete(0, 'end')
    number2_entry.delete(0, 'end')


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x400")
window.resizable(False, False)
# Кнопки
button_add = tk.Button(window, text='+', width=3, height=2, command=add)
button_add.place(x=60, y=240)
button_sub = tk.Button(window, text='-', width=3, height=2, command=sub)
button_sub.place(x=110, y=240)
button_mul = tk.Button(window, text='*', width=3, height=2, command=mul)
button_mul.place(x=160, y=240)
button_div = tk.Button(window, text='/', width=3, height=2, command=div)
button_div.place(x=210, y=240)
button_deg = tk.Button(window, text='^', width=3, height=2, command=deg)
button_deg.place(x=260, y=240)
button_del = tk.Button(window, text='Очистить все поля', width=32, height=2, command=del_)
button_del.place(x=60, y=300)
# Окна
number1_entry = tk.Entry(window, width=38)
number1_entry.place(x=60, y=55)
number2_entry = tk.Entry(window, width=38)
number2_entry.place(x=60, y=125)
answer_entry = tk.Entry(window, width=38)
answer_entry.place(x=60, y=195)
# Подписи
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=60, y=33)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=60, y=103)
answer = tk.Label(window, text="Ответ:")
answer.place(x=60, y=173)
window.mainloop()
