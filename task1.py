#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""
x = input("ENTER A NUMBER")
x = int(x)
if x > 100:
    print("Number is great than 100")
else:
    if x == 100:
        print("Nuber is 100")
    else:
        if x < 100:
            print("number small than 100")