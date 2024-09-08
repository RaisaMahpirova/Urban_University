def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(1, 'Hello World')
print_params(c=False)
print_params()
print_params(b=25)  #вызов функции срабатывает, но появляется предупреждение
print_params(c=[1, 2, 3])  #об изменении типа данных
values_list = [11, 'The string', False]
values_dict = {'a': 5, 'b': 'some words', 'c': [1, 2, 3]}
values_list_2 = ['The Sun', False]
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
