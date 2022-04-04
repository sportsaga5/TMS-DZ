# задание 1
from functools import reduce


def meet_with_people_decorator(function_to_decorate):
    """Декоратор"""
    def meet_with_people():
        """Спрашивает у пользователя его имя"""
        print("Как тебя зовут?")
        function_to_decorate()
        print("Приятно познакомиться!")
    return meet_with_people

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
@meet_with_people_decorator
def say_hello():
    """Выводит приветствие пользователя"""
    name = input('Введите имя: ')
    print("Привет,", name)

say_hello()