#
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Написать программу для транслитерации фамилии, имени, отчества для загранпаспорта по установленным МВД РФ требованиям:
#
# А (а) -> A (a)   Ж (ж) -> Zh (zh)    Н (н) -> N (n)   Ф (ф) -> F (f)        Ъ (ъ) -> Ie (ie)
# Б (б) -> B (b)   З (з) -> Z (z)      О (о) -> O (o)   Х (х) -> Kh (kh)      Э (э) -> E (e)
# В (в) -> V (v)   И (и) -> I (i)      П (п) -> P (p)   Ц (ц) -> Ts (ts)      Ю (ю) -> Iu (iu)
# Г (г) -> G (g)   Й (й) -> I (i)      Р (р) -> R (r)   Ч (ч) -> Ch (ch)      Я (я) -> Ia (ia)
# Д (д) -> D (d)   К (к) -> K (k)      С (с) -> S (s)   Ш (ш) -> Sh (sh)      ь     -> не пишется
# Е (е) -> E (e)   Л (л) -> L (l)      Т (т) -> T (t)   Щ (щ) -> Shch (shch)
# Ё (ё) -> E (e)   М (м) -> M (m)      У (у) -> U (u)   Ы (ы) -> Y (y)
# Формат ввода
# Иванов Иван Иванович
#
# Формат вывода
# Ivanov Ivan Ivanovich

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