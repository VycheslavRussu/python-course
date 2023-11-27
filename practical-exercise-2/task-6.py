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