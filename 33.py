import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b * b - 4 * a * c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)

    print("Two real and distinct roots")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root = -b / (2 * a)

    print("Two real and equal roots")
    print("Root =", root)

else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-d) / (2 * a)

    print("Imaginary roots")
    print("Root 1 =", real, "+", imaginary, "i")
    print("Root 2 =", real, "-", imaginary, "i")
