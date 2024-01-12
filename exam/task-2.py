# Написать функцию factorial, принимающую одно целое число.
# Функция должна возвращать факториал исходного числа.


def factorial(value):
    answer = 1
    while value != 0:
        answer = answer * value
        value -= 1
    return answer