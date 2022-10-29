def dividers(border_1, border_2):
    summ_count = 0
    max_i = 0
    for i in range(border_1, border_2 + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += j
            if count >= summ_count:
                summ_count = count
                max_i = i
    print(max_i, summ_count)


border_1, border_2 = map(int, input().split())
dividers(border_1, border_2)

#На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу,
# которая находит натуральное число из отрезка [a; \, b][a;b] с максимальной суммой делителей.
