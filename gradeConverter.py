userNbr=input('Enter a number grade between 0 and 100\n')
x=int(userNbr)
if x >=90:
    print('A')
elif x >=80 and x<=90:
    print('B')
elif x >=70 and x<=80:
    print('C')
elif x >=60 and x<=70:
    print ('D')
elif x >=50 and x<=60:
    print('E')
elif x < 50:
    print ('F')
