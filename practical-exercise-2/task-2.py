inputValue = input()
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