
# 3.1 Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay. Pay the hourly rate
# for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# #You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.





hrs = float(input("Enter Hours: "))
ot = float(1.5)
rate = float(input("enter rate "))
overtime = float(15.5)
hrsOt = float(0)
pay = float(0)

try:
 if hrs < 41:
        hrs = hrs * rate
        print('enter hours ', hrs)
 elif hrs > 40:
        hrsOt = hrs - 40
        pay = (40 * rate) + (hrsOt * 1.5)
        print(pay)

except ValueError:
        print("there was an error ")
