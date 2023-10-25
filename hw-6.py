# less 1

number = int(input('Введите количество чисел: '))
count = 0

for i in range(number):
    second_number = int(input('Введите целое число: '))
    if second_number % 2 == 0:
        count += 1

print(count)

# less 2

number = int(input('Натуральное число: '))
count = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        count += 1
        print(i)

print()
print(f'Всего: {count}')

# less 3

a = int(input('A: '))
b = int(input('B: '))

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')