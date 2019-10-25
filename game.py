import time # import time module
import random # import random module

input("Welcome to Python-Game by Tyler Wolf\n Please input anything to begin")

print("\nLet's dive right into Python, we will do that with starting with\nthe basics, math. Math in Python is very simple.\n You just type the expression as you would,\nx+y (add two operands), x-y (subtract right operand from left),\n x*y (multiply two operands), x/y (divide left operand by right operand to result in float)\nx%y (modulus operation/remainder of x/y), x//y (floor division) and x**y (x raised to the power of y.)\n")
time.sleep(10) # wait 10 seconds
q1 = str(input("Now you try, try multiplying 5 and 10\n"))

a1 = '5*10' or '5 * 10' or '10*5' or '10 * 5'

if q1 == a1:
    print("10\nYou have succesfully multiplied 5 and 10 using Python.")
else:
    pass
while q1 != a1:
    q1 = str(input("You have guessed incorrectly, try again.\n"))
    if q1 == a1:
        print("10\nYou have sucessfully multiplied 5 and 10 using python.")
q2 == str(input("Next, we will go over assigning variables. This means using terms to represent\nvalues. For example, you can assign the value of 10 to number using 'number = 10'.\nFor this exercise create the variable 'x' and assign the value 1 to it."))
a2 == 'x=1' or 'x = 1'

if q2 == a2:
    print("You have succesfully assigned the value '1' to the variable 'x'.\nNext, try and call the variable to see it's value, simply just run the variable by entering the command 'x'.")
else:
    pass
while q2 != a2:
    q2 = str(input("You have guessed incorrectly, try again.\n"))
    if q2 == a2:
        q3 = str(input("You have sucessfully assigned the value '1' to the variable 'x'.\nNext, try and call the variable to see it's value, simply just run the variable by entering the command 'x'."))
if q3 == 'x':
    print('1')
else:
    pass
while q3 != 'x\nYou have successfully printed out the value of x':
    q3 = str(input("You have guessed incorrectly, try again.\n"))
    if q3 == a3:
        q3 = str(input("1\nYou have successfully printed out the value of variable 'x'."))
