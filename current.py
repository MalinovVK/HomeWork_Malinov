import threading
import time
def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'Какое то слово №{word_count}\n')
    time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(100, 'example2.txt')
write_words(200, 'example3.txt')
write_words(300, 'example4.txt')

ex5 = threading.Thread(target=write_words, args = (10, 'example5.txt'))
ex6 = threading.Thread(target=write_words, args = (100, 'example6.txt'))
ex7 = threading.Thread(target=write_words, args = (200, 'example7.txt'))
ex8 = threading.Thread(target=write_words, args = (310, 'example8.txt'))
start = time.time()
print(f'Начало создания потока: {start}')
ex5.start()
ex5.join()
ex6.start()
ex6.join()
ex7.start()
ex7.join()
ex8.start()
ex8.join()
print(f'Конец выполнения потоков: {start - time.time()}')

# start = time.time()
# print(start)
# write_words(10, 'example0.txt')
# write_words(100 , 'example0.txt')
# write_words(200, 'example0.txt')
# write_words(300, 'example0.txt')
# elapsed_seconds = time.time() - start
# print(elapsed_seconds)
# formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_seconds))
# print(f"Отформатированное время: {formatted_time}")