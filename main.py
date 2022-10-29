def numerical_triangle(num):
    for i in range(1,num+1,1):
        print(f'{i}'*i, end='\n')


num = int(input())

numerical_triangle(num)

#Дано натуральное число nn. Напишите программу,
# которая печатает численный треугольник в соответствии с примером:
# 1
# 22
# 333
# 4444
# 55555
