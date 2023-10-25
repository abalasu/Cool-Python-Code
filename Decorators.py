def zeroth_func(func):
    print('I am a Decorator zero ', func.__name__)
    def inner(a, b):
        print("The value of a+b is in zero")
        print(a, b)
        print(func)
        print(inner)
        func(a,b)
        print('Back in zeroth func')
    return inner

def first_func(func):
    print('I am a Decorator one', func.__name__)
    def inner(a, b):
        print("The value of a+b is in one")
        print(a, b)
        print(func)
        print(inner)
        func(a,b)
        print('Back in first func')
    return inner

@first_func
@zeroth_func
def second_func(a, b):
    print(a+b)
    print('In second Func')
#   return

print('Main Program')
second_func(5,10)
print('End of Main')