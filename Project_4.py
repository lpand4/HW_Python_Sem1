# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

coordinate = int(input("Введите номер четверти: "))
while coordinate < 0 or coordinate > 4:
    coordinate = int(input("Четвертей всего 4! Введите номер четверти: "))
if coordinate == 1:
    print("x > 0 и y > 0")
elif coordinate == 2:
    print("x < 0 и y > 0")
elif coordinate == 3:
    print("x < 0 и y < 0")
else:
    print("x > 0 и y <>> 0")
