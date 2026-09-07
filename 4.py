choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

temp = float(input("Enter temperature: "))

if choice == 'C' or choice == 'c':
    fahrenheit = (temp * 9 / 5) + 32
    print("Fahrenheit =", fahrenheit)

elif choice == 'F' or choice == 'f':
    celsius = (temp - 32) * 5 / 9
    print("Celsius =", celsius)

else:
    print("Invalid choice")