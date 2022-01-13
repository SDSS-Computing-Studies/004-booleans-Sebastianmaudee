#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
import math
a = input("enter first side length")
b = input("enter second side length")
c = input("enter third side length")

list1 = [a,b,c]


list1 = sorted(list1)

d = (list1[2])
e = (list1[1])
f = (list1[0])

d = int(d)
e = int(e)
f = int(f)


g = (e ** 2) + (f ** 2)

h = d ** 2

z = h + g


if g == h:
    print("this is a right angle triangle")
else:
    print("that is an obtuse")