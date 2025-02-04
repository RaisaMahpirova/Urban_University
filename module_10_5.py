import threading as tr
import multiprocessing as mp
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        counter = 0
        line = file.readline()
        while len(line) > 0:
            all_data.append(line)
            line = file.readline()
            counter += 1
    return counter


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

line_start_time = time.time()
thread1 = tr.Thread(target=read_info, args=(filenames[0],))
thread2 = tr.Thread(target=read_info, args=(filenames[1],))
thread3 = tr.Thread(target=read_info, args=(filenames[2],))
thread4 = tr.Thread(target=read_info, args=(filenames[3],))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread3.join()
line_finish_time = time.time()
line_result = line_finish_time - line_start_time
print(f'Линейный вызов затратил {line_result} секунд')

# Многопроцессный

if __name__ == '__main__':
    multiple_start_time = time.time()
    with mp.Pool(processes=4) as pool:
        process = map(read_info, filenames)
    multiple_finish_time = time.time()
    multiple_result = multiple_finish_time - multiple_start_time
    print(f'Многопроцессный вызов затратил {multiple_result} секунд')
