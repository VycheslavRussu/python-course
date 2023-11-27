import re

inputValue = input()

letterCounter = len(re.findall(r'[a-zA-Zа-яА-ЯёЁ]', inputValue))
digitCounter = len(re.findall(r'\d', inputValue))
symbolCounter = len(re.findall(r'(\W|[_])', inputValue))

print(letterCounter, digitCounter, symbolCounter, sep='\n')