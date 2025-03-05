dna_code = str(input())
shortener = dict()

for letter in dna_code:
    if letter not in shortener.keys():
        shortener[letter] = 0

for letter in dna_code:
    shortener[letter] += 1

for letter in shortener.keys():
    print(f'{letter}{shortener[letter]}', end='')