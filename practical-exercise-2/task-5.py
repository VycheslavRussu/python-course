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