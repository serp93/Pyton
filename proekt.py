# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input("введите число: "))
if 6<=a<=7:
    print("yes")
else:
    print("no")

# 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("введите число X: "))
y = int(input("введите число Y: "))
z = int(input("введите число Z: "))
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            print(not(x or y or z) == (not(x) and not(y) and not(z)))

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input("введите X: "))
y = int(input("введите Y: "))
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)

# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

qrtr = int(input('Enter quarter: '))
while qrtr < 1 or qrtr > 4:
    qrtr = int(input('ошибка'))
if qrtr == 1:
    print('X > 0 - (+∞); Y > 0 - (+∞)')
elif qrtr == 2:
    print('X < 0 - (-∞); Y > 0 - (+∞)')
elif qrtr == 3:
    print('X < 0 - (-∞); Y < 0 - (-∞)')
else:
    print(('X > 0 - (+∞); Y < 0 - (-∞)'))

# 5. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

import math

x1 = float(input("введите X1: "))
y1 = float(input("введите Y1: "))
x2 = float(input("введите X2: "))
y2 = float(input("введите Y2: "))
result = math.sqrt(((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)))
print(round(result, 3))

