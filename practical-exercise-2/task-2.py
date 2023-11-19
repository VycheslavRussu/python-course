# Сжатие строки
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt

# Написать программу для сжатия строки, в которой алгоритм работает следующим образом:
#
# 'xxxxtttсyyaaa'
#
# преобразуется в
#
# 'x4t3с1y2a3',
#
# то есть последовательность одинаковых символов строки заменяется на этот символ и количество его повторений в текущей позиции строки.
#
# Формат ввода
# pppppuuueeattt
#
# Формат вывода
# p5u3e2a1t3


inputValue = 'pppppuuueeattt'
letterCounter = 1
answerString = str()

for i in range(1, len(inputValue)):
    if inputValue[i] == inputValue[i-1]:
        letterCounter += 1
    else:
        answerString += inputValue[i-1]
        answerString += str(letterCounter)
        letterCounter = 1

answerString += inputValue[-1]
answerString += str(letterCounter)

print(answerString)