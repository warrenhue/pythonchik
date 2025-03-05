biologists = int(input())
programmers = int(input())

for cake_pieces in range(max(biologists, programmers), biologists*programmers+1):
    if cake_pieces % biologists == 0 and cake_pieces % programmers == 0:
        print(cake_pieces)
        break