#Converter
import time
def openConverter():
    while True:
#User enters number that corresponds with converter they wish to use.
        choice = int(input('1. Binary to Hexadecimal\n'
                           '2. Hexadecimal to Binary\n'
                           '3. Decimal to Binary\n'
                           '4. Binary to Decimal\n'
                           '5. Hexadecimal to Decimal\n'
                           '6. Decimal to Hexadecimal\n'
                           'Enter the number to run converter: '))
#Binary to Hexadecimal
        if choice == 1:
            binum = input("Enter a number in Binary: ")
            newNbr = int(binum, 2)
            print('The hexadecimlal is')
            print(hex(newNbr))
            time.sleep(3) 
#Hexadecimal to Binary
        elif choice == 2:
            hexDec = input("Enter any number in Hexadecimal: ")
            decNum = int(hexDec, 16)
            print('The binary number is')
            print(bin(decNum))
            time.sleep(3)
#Decimal to Binary
        elif choice == 3:
            def dec2Bi(a):
                if a > 1:
                   dec2Bi(a//2)
                   print(a % 2,end = '')
            decNum = int(input('Enter a posotive number: '))
            print('The binary number is')

            dec2Bi(decNum)
            time.sleep(3)
#Binary to Decimal
        elif choice == 4:
            userInt=input("Enter a binary number: ")
            numA=userInt
            power=0
            newNbr=0
            while len(numA)>0:
                bit=int(numA[-1])
                newNbr=newNbr+bit*2**power
                power+=1
                numA=numA[:-1]
            print('The deimcal number is')
            print(newNbr)
            time.sleep(3)
#Hexadecimal to Decimal
        elif choice == 5:
                hexdec = input("Enter a Hexadecimal to be converted to decimal: ")
                dec = int(hexdec, 16)
                print('The decimal number is')
                print(str(dec))
                time.sleep(3)
#Decimal to Hexadecimal
        elif choice == 6:
            def dec2Hex():
                decnum = int(input("Enter a decimal number to be converted to hexadecimal: "))
                hexadecimal = ""
                while decnum != 0:
                    remainder = convert(decnum % 16)
                    hexadecimal = str(remainder) + hexadecimal
                    decnum = int(decnum / 16)
                print('The hexadecimal is')
                print(hexadecimal)
                time.sleep(3)
            def convert(numA):
                decimal =     [10 , 11 , 12 , 13 , 14 , 15 ]
                hexadecimal = ["A", "B", "C", "D", "E", "F"]
                for counter in range(7):
                    if numA == decimal[counter - 1]:
                        numA = hexadecimal[counter - 1]
                return numA

            dec2Hex()

        
