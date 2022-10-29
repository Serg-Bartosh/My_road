def tabl(num):
    for _ in range(1, num+1, 1):
        for _ in range(3):
            print(f'{num}', end=' ')
        print()


num = int(input())

tabl(num)