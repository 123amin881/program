n = int(input("Enter a number: "))
k = int(input("Enter K (starting from 0): "))

if n & (1 << k):
    print("Kth bit is set")
else:
    print("Kth bit is not set")