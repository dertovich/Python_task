import time

# Функция нахождения наибольшего общего делителя
def nod_search(a, b):
    nod = 0
    var_1 = abs(int(float(a)))
    var_2 = abs(int(float(b)))
    if var_1 > var_2:
        temp = var_2
    else:
        temp = var_1
    for i in range(1, temp + 1):
        if (var_1 % i == 0) and (var_2 % i == 0):
            nod = i
    return nod


# Функция завершения работы программы при подаче
# в один из аргументов символа 'q' или '0'
def quit_program(a):
    if a == 'q':
        print("Завершаю работу....")
        separator = '#'
        for i in range(101):
            time.sleep(0.00001)
            print('\r', 'Завершение работы', '[', i*separator, ']', str(i), '%', end='')
        print()
        print("До свидания!")
        exit(1)
    if a == '0':
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
            print("Один из аргументов пустой. Введите, пожалуйста, два числа")
            flag = True
    return num1, num2


x = 0
y = 0
work = 1
while work != 'q':
    print("Программа находит наибольший общий делитель двух чисел")
    x, y = input_nums()
    print("Считаю циферки...")
    time.sleep(0.6)
    result = nod_search(x, y)
    print("Продумываю алгоритм.....")
    time.sleep(0.6)
    separator = '#'
    for i in range(101):
        time.sleep(0.006)
        print('\r', 'Вычисляю', '[', i * separator, ']', str(i), '%', end='')
    print()
    print("Спасибо за ожидание! Наибольший общий делитель", x, "и", y, ":", result)
    work = input("Для заверешения работы нажмите 'q': ")
quit_program(work)
