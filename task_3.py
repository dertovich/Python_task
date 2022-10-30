import time
import os
import datetime

# Функция нахождения наибольшего общего делителя
def nod_search(a, b):
    nod = 0
    if int(float(a)) > int(float(b)):
        temp = int(float(b))
    else:
        temp = int(float(a))
    for i in range(1, temp + 1):
        if (int(float(a)) % i == 0) and (int(float(b)) % i == 0):
            nod = i
    return nod


# Функция завершения работы программы при подаче
# в один из аргументов символа 'q' или '0'
def quit_program(a):
    if a == 'q':
        print("Завершаю работу....")
        program_logging('q')
        separator = '#'
        for i in range(101):
            time.sleep(0.00001)
            print('\r', 'Завершение работы', '[', i*separator, ']', str(i), '%', end='')
        print()
        print("До свидания!")
        exit(1)
    if a == '0':
        program_logging('Null')
        print("Ошибка! Необходимо ненулевое число")
        exit(-1)


def input_nums():
    num1 = ""
    num2 = ""
    flag = True
    while flag:
        num1 = input("Введите первое число: ")
        quit_program(num1)
        num2 = input("Введите второе число: ")
        quit_program(num2)
        flag = False
        if num1.isalpha() == True or num2.isalpha() == True:
            print("Введите число, пожалуйста")
            flag = True
        if num1 == "" or num2 == "":
            program_logging('Empty')
            print("Один из аргументов пустой. Введите, пожалуйста, два числа")
            flag = True
    return num1, num2


def program_logging(flag):
    if not os.path.exists("logs"):
        os.mkdir("logs")
    if flag == 'Start':
        with open("logs/logs.txt", "a") as log_file:
            log_file.write("===Начало работы===")
            log_file.write(" Дата: " + str(datetime.datetime.fromtimestamp(int(os.path.getmtime('logs/logs.txt')))))
            log_file.write("\n")
            log_file.close()
    if flag == 'Correct':
        with open("logs/logs.txt", "a") as log_file:
            log_file.write("Первое число: " + x + " Второе число: " + y + " НОД: " + str(result))
            log_file.write(" Дата: " + str(datetime.datetime.fromtimestamp(int(os.path.getmtime('logs/logs.txt')))))
            log_file.write("\n")
            log_file.close()
    if flag == 'Empty':
        with open("logs/logs.txt", "a") as log_file:
            log_file.write("ОШИБКА! Передано пустое число")
            log_file.write(" Дата: " + str(datetime.datetime.fromtimestamp(int(os.path.getmtime('logs/logs.txt')))))
            log_file.write("\n")
            log_file.close()
    if flag == 'Null':
        with open("logs/logs.txt", "a") as log_file:
            log_file.write("ОШИБКА!Передан нуль")
            log_file.write(" Дата: " + str(datetime.datetime.fromtimestamp(int(os.path.getmtime('logs/logs.txt')))))
            log_file.write("\n")
            log_file.close()
    if flag == 'q':
        with open("logs/logs.txt", "a") as log_file:
            log_file.write("===Завершение работы===")
            log_file.write(" Дата: " + str(datetime.datetime.fromtimestamp(int(os.path.getmtime('logs/logs.txt')))))
            log_file.write("\n")
            log_file.close()


x = 0
y = 0
work = 1
while work != 'q':
    print("Программа находит наибольший общий делитель двух чисел")
    program_logging('Start')
    x, y = input_nums()
    print("Считаю циферки...")
    time.sleep(0.6)
    result = nod_search(int(y), int(x))
    print("Продумываю алгоритм.....")
    time.sleep(0.6)
    separator = '#'
    for i in range(101):
        time.sleep(0.006)
        print('\r', 'Вычисляю', '[', i * separator, ']', str(i), '%', end='')
    print()
    print("Спасибо за ожидание! Наибольший общий делитель", x, "и", y, ":", result)
    program_logging('Correct')
    work = input("Для заверешения работы нажмите 'q': ")
quit_program(work)
