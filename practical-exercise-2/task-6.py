import copy

input_string = input()
input_string = input_string.casefold()

words_list = input_string.split()

words_dict = dict()
letter_set = set()
letters_set = set()
set_list = list()
id_list = list()
answer_list = list()

for word in words_list:
    for letter in word:
        letters_set.add(letter)
    set_list.append(letters_set.copy())
    letters_set.clear()

for i in range(0, len(words_list)):
    for j in range(0, len(words_list)):
        if set_list[i] == set_list[j]:
            id_list.append(i)
            id_list.append(j)
            answer_list.append(id_list.copy())
        id_list.clear()

answer = list()

for couple in answer_list:
    if couple[0] != couple[1]:
        answer.append(couple)

reversed_answer = copy.deepcopy(answer)

a = int()
b = int()

for couple in reversed_answer:
    a = copy.deepcopy(couple[0])
    b = copy.deepcopy(couple[1])
    couple[0] = copy.deepcopy(b)
    couple[1] = copy.deepcopy(a)

finaly_answer = list()

for i in range(len(answer)):
    if reversed_answer[i] not in finaly_answer:
        finaly_answer.append(answer[i])

text_answer = list()
temp_list = list()

for i in range(len(finaly_answer)):
    temp_list.append(words_list[finaly_answer[i][0]])
    temp_list.append(words_list[finaly_answer[i][1]])
    text_answer.append(temp_list.copy())
    temp_list.clear()

for couple in text_answer:
    couple.sort()

text_answer.sort()

for couple in text_answer:
    print(couple[0], couple[1])