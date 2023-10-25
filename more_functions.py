def calculate(operation='+',*args):
    result = 0
    print(operation)
    if operation=='+':
        sum = 0
        for i in args:
            sum = sum + i
        result = sum
    elif operation == '-':
        result = args[0] - args[1]
    elif operation == '*':
        result = 1
        for i in args:
            result = result * i
    elif operation == '/':
        result = args[0] / args[1]
    return result

print(calculate('+',5,10,15))
print(calculate('-',5,10))
print(calculate('*',5,10,15))
print(calculate('/',5,10))
print(calculate())