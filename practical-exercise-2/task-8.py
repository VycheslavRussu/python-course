# H. Общие элементы
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# На вход поступают два списка элементов в виде строки. Выведите все элементы, которые входят как в первый, так и во второй список, в порядке возрастания, через пробел.
#
# Формат ввода
# aahrh44547hgfd
# dngey580654fdgdd
# Формат вывода
# 4 5 d f g
#

first_string = input()
second_string = input()

all_symbols_list_first = list()
all_symbols_list_second = list()

for symbol in first_string:
    all_symbols_list_first.append(symbol)

for symbol in second_string:
    all_symbols_list_second.append(symbol)

unique_symbols_dict_first = sorted(set(all_symbols_list_first))
unique_symbols_dict_second = sorted(set(all_symbols_list_second))

unique_from_both = list()
answer_string = str()

for symbol in unique_symbols_dict_first:
    if symbol in unique_symbols_dict_second:
        if symbol in unique_from_both:
            None
        else:
            unique_from_both.append(symbol)
            answer_string += (symbol + ' ')

print(answer_string)