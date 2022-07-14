# Задача 1. Напишите программу, которая принимает на вход число N и выдает 
# последовательность из N членов.


def list_num(n):
    i = 0
    list = [1]
    while i < n - 1:
        list.append(list[i] * -3)
        i += 1
    return list

n = int(input('Введите N: '))
print(list_num(n))
    