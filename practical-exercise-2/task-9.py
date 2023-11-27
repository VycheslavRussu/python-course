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
