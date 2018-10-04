#Comment This formula is to find you monthly cost on a car loan
def carpayment():
    print('Determine your monthly payments on a car loan!')
    car_value=input('Enter price of vehicle\n')
    p=float(car_value)
    loan_length=input('Enter number of months loan is for\n')
    n=int(loan_length)
    interest_rate=input('Enter interest rate\n')
    r=float(interest_rate)/100
    monthly_payment=(r/12*p)/(1-(1+r/12)**-n)
    print (monthly_payment)
    carpayment()
carpayment()
