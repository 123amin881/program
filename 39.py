balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

minimum_balance = 500

if amount <= 0:
    print("Rejected: Invalid withdrawal amount")

elif amount > balance:
    print("Rejected: Insufficient balance")

elif balance - amount < minimum_balance:
    print("Rejected: Minimum balance must be maintained")

else:
    balance = balance - amount
    print("Withdrawal Approved")
    print("Remaining Balance =", balance)
