from datetime import datetime
from multiprocessing import Pool
def red_info(name):
    all_data = []
    with open(name, 'r') as file:
        data = file.readline()
        all_data.append(data)

filenames = [f'C:/Users/botki/PycharmProjects/Urban_HW/module_11/file {number}.txt' for number in range(1,5)]
t1 = datetime.now()
for names in filenames:
    red_info(names)
t2 = datetime.now()
print(f'{t2 - t1} LN')

if __name__ == '__main__':
    t_1 = datetime.now()
    with Pool(1) as p:
        map(red_info, filenames)
    t_2 = datetime.now()
    print(f'{t_2-t_1} MP')



