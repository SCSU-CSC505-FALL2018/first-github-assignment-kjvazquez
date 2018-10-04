#Script for waiter in a restaurant
import time
def startOrder():
    print('Welcome to KISS, my name is Joe and I will be your server for today')
    while True:
        drinkYN = input('Can I get you something to drink? yes or no\n')# drinkYN is 'yes' or 'no'.
        while drinkYN == 'yes' or 'no':
            if drinkYN == 'yes':
                while True:
                    print('What would you like?\n')
                    dS = input('hot tea: $2.50\n'# dS is 'drink select'
                               'coca cola: $2.00\n'
                               'orange juice: $2.00\n'
                               'or cranberry juice: $2.00?\n')
                    if dS == 'hot tea' or dS == 'coca cola' or dS == 'orange juice' or dS == 'cranberry juice':
                        print('okay, I will be right back\n')
                        time.sleep(5)
                        print('okay, here is your drink.')
                        time.sleep(2)
                        while True:
                            orderYN= input('Are you ready to order? yes or no\n')# orderYN is 'yes' or 'no'.
                            if orderYN == 'yes':
                                print('For our menu, we have...\n')
                                mS = input('spaghetti and meatballs: $8.99\n'# mS is 'menu select'
                                           'pork tacos: $5.99\n'
                                           'pizza: $11.00\n'
                                           'hot dogs: $9.50\n'
                                           'and cheeseburgers: $7.50\n'
                                           'Which would you like?\n')
                                if mS == 'spaghetti and meatballs' or mS=='pork tacos' or mS=='pizza' or mS=='hot dogs' or mS=='cheeseburgers':
                                    print('Okay, I will be right back with your order.\n')
                                    time.sleep(5)
                                    print('Here you are, enjoy!')
                                    time.sleep(3)
                                    print('I hope you enjoyed your meal today\n'
                                          'here is your bill. I will reutrn in\n'
                                          'just a moment...')
                                    time.sleep(3)
                                    print('Thank you very much, I will return with\n'
                                          'your receipt.')
                                    time.sleep(3)
                                    print('Here you are, thank you for joining us\n'
                                          'today and I hope you have a wonderful\n'
                                          'rest of the day.')
                                    return
                                else:
                                    print("I'm sorry, I didn't get that...")
                                    time.sleep(2)
                            elif orderYN == 'no':
                                print('Okay, I will give you some more time to look at our menu.')
                                time.sleep(5)
                            else:
                                print("I'm sorry, I didn't get that...")
                                time.sleep(2)
                        else:
                            print("I'm sorry, I didnt get that...")
                            time.sleep(2)
                    else:
                        print("Sorry, I didn't get that...")
                        time.sleep(2)
                        break
                        continue
                else:
                    print("Sorry, I didn't get that...")
                    time.sleep(2)
            elif drinkYN == 'no':
                while True:   
                    yN = input('Are you ready to order? yes or no\n')
                    if yN == 'yes':
                        print('For our menu, we have...')
                        while True:
                            mS = input('spaghetti and meatballs: $8.99\n'# mS is 'menu select'
                                       'pork tacos: $5.99\n'
                                       'pizza: $11.00\n'
                                       'hot dogs: $9.50\n'
                                        'and cheeseburgers: $7.50\n'
                                       'Which would you like?\n')
                            if mS == 'spaghetti and meatballs' or mS=='pork tacos' or mS=='pizza' or mS=='hot dogs' or mS=='cheeseburgers':
                                print('Okay, I will be right back with your order.\n')
                                time.sleep(5)
                                print('Here you are, enjoy!')
                                time.sleep(3)
                                print('I hope you enjoyed your meal today\n'
                                      'here is your bill. I will reutrn in\n'
                                      'just a moment...')
                                time.sleep(3)
                                print('Thank you very much, I will return with\n'
                                      'your receipt.')
                                time.sleep(3)
                                print('Here you are, thank you for joining us\n'
                                      'today and I hope you have a wonderful\n'
                                      'rest of the day.')
                                return
                            else:
                                print("I'm sorry, I didn't get that...")
                                time.sleep(2)
                    elif yN == 'no':
                        print('Okay, I will give you some more time to look at our menu.')
                        time.sleep(5)
                    else:
                        print("I'm sorry, I didn't ge that...")
                        time.sleep(2)
            else:
                print("Sorry, I didn't get that...")
                time.sleep(2)
                break
