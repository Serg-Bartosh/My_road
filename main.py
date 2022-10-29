def get_number_triangle_3(num):
    total = 0
    for i in range(1, num+1, 1):
        for j in range(1, i+1):
            total += 1
            print(f'{total}', end=' ')
        print()


num = int(input())
get_number_triangle_3(num)

#Дано натуральное число nn.
# Напишите программу, которая печатает численный треугольник с высотой равной nn,
# в соответствии с примером:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...