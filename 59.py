a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    greater = a
else:
    greater = b

while True:
    if greater % a == 0 and greater % b == 0:
        lcm = greater
        break

    greater = greater + 1

print("LCM =", lcm)
