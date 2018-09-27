#Four scripts for teaching basic operations.

import random

print('Learn an operation!')
choice = input ("Choose a number:\n 1)add\n 2)subtract\n 3)multiply\n 4)divide?\n")

#Script for addition
if choice == '1':
    for i in range(1):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        print((x), "+", (y), "=", (x+y))
        print('Your answer is correct!')
        
#Script for subtraction
elif choice == '2':
    for i in range(1):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        print((x), "-", (y), "=", (x-y))
        print('Your answer is correct!')
        
#Script for multiplication
elif choice == '3':
    for i in range(1):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        print((x), "*", (y), "=", (x*y))
        print('Your answer is correct!')

#Script for division
elif choice == '4':
    for i in range(1):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        print((x), "/", (y), "=", (x/y))
        print('Your answer is correct!')

