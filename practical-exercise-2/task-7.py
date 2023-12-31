inputValue = input()

russianInitials = inputValue.casefold()
englishInitials = str()

lettersTransliteration = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
                         'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
                         'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
                         'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y',
                         'ъ': 'ie', 'э': 'e', 'ю': 'iu', 'я': 'ia', 'ь': '', ' ': ' '}

for letter in russianInitials:
    englishInitials += lettersTransliteration[letter]

print(englishInitials.title())