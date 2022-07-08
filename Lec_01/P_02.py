# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

a = list(map(int, input().split()))
max_number = a[0]
for i in a:
    if i > max_number:
        max_number = i
print(max_number)