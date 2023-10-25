t = [0, 0, 2]
print(len(t))
print(t)

t.extend([3,4])
print(len(t))
print(t)
t.append([[5,6]])

print(len(t))
print(t)

my_list=[('i','f'), ('h','i','gh'), ('o','n'), ('so','x'),
         ('ge','t'), ('Y','e'), ('mo','r','e')]
print(''.join([t[1] for t in my_list]))

count = 0

def increment(n):
    count=0
    count += n
    return count
    
count = increment(5//2 ** 2)
print(count)

python = ['cool']
x = python[0] in python
print(x)

print('P"yt\'h"on')

image_array = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])