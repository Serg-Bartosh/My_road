def dividers2(border):
    for i in range(1, border+1, 1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        print(f'{i}{count * "+"}')



border = int(input())
dividers2(border)

#На вход программе подается натуральное число nn. Напишите программу,
# выводящую графическое изображение делимости чисел от 11 до nn включительно.
# В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.
