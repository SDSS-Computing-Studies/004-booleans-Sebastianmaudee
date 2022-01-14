#! python3 

"""
Have the user enter a number. 
Use an if...elif statement to determine if the number is 
a) larger than 1000 
b) larger than 100 
c) larger than 10 
d) larger than 0 
Output must match one of the valid output statements listed
(2 points)

Inputs:
a number

Output is a single number that represents a range of numbers:
"3" : The number is equal to 1000 or is larger than 1000
"2" : The number is 100 or a number up to 1000 
"1" : The number is 10 or a number up to 100 
"0" : The number is 0 or a number up to 100 

Example:
Enter a number: 3
0

Enter a number: 212
2

Enter a number: 10000
3


"""

x = input("Enter number")
x = float(x)
if x > 1000 or x ==1000:
    print("The number is or is larger than 1000")
else:
    if x > 100 or x == 100:
        print("The number is or is larger than 100")
    else:
        if x > 10 or x == 10:
            print("The number is or is larger than 10")
        else:
            if x > 0 or x == 0:
                print("The number is 0 or a number up to 10")