def do_twice(f):
    f()
    f()

def print_spam():
    print ('spam')
    
do_twice(print_spam)

def do_four(f):
    do_twice(print_spam)
    do_twice(print_spam)

do_four(print_spam)
