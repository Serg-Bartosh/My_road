def get_number_triangle_4(num):
    for i in range(1, num+1, 1):
        for j in range(i):
            print(j+1, end='')
        for k in range(i-1, 0, -1):
            print(k, end='')
        print()


num = int(input())
get_number_triangle_4(num)

#Дано натуральное число nn.
# Напишите программу, которая печатает численный треугольник с высотой равной n,
# в соответствии с примером:
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4 5 6 5 4 3 2 1
# ...