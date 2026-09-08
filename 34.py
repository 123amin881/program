ch = input("Enter a character: ")

if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print("Alphabet")

elif '0' <= ch <= '9':
    print("Digit")

else:
    print("Special character")
