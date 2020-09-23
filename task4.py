#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704

import math

print("We're looking for the hypotenuse")

print("Enter side 1 ")
s1 = input()

print("Enter side 2 ")
s2 = input()

s1 = float(s1)
s2 = float(s2)

s3 = s1**2 + s2**2
s3 = math.sqrt(s3)

print("The hypotenuse = " ,end="")
print(s3)
