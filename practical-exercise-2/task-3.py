inputValue = int(input())

def wordEnding(wordCount):
    # Если число большое — оставляем от него только десятки
    while wordCount >= 100:
        wordCount = wordCount % 100

    # Если число большое 20, то оставляем от него единицы и на их основе пишем окончание.
    if wordCount >= 20:
        wordCount = wordCount % 10
        if wordCount == 0: endString = 'иев'
        elif wordCount == 1: endString = 'ий'
        elif wordCount == 2: endString = 'ия'
        elif wordCount == 3: endString = 'ия'
        elif wordCount == 4: endString = 'ия'
        elif wordCount >= 5: endString = 'иев'

    # Если число большое 10, но меньше 20 — у него фиксированное окончание 'иев'
    elif wordCount >= 10:
        endString = 'иев'

    # Если число меньше 10, то делаем то пишем окончание на основе единиц
    elif wordCount >= 0:
        if wordCount == 0: endString = 'иев'
        elif wordCount == 1: endString = 'ий'
        elif wordCount == 2: endString = 'ия'
        elif wordCount == 3: endString = 'ия'
        elif wordCount == 4: endString = 'ия'
        elif wordCount >= 5: endString = 'иев'

    return endString

print('комментар'+wordEnding(inputValue))