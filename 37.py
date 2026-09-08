n = int(input("Enter a 3-digit number: "))

if 100 <= n <= 999:
    original = n
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** 3
        n = n // 10

    if sum == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

else:
    print("Please enter a 3-digit number")
