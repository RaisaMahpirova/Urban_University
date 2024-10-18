def custom_write(file_name, strings):
    strings_positions = {}
    keys = []
    values = []
    file = open(file_name, 'w')
    file.close()
    c = 1
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        position = (c, file.tell())
        keys.append(position)
        file.write(i + '\n')
        c += 1
        values.append(i)
    file.close()

    return dict(zip(keys, values))


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)