#Write a program to prompt for a sc
# between 0.0 and 1.0. If the sc
# is out of range, print an error.
#If the sc is between 0.0 and 1.0,
# print a grade using the following table:
#sc Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a sc of 0.85.

s = input("Enter sc: ")
sc = float(s)
if sc <= 1.0 :
    if sc >= 0.9 :
        print("A")
    elif sc >= 0.8 :
        print("B")
    elif sc >= 0.7 :
        print("C")
    elif sc >= 0.6 :
        print("D")
    elif sc < 0.6 :
        print("F")
else :
    print("Error, please enter number within range 0.0 and 1.0")