def tabl(num):
    for i in range(1, num+1, 1):
        for j in range(1, 10):
            print(f'{i} + {j} = {i+j}')
        print()


num = int(input())

tabl(num)
