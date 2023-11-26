# F. Анаграммы
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Дана текстовая строка (кириллица) со словами через пробел. Среди слов найти все пары анаграмм. Пары анаграмм вывести в алфавитном порядке, среди пар сортировка тоже по алфавиту. Каждая пара выводится в новой строке в нижнем регистре.
#
# Формат ввода
# Кот нос ток сон клад рама вход книга вдох
#
# Формат вывода
# вдох вход
# кот ток
# нос сон

input_string = 'Кот нос ток сон клад рама вход книга вдох нос'
input_string = input_string.casefold()
words_list = input_string.split()

words_dict = dict()
letter_list = list()

for word in words_list:
    if word == words_dict:
        None
    else:
        for letter in word:
            letter_list.append(letter)
        words_dict[word] = letter_list.copy()
        letter_list.clear()

for first_word in words_dict:
        if words_dict[first_word] == words_dict[first_word]:
            print('yes')

print(words_dict)




# if {'g', 'w'} == {'w', 'g'}:
#      print('Yes')
# else:
#     print('No')

# for i in range(0, len(inputString)):
#     print(inputString[i])
#     # reversedString += inputString[i]


# print(len(inputString))