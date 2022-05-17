# Сделать программу которая создаёт заданное количество файлов
# с названием которое соответствует номеру итерации его создания.
# В трёх вариантах:
# 1.без потоков и процессов
# 2.с помощью потоков
# 3.с помощью процессов
# В каждом варианте сохранять в отдельную папку
import os
import time
from threading import Thread
from multiprocessing import Process

n = int(input("Введите количество добавляемых файлов: "))

print("\nCоздание файлов без процессов и потоков")
if not os.path.isdir("Без процессов и потоков"):
    os.mkdir("Без процессов и потоков")
os.chdir("Без процессов и потоков")
for i in range(n):
    with open(f'{i + 1}_without.txt', 'w') as my_file:
        time.sleep(0.5)
print("Файлы без потоков и процессов созданы")

print("\nCоздание файлов c помощью потоков")
os.chdir("..")
if not os.path.isdir("С потоками"):
    os.mkdir("С потоками")
os.chdir("С потоками")


def func_thread():
    with open(f'{i + 1}_thread.txt', 'w') as my_file_thread:
        time.sleep(0.5)


for i in range(n):
    thread = Thread(target=func_thread())
    thread.start()

print("Файлы потоками созданы")

print("\nCоздание файлов c помощью процессов")
os.chdir("..")
if not os.path.isdir("С процессами"):
    os.mkdir("С процессами")
os.chdir("С процессами")


def func_process():
    with open(f'{i + 1}_process.txt', 'w'):
        print()


for i in range(n):
    process = Process(target=func_process(), args=(i,))
    process.start()

print("Файлы процессами созданы")
