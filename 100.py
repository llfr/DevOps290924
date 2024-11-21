import datetime
#after creating mydep file we can now call its function 
# import mydep
# import my_other_dep
# mydep.test()
# my_other_dep.test()
#another option to call the function is to specify its fuction name "as" alias
from mydep import test as my_test
from my_other_dep import test as my_other_test

my_test()
my_other_test()

def wait_for_print():
    from time import sleep
    sleep(3)
    print("Hello world")

print(datetime.datetime.now())

wait_for_print()