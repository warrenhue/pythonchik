# Ввод: haystack = "sadbutsad", needle = "sad" Вывод: 0 Пояснение: Строка needle = "sad"
# входит в строку haystack = "sadbutsad" дважды - в индексах 0 и 6.
# Первое вхождение в индексе 0, поэтому возвращаем 0. Ограничения: Нельзя использовать .index().
# Задача в том и состоит, чтобы его написать

def haystacks (haystack, needle):
    for i in range(0, len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle):1] == needle:
            print(i, end=' ')
#
# Дана строка s, состоящая из слов и пробелов, верните длину последнего слова в строке.
#
# Слово - это максимальная подстрока, состоящая только из символов, не являющихся пробелами.
def no_spaces_count(word):
    letter_count = 0
    caught_space = False
    for letter in word:
        if caught_space: #Проверка, если предыдущий символ - пробел
            letter_count = 0
            if letter != ' ': #Считаем нынешнюю букву, если предыдущий символ пррбел
                letter_count += 1
                caught_space = False
            else:
                caught_space = True #Если нынешний символ тоже пробел
        else:
            if letter != ' ':
                letter_count += 1
                caught_space = False
            else:
                caught_space = True #Нынешний символ - пробел
    return letter_count

print(no_spaces_count(input()))