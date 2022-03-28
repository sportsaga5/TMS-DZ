# задание 1
from functools import reduce


def decorator(function_to_decorate):
    """Декоратор"""
    def wrapper_around():
        """Спрашивает у пользователя его имя"""
        print("Как тебя зовут?")
        function_to_decorate()
        print("Приятно познакомиться!")
    return wrapper_around

# задание 2
print(list(map(lambda x: x**2, range(1, 11))))
print(list(filter(lambda x: x%2 == 0, range(1, 11))))
def my_sum(a, b):
    """Складываем два числа"""
    sum = a + b
    return sum
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(reduce(my_sum, numbers))

# задание 3
def hello_to():
    """Выводит приветствие пользователя"""
    name = input('Введите имя: ')
    print("Привет,", name)

hello_to_decorator = decorator(hello_to)

hello_to_decorator()