# 3. Напишите программу, которая будет на вход принимать число N и выводить числа 
# от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

n = int(input('Введите число: '))
print(*range(-n, n + 1))