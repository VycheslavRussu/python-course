# I. Чётность
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# На входе имеется два набора чисел, разделенных пробелами.
#
# Необходимо сформировать два новых набора, первый из которых содержит все нечётные числа из обоих входных наборов, а второй - все чётные. Дублирующиеся элементы оставить, результаты отсортировать в порядке убывания, вывести каждый набор в отдельную строку.
#
# Формат ввода
# 11 29 10 435 53 93 12 90 16
# 16 1 2 778 233 909 134 1457
# Формат вывода
# 1457 909 435 233 93 53 29 11 1
# 778 134 90 16 16 12 10 2

input_string_first = input()
input_string_second = input()

all_values = input_string_first + ' ' + input_string_second

values_list = all_values.split()

for i in range(0, len(values_list)):
    values_list[i] = int(values_list[i])

values_list = sorted(values_list, reverse=True)

even_values = str()
odd_values = str()

for value in values_list:
    if value % 2 == 0:
        even_values += (str(value) + ' ')
    else:
        odd_values += (str(value) + ' ')

print(odd_values)
print(even_values)
