def is_palindrome(a):
    return a == a[::-1]
print("is it a Palindrome?? - (type quit to exit)")
a = ""
b = ""
while True
    print()
    a = input("Please enter a word: ")
    b = is_palindrome(a)

if b and a != "":
    print()
    print(a.upper()+ "is palindrome.")
if not b:
    print()
    print(a.upper()+ "is not palindrome.")
if a == "quit":
    break
print("good bye.")

