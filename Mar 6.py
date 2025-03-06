# Ввод: haystack = "sadbutsad", needle = "sad" Вывод: 0 Пояснение: Строка needle = "sad"
# входит в строку haystack = "sadbutsad" дважды - в индексах 0 и 6.
# Первое вхождение в индексе 0, поэтому возвращаем 0. Ограничения: Нельзя использовать .index().
# Задача в том и состоит, чтобы его написать

haystack = input()
needle = input()

for i in range(0, len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle):1] == needle:
        print(i, end=' ')
