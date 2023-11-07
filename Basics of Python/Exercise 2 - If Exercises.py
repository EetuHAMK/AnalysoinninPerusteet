# 1:

number1 = 5
number2 = 10

if number1 == number2:
    print("Number1 is equal to Number2.")

if number1 > number2:
    print("Number1 is greater than Number2.")

if number1 >= number2:
    print("Number1 is greater or equal to Number2.")

if number1 != number2:
    print("Number1 is NOT equal to Number2.")

# 2:

number1 = 5
number2 = 10
number3 = 15

if number1 == number2 == number3:
    print("All numbers are equal.")

if number1 == number2 or number2 == number3:
    print("Either number1 & number2, or number2 & number3 are equal.")

if number1 > number2 and number3:
    print("Number1 is greater than number2 & number3.")

if number1 > number2:
    print("Number1 is greater than Number2.")
elif number2 > number3:
    print("Number2 is greater than Number3.")

if number1 == number2:
    print("Number1 and Number2 are equal.")
elif number1 > number3:
    print("Number1 is greater than Number3.")

# 3:

name1 = "Eetu"
name2 = "Jani"
name3 = "Eeni"

if name1 == name2:
    print("Names are equal.")

if name1 != name2:
    print("Names are NOT equal.")

if name1 == name2:
    print("Names 1 & 2 are equal.")
elif name1 == name3:
    print("Names 1 & 3 are equal.")
    