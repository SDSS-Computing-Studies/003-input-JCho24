#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

print("The equation ax + b = c is a two step algebra equation")
print("You can input numbers into a, b, and c to find out what x =")

print("Enter value for a")
a = input()

print("Enter value for b")
b = input()

print("Enter value for c")
c = input()

print("Your equation is setup as " + a + "x + " + b + " = " + c)

a = float(a)
b = float(b)
c = float(c)

equation = (c-b)/a
equation = float(equation)

print("Therefore x = " ,end="")
print(equation)

