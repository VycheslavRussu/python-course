#
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Написать программу, которая из исходной строки оставляет только уникальные слова (без учета регистра), но в том порядке, в котором они первый раз встретились. Слова разделены пробелом, вывод слов в нижнем регистре.
#
# Формат ввода
# Мама мыла раму Мыла мама папа Привет
#
# Формат вывода
# мама мыла раму папа привет

inputString = input()

# Делаем регистр маленьким
inputString = inputString.casefold()

# Сплитим строку на слова
allWords = inputString.split()

uniqueWordsList = list()
answerString = str()

# Считаем уникальные слова
for word in allWords:
    if word not in uniqueWordsList:
        uniqueWordsList.append(word)
        answerString += word + ' '

print(answerString)