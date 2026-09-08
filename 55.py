n = int(input("Enter a number: "))

divisor = 1
temp = n

while temp >= 10:
    temp = temp // 10
    divisor = divisor * 10

while divisor > 0:
    digit = n // divisor
    print(digit)

    n = n % divisor
    divisor = divisor // 10
