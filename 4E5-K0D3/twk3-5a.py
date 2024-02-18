###################################################
#Lab 3.1 PRG435
#Conrad Brookes
#14 Feb 2024
# GNU
# Press the green button in the gutter to run the script.
####################################################

import sys

val = int(input("enter a number 1 to 30 "))

try:
       if val < 11:
           print('x less than 11')
       elif val > 10 and val < 21:
         print('between 11 and 20')
       elif val > 20:
         print('its greater than 20')
       else:
           print('Not in range')
except ValueError:
           print("That's not an int!")


