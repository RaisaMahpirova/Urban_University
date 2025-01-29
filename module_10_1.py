# Импорты необходимых модулей и функций

import time
import threading


# Объявление функции write_words

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


# Взятие текущего времени

start_time = time.time()

# Запуск функций с аргументами из задачи

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени

ended_time = time.time()

# Вывод разницы начала и конца работы функций

print(f'Работа потоков {ended_time - start_time}')

# Взятие текущего времени

start_time_2 = time.time()

# Создание и запуск потоков с аргументами из задачи

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread1.start()

thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread2.start()


thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread3.start()

thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread4.start()

thread3.join()

# Взятие текущего времени

ended_time_2 = time.time()

# Вывод разницы начала и конца работы потоков

print(f'Работа потоков {ended_time_2 - start_time_2}')
