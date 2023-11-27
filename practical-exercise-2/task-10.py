input_string = input()
expected_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '']

input_list = list()

for value in input_string:
    input_list.append(value)

j = 0
finded_values_list = list()
position = int()

for i in range(0, len(input_list)):
    if input_list[i] == expected_list[j]:
        finded_values_list.append(input_list[i])
        j += 1
        position = i + 1

expected_list.pop(len(expected_list)-1)

if finded_values_list == expected_list:
    print(position)
else:
    print('ОШИБКА')
