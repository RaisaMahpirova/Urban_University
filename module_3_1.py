calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(s):
    info = [str(len(s)), s.upper(), s.lower()]
    info = tuple(info)
    count_calls()
    return info


def is_contains(string, list_to_search):
    cont = False
    if list_to_search.upper() in string.upper():
        cont = True
    count_calls()
    return cont


print(string_info('Какой чудесный день'))
print(is_contains('some words', 'Word'))
print(string_info('Учиться мне не лень'))
print(is_contains('some words', 'Worm'))
print(string_info('Не хочу на работу'))
print(is_contains('some words', 'some'))
print(calls)
