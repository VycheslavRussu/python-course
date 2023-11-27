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