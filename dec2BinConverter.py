#Comment Decimal to Binary Conversion
def dec2BinConverter():
    userInt=input("Enter a number\n")
    newNbr=int(userInt)
    binStr=""
    while newNbr>0:
        binStr=str(newNbr%2)+binStr
        newNbr=newNbr//2
    print("The binary number is:",binStr)
#Comment Binary to Decimal Conversion
    userInt=input("Enter a binary number:\n")
    temp=userInt
    power=0
    number=0
    while len(temp)>0:
        bit=int(temp[-1])
        number=number+bit*2**power
        power+=1
        temp=temp[:-1]
    print("The number is:",number)
    dec2BinConverter()
dec2BinConverter()
