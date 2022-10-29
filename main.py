def star_triangle(num):
    for i in range(1, num // 2 + 2):
        print('*' * i, end='')
        print()
    for i in range(num // 2, 0, -1):
        print('*' * i, end='')
        print()


num = int(input())

star_triangle(num)

#Звездный треугольник .
# Дано нечетное натуральное число nn. Напишите программу,
# которая печатает равнобедренный звездный треугольник с основанием,
# равным nn в соответствии с примером:
