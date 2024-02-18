## Debugger example

# Import random stuff
import random

# Variables
family = ['Stan','Hayley','Francine','Steve','Roger','Klaus']
a_random_number = random.randrange(0,5)

# Remove someone
del family[a_random_number]
print("Done!")
