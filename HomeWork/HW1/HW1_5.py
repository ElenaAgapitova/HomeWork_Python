# Задача 5. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.

x1, y1 = map(int, input('Введите координаты точки А через пробел: ').split())
x2, y2 = map(int, input('Введите координаты точки B через пробел: ').split())

AB = ((x2 - x1) ** 2 + (y2 - y1)**2)**0.5
print(f'A({x1},{y1}); B({x2},{y2}) -> растояние между точками = {round(AB, 2)}')
