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