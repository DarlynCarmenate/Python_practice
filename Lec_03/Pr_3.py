# Напишите, програму, которая определит позицию второго вхождения строки в списке,
# либо сообщит, что ее нет


def searchElem(arr, element):
    count = 0
    for i in range(len(arr)):
        if arr[i] == element:
            count += 1
        if count == 2:
            return f'yes: {i + 1}'
    return 'no'

lst = ['sff', 'fkgj', 'djf', 'dfe', 'sff', 'df', 'sfsf']
print(searchElem(lst, 'sff'))

