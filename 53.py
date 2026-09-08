def product_digits(n):
    if n == 0:
        return 1
    else:
        return (n % 10) * product_digits(n // 10)


n = int(input("Enter a number: "))

if n == 0:
    product = 0
else:
    product = product_digits(abs(n))

print("Product of digits =", product)
