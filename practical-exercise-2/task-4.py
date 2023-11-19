#
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Для строки вывести статистику по количеству входящих в нее букв (без учета регистра), сортируя по алфавиту. Игнорируйте всё, кроме букв латиницы и кириллицы. Вывод: символ, пробел, количество. Приоритет вывода у латиницы, вывод символов в нижнем регистре.
#
# Формат ввода
# Hello Привет 123 как дела?
#
# Формат вывода
# e 1
# h 1
# l 2
# o 1
# а 2
# в 1
# д 1
# е 2
# и 1
# к 2
# л 1
# п 1
# р 1
# т 1

import re

inputString = input()

# Делаем все буквы маленьким регистром
inputString = inputString.casefold()

# Находим все буквы в предложении
allLetters = re.findall(r'[a-zа-яё]', inputString)

lettersDict = dict()

# Записываем буквы в словарь и считаем их количество
for letter in allLetters:
    if letter in lettersDict:
        lettersDict[letter] += 1
    else:
        lettersDict[letter] = 1

# Создаем отсортированный список из словаря
sortedLettersDict = sorted(lettersDict)

# Пробегаемся по сортированному списку и печатаем значения из словаря
for item in sortedLettersDict:
    print(item, lettersDict[item])