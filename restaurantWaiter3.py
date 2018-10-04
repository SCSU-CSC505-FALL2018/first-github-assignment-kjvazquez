#Script for waiter in a restaurant
import time
print('Welcome to KISS, my name is Joe and I will be your server for today')
yN = input('For starters can I get you something to drink? yes or no\n') #yN is 'yes' or 'no'.
if yN == 'yes':
    print('What would you like?')
    dS = input('hot tea, coca cola, orange juice or cranberry juice?\n') #dS is 'drink select'.
    if dS == 'hot tea' or dS=='coca cola' or dS=='orange juice' or dS=='cranberry juice':
        print('okay, I will be right back\n')
        time.sleep(5)
        print('okay, here is your drink.')
        time.sleep(2)
        yN= input('Are you ready to order? yes or no\n')
        
        if yN == 'yes':
            print('For our menu, we have...')
            mS = input('spaghetti and meatballs, pork tacos, pizza, hot dogs, and cheeseburgers. Which would you like?\n')#mS is 'menu select'
            
            if mS == 'spaghetti and meatballs' or mS=='pork tacos' or mS=='pizza' or mS=='hot dogs' or mS=='cheeseburgers':
                print('Okay, I will be right back with your order.\n')
                time.sleep(5)
                print('Here you are, enjoy!')
                time.sleep(3)
                print('I hope you enjoyed your meal today, here is your bill. I will reutrn in just a moment...')
                time.sleep(3)
                print('Thank you very much, I will return with your receipt.')
                time.sleep(3)
                print('Here you are, thank you for joining us today and I hope you have a wonderful rest of the day.')
                
        elif yN == 'no':
            print('Okay, I will give you some more time to look at our menu.')
            time.sleep(5)
            yN = input('Are you ready? yes or no')
            if yN == 'yes':
                print('For our menu, we have...')
                mS = input('spaghetti and meatballs, pork tacos, pizza, hot dogs, and cheeseburgers. Which would you like?\n')
                if mS == 'spaghetti and meatballs' or mS=='pork tacos' or mS=='pizza' or mS=='hot dogs' or mS=='cheeseburgers':
                    print('Okay, I will be right back with your order.\n')
                    time.sleep(5)
                    print('Here you are, enjoy!')
                    time.sleep(3)
                    print('I hope you enjoyed your meal today, here is your bill. I will reutrn in just a moment...')
                    time.sleep(3)
                    print('Thank you very much, I will return with your receipt.')
                    time.sleep(3)
                    print('Here you are, thank you for joining us today and I hope you have a wonderful rest of the day.')
                 
elif yN == 'no':
    yN= input('Are you ready to order? yes or no\n')
    
    if yN == 'yes':
        print('For our menu, we have...')
        mS = input('spaghetti and meatballs, pork tacos, pizza, hot dogs, and cheeseburgers. Which would you like?\n')
        
        if mS == 'spaghetti and meatballs' or mS=='pork tacos' or mS=='pizza' or mS=='hot dogs' or mS=='cheeseburgers':
            print('Okay, I will be right back with your order.\n')
            time.sleep(5)
            print('Here you are, enjoy!')
            time.sleep(3)
            print('I hope you enjoyed your meal today, here is your bill. I will reutrn in just a moment...')
            time.sleep(3)
            print('Thank you very much, I will return with your receipt.')
            time.sleep(3)
            print('Here you are, thank you for joining us today and I hope you have a wonderful rest of the day.')
            
    elif yN == 'no':
        print('Okay, I will give you some more time to look at our menu')
        time.sleep(5)
        yN = input('Are you ready? yes or no')
        
        if yN == 'yes':
            print('For our menu, we have...')
            mS = input('spaghetti and meatballs, pork tacos, pizza, hot dogs, and cheeseburgers. Which would you like?\n')
            
            if mS == 'spaghetti and meatballs' or mS=='pork tacos' or mS=='pizza' or mS=='hot dogs' or mS=='cheeseburgers':
                print('Okay, I will be right back with your order.\n')
                time.sleep(5)
                print('Here you are, enjoy!')
                time.sleep(3)
                print('I hope you enjoyed your meal today, here is your bill. I will reutrn in just a moment...')
                time.sleep(3)
                print('Thank you very much, I will return with your receipt.')
                time.sleep(3)
                print('Here you are, thank you for joining us today and I hope you have a wonderful rest of the day.')
            
