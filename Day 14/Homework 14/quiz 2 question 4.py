# ra capormatdeba tu shevitant 13s da 20s da 7s

number1 = int(input("enter number 1 : "))
number2 = int(input("enter number 2 : "))
number3 = int(input("enter number 3 : "))



my_odds = 0

if number1 % 2 == 1:
    my_odds += number1
if number2 % 2 == 1:
    my_odds += number2
if number3 % 2 == 1:
    my_odds += number3

print("the output of the odd numbers is []".format(my_odds))