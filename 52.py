n = int(input("Enter a number: "))

original = n

while n != 1 and n != 4:
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** 2
        n = n // 10

    n = sum

if n == 1:
    print(original, "is a Happy Number")
else:
    print(original, "is not a Happy Number")
