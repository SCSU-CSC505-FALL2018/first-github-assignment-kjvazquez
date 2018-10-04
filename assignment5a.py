#Four scripts for teaching basic operations.
import time
import random
    
def operations():
    print('Learn an operation!')
    operation = input("Choose a number: 1)add, 2)subtract, 3)multiply, 4)divide, 5)random?\n")
#Add Operation
    if operation == 'add' or operation == '1':
        while True:
            a = random.randint(0, 10)#Random numbers between 0 and 10
            b = random.randint(0, 10)
            while True:
                print((a), "+", (b), "=", 'x')
                x = int(input())#user will type answer to problem
                if x == a + b:
                     print('correct')
                     time.sleep(1)
                     break       
                elif x != a + b:
                    print('Wrong!')
                    time.sleep(1)
                    while x != a + b:
                        y = input('Try again?\nyes or no\n')#Prompted to return to main menu if 'no'
                        if y == 'yes':
                            break
                        elif y == 'no':
                            operations()#Return to main menu
#Subtract Operation                            
    elif operation == 'subtract' or operation == '2':
        while True:
            a = random.randint(0, 10)#Random numbers between 0 and 10
            b = random.randint(0, 10)
            while True:
                print((a), "-", (b), "=", 'x')
                x = int(input())#user will type answer to problem
                if x == a - b:
                     print('correct')
                     time.sleep(1)
                     break
                     
                elif x != a - b:
                    print('Wrong!')
                    time.sleep(1)
                    while x != a - b:
                        y = input('Try again?\nyes or no\n')#promted to return to main menu if 'no'
                        if y == 'yes':
                            break
                        elif y == 'no':
                            operations()#Return to main menu
#Multiply Operation
    elif operation == 'multiply' or operation == '3':
        while True:
            a = random.randint(0, 10)#random numbers between 0 and 10
            b = random.randint(0, 10)
            while True:
                print((a), "*", (b), "=", 'x')
                x = int(input())#user will type answer to problem
                if x == a * b:
                     print('correct')
                     time.sleep(1)
                     break
                elif x != a * b:
                    print('Wrong!')
                    time.sleep(1)
                    while x != a * b:
                        y = input('Try again?\nyes or no\n')#promted to return to main menu if 'no'
                        if y == 'yes':
                            break
                        elif y == 'no':
                            operations()#Return to main menu
#Divide Operation
    elif operation == 'divide' or operation == '4':
        while True:
            a = random.randint(1, 10)#Random numbers between 1 and 10
            b = random.randint(1, 10)
            while True:
                print((a), "/", (b), "=", 'x')
                x = float(input())##user will type answer to problem and allow for decimals
                if x == a / b:
                     print('correct')
                     time.sleep(1)
                     break
                elif x != a / b:
                    print('Wrong!')
                    time.sleep(1)
                    while x != a / b:
                        y = input('Try again?\nyes or no\n')#promted to return to main menu if 'no'
                        if y == 'yes':
                            break
                        elif y == 'no':
                            operations()#Return to main menu
#Unable to program random script.                            
    elif operation == 'random' or '5':
        addition()
