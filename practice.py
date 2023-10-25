cities = ['Madurai', 'Chennai', 'Virudhunagar', 'Coimbatore', 'Pondicherry', 'Tirunelveli']
newlist = []
for city in cities:
    if 'a' in city:
        newlist.append(city)

print(cities)
print(newlist)

# List Comprehension - Syntax: new_list = [return_value/expression for item in iterable if condition == true]
rev_list = [city for city in cities if 'a' in city]
print(rev_list)

# return the item from the list if city is not Virudhunagar, if Virudhunagar return Chennai
rev_list1 = [city if city != 'Virudhunagar' else 'Chennai' for city in cities]
print(rev_list1)

# Reversing a list function
print(list(reversed(newlist)))

# Lambda functions - Syntax: Function_name = lambda input parameters: return expression
a = 3
b = 5
c = 7
x = lambda a, b, c : a + b + c
print('x is ', x(a,b,c))

# Using lamda functions as anonymus functions within other functions
def myfunc(n):
    return lambda a: a * n

# Define new functions with names for lambda
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(4))
print(mytripler(4))

# Nested Functions

def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)

# Pass function as an argument

def add(x, y):
    return x + y
def sub(x, y):
    return x - y

def calc(func, x, y):
    return func(x,y)

print(calc(add,4,6))
print(calc(sub,5,4))

# Return function as a value
def greeting(name):
    def hello():
        return "Hello " + name
    return hello

greet = greeting("Arul")
print(greet())

# Decorators 1
def make_pretty(func):
    def inner():
        print("I got decorated ")
        func()
        print("After Func")
    return inner

@make_pretty
def regular():
    print("I am Regular ")
    return

regular()

# Decorators 2 - Decorating with parameters
def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("Divide by Zero Error ")
        else:
            x = func(a, b)
    return inner

@smart_divide
def divide(a,b):
    print("The result is ", a/b)
    return

divide(2,5)
divide(3,0)

# Decorators 3 - Chaining of decorators
def star(func):
    def inner(*args, **kwargs):
        print(args, kwargs)
        print('*' * 15)
        func(*args, **kwargs)
        print('*' * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print('%' * 15)
        func(*args, **kwargs)
        print('%' * 15)
    return inner

@star
@percent
def printer(msg, num=x):
    print(msg,num)
    return

printer("Hello there", num=5)

# printer=star(percent(printer))
# printer("Hi there")