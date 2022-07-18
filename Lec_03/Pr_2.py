# Задайте список. Напишите программу, которая определяет, присутствует ли в заданном
# списке строк некое число

def searchList(arr, number):
    # for i in arr:
        # if i == number:
    if number in arr:
            return 'yes'
    return 'no'


lst = [1, 4, 23, 76, 34, 56, 9, 75, 7]
n = int(input('Input a number: '))
print(searchList(lst, n))