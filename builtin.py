# abs - absolute value
import enum


x = -10
print('Absolute of ', abs(x))

# all - returns true if all iterable values are true / non-zero
l = [1,2,3,0]
print('All true', all(l))

# any - returns true if any iterable value is true
print('Any true', any(l))

# ascii - printst the readable version of the passed parameter 

# bin - returns binary version of a given number
print('Binary of ', bin(7))

# oct - returns oct version of a given number
print('Oct of ', oct(17))

# hex - returns hex version of a given number
print('Hex of ', hex(171))

# bool - returns the boolean value of the object
l1 = [255, 2, 3]
l2 = []
print('Bool of zero ', bool(0))
print('Bool of one ', bool(1))
print('Bool of a non-empty list ', bool(l1))
print('Bool of an empty list ', bool(l2))

# bytearray - returns a bytearray object
s1 = 'Hello world'
print('byte array ', bytearray(4))
print('byte array of a list ', bytearray(l1))
print('byte array with encoding ', bytearray(s1, 'utf-8'))

# bytes - returns a bytes object
print('bytes object ', bytes(4))
print('length of bytes object ', len(bytes(4)))

# callable
print('If the passed object is callable ', callable(l1))
def func1():
    return 2
print('If the passed object is callable ', callable(func1))

# chr - returns the character from the specified unicode
print('Chr of unicode', chr(0xb90))

# compile and exec - compile() and execute() given program
f = open('C:/Users/jeyar/source/repos/coolcode/lambda.py','r')
python_source = f.read()
f.close()
codebase = compile(python_source, 'lambda.py','exec')
exec(codebase)

# complex() - returns a complex number
print('Complex number ', complex(3,5))

# delattr() - deletes specific attributes and methods from a given object
class c1():
    x = 'This is an example '
    y = 'This is another example '
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def print_method(self):
        print(self.a, self.b, self.c, self.y)

obj1 = c1(1, 2, 3)
obj1.print_method()
print(delattr(c1, 'x'))

# dir() -> returns the list of methods and variables of a class
print('Directory function', dir(c1))
print(obj1.__sizeof__())

# divmod -> returns the quotient and reminder
print('Divmod function ', divmod(5,2))

# enumurate() -> Adds a counter to a list or a string or any iterable
l3 = ['arul','raj','ram']
e1 = enumerate(l3)
for ele in e1:
    print(ele)
for count, ele in enumerate(l3, 10):
    print(count, ele)

# eval() -> Evaluates and executes an expression
x = 'print("Hello World ")'
eval(x)

# filter() -> Executes a user defined function on an iterable and filters out based on the function
l2 = [3,4,5,2,7,9,6]

def odd_even_sorter(x):
    a, b = divmod(x, 2)
    if b == 0:
       return True
    else:
       return False

l4 = filter(odd_even_sorter, l2)
print('Filter function ')
for x in l4:
    print(x)

# format() -> Formats numbers / strings as required
print("format(0.43,'%') ",format(0.43,'%'))
print("format(43,'b') ",format(43,'b'))
print("format(43,'o') ",format(43,'o'))
print("format(43,'x') ",format(43,'x'))
print("format(430002,',') ",format(430002,','))

#frozenset() -> Converts iterable to an immutable frozen set
fs = frozenset(l2)
print('Frozenset ', fs)

#getattr() -> To get the attribute of an object
print('getattr() ', getattr(obj1, 'y'))

#globals() -> Returns the global symbol table as a dictionary.
x = globals()
print('Global Table ', x)
print('Program Name ', x["__name__"])

#id() -> prints the ID of the object
a = 5
print('ID of a is ', id(a))
print('ID of obj1 is ', id(obj1))

#input() -> Allows user to accept an input
a = input('Enter a number ')
print(a)

#isinstance() -> Checks if the object is an instance of a class/object
print('isintance() ', isinstance(obj1, c1))
print('isintance() ', isinstance(a, (str, int, float)))

#iter() -> creates an iterable
a = [2,3,1,4]
b = iter(a)
print('iter() ', next(b), next(b), next(b))

#locals - dump of all the variable and function defenitions
print('locals()', locals())

#map - takes each element of an iterable and passes through the function and captures results in a list
def double(a):
    return a*2
b = map(double, (4,5,8))
print(list(b))

#object() - creates an empty object
x = object()
print('object() ', type(x))

#ord() - returns the unicode code of the passed character
print(ord('A'))

#pow() - Power of x to y
print('pow() ', pow(4,2))

#range() - range of numbers from start, end incremented at a step level
print("range() ", list(range(0,10,2)))

#reversed() - reverses a given iterable
a = (4,5,2,3)
print('reversed() ', tuple(reversed(a)))

#round() - round the numbers
print('round() ', round(3.5))

#setattr() - updates the value of the attribute
setattr(obj1,'y','this is the updated value')
obj1.print_method()

#slice() - substr of an iterable
l1 = [1,2,3,4,5,6,7,8]
x = slice(0,8,2)
print('slice() ', l1[x])

#sorted() - sorts an iterable
t1 = (4,1,3,8,7)
print('sorted() ', sorted(t1,reverse=True))

#sum() - finds the sum of an iterable
print('sum() ', sum(t1))

#zip() - merges two iterables at an element level
first_name_list = ['Arul','Jeya','Bhavna']
last_name_tuple = ('Bala','Arul','Arul')
print('zip() ', list(zip(first_name_list,last_name_tuple)))
