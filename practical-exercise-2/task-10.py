input_string = input()
expected_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

input_list = list()
position = int()

for value in input_string:
    input_list.append(value)

for i in range(0, len(input_list)):
    if input_list[i] in expected_set:
        position = i + 1
        expected_set.remove(input_list[i])

if len(expected_set) == 0:
    print(position)
else:
    print('ОШИБКА')
