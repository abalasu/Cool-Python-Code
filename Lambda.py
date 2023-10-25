x = lambda a: a*2 
print(x(2))

def greeting(g):
    return lambda x: g + x

a = greeting("Hello ")
b = greeting("Hi ")
c = greeting("Vanakam ")

print(a('Arul'))
print(b('Arul'))
print(c('Arul'))

def func(x:"str",y:"str") -> str:
    return x+y

print(func("Hello world ","Arul"))
