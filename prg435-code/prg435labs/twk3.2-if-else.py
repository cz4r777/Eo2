###################################################
#Lab 3.2 PRG435
#Conrad Brookes
#14 Feb 2024
# GNU
# exception grabbing
####################################################

x = int(input("enter a number for x: "))
y = int(input("enter a number for y: "))

try:
    if x < y:
        print('x less than y')
    elif x > y:
        print('x greater than y')
    else:
        print('they are equal')
except Exception as err:
        print('error out put uses except', err)


