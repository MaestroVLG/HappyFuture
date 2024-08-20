import os
import time
from multiprocessing import Pool

#filenames = [os.path.abspath(f'file {number}.txt') for number in range(1, 5)]
#print(filenames)


def read_info(filename):
    all_data = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            all_data.append(line)
            line = f.readline()

if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in range(1, 4)]

#     #Линейный вызов
# start = time.time()
# for filename in filenames:
#     with open(filename, 'r') as f:
#            read_info(filename)
# end = time.time()
# print(end - start)

# Многопроцессорный вызов
    start = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end = time.time()
    print(end - start)
