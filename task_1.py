# 1.Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.
n=5
def exponent_list(n):
    list_n = {}
    for i in range (n):
        list_n[i]=(-3)**i
    return list_n
exponent = exponent_list(n)
print (exponent)


# 2.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. 
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n=6
def gen_index_value(n):
    index_value = {}
    for i in range(1,n+1):
        index_value[i]=3*i+1
    return index_value
sequence=gen_index_value(n)
print (sequence)
 

# 3.Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
str1 = "in"
str2 = "string"
def str_count(str, substr):
    count = 0
    m=len(str)
    l=len(substr)-m+1
    for i in range(0,l):
        if substr[i:i+m]==str:
            count += 1
    return count
print(str_count(str1, str2))


# 4.Подсчитать сумму цифр в вещественном числе.
n = input ('Введите вещественное число: ')
summ = 0
for i in n:
    if i != "." and i != "," and i != "-":
        summ += int(i)
print (f'Сумма цифр данного числа: {summ}')


# 5.Написать программу получающую набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
n = 4
def factorial_list(n):
    factorial = 1
    f_list = []
    for i in range(1, n+1):
        factorial *= i
        f_list.append(factorial)
    return f_list
print(factorial_list(n))