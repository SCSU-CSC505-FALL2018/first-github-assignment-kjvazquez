usernum = input('Enter a number\n')
usernum2 = input ('Enter another number\n')
x = int(usernum)
y = int(usernum2)
str=(' is greater than ')
str2=(' is less than ')
if x > y:
    print((usernum) + str + (usernum2))
elif x < y:
    print((usernum) + str2 + (usernum2))
