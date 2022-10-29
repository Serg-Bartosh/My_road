def tabl(num):
    for i in range(1, num+1, 1):
        for _ in range(1, 6):
            print(f'{i}', end=' ')
        print()


num = int(input())

tabl(num)
