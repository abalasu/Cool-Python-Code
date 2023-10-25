# First decorator
import time
def exec_time_calc(func_name):
    print('Step 1 - Decorator wrapper Starts ', func_name.__name__)
    def inner_fun(*arg, **kwarg):
        print('Step 3 - Decorator inner function starts - has the actual parms ')
        st_time = time.time()
        print('Step 4 - Decorator inner function calls actual function with parms')
        func_name(*arg, **kwarg)
        print('Step 7 - Actual function returns back to decorator function ')
        ed_time = time.time()
        print('    Time taken by ', func_name.__name__, ed_time - st_time)
        print('Step 8 - Decorator function completes and returns back to the main function ')
    return inner_fun
@exec_time_calc
def multiplier(a, b):
    print('Step 5 - Execution of the actual function ')
    print('    Value of ', a ,'*', b, ' is ', a*b)
    time.sleep(2)
    print('Step 6 - Actual function completes and passes back to the decorator ')
    return
print('Step 2 - Main Func Starts and calls actual function ')
multiplier(4,45)
print('Step 9 - Main Func Ends ')