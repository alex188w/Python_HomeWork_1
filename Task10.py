# Задача 10.	Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве

x1 = float(input('Введите координату х первой точки: '))
y1 = float(input('Введите координату у первой точки: '))
x2 = float(input('Введите координату х второй точки: '))
y2 = float(input('Введите координату у второй точки: '))
S = (((x2 - x1)**2 + (y2 - y1)**2)**(0.5))
print(f'Расстояние между данными точками в 2D  пространстве составляет: {S:.2f}')