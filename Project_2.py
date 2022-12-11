# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = False
y = False
z = False
print(f"1. {x} {y} {z}")
print(f"Answer is {not (x and y and z) == (not x or not y or not z)}")
x = False
y = False
z = True
print(f"2. {x} {y} {z}")
print(f"Answer is {not (x and y and z) == (not x or not y or not z)}")
x = False
y = True
z = False
print(f"3. {x} {y} {z}")
print(f"Answer is {not (x and y and z) == (not x or not y or not z)}")
x = False
y = True
z = True
print(f"4. {x} {y} {z}")
print(f"Answer is {not (x and y and z) == (not x or not y or not z)}")
x = True
y = False
z = False
print(f"5. {x} {y} {z}")
print(f"Answer is {not (x and y and z) == (not x or not y or not z)}")
x = True
y = False
z = True
print(f"6. {x} {y} {z}")
print(f"Answer is {not (x and y and z) == (not x or not y or not z)}")
x = True
y = True
z = False
print(f"7. {x} {y} {z}")
print(f"Answer is {not (x and y and z) == (not x or not y or not z)}")
x = True
y = True
z = True
print(f"8. {x} {y} {z}")
print(f"Answer is {not (x and y and z) == (not x or not y or not z)}")