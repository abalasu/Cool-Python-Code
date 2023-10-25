# 1. Identify if a given number is in a list
l1 = [4, 5, 2, 0, 9, 10]
x = int(input("Enter the number "))
print(x in l1)

# 2. Identify the missing numbers in a list of 1 to 100
s1 = set(range(0,100))
s1.remove(35)
s1.remove(46)
s2 = set(range(0,100))
s3 = s2.difference(s1)
print(s3)

# 3. Find duplicate number in integer list
l1 = [3, 5, 2, 0, 4, 3, 7, 8, 1]
l2 = []
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
    else:
        l2.append(i)
print("Duplicate list ", l3)

# 4. Compute the intersection of two lists
l1 = [2, 3, 4, 0, 5]
l2 = [0, 4, 3, 5, 7]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print("Intersection list ", l3)

# 5. Check if two strings are anagrams
s1 = "binary"
s2 = "brainy"
set1 = set(s1)
set2 = set(s2)
if (set1 == set2):
    print("Is an Anagram")
else:
    print("Not an Anagram")

# 6. Find max and min in unsorted list
l1 = [2, 4, 3, 0, 5, 7, 0, 4]
min = l1[0]
max = l1[0]
for x in l1:
    if x > max:
        max = x
    if x < min:
        min = x
print("Max number ", max)
print("Min number ", min)

#7. Remove all duplicates from list
l1 = [2, 4, 3, 0, 5, 7, 0, 4]
l2 = []
for i in l1:
    if i in l2:
        continue
    else:
        l2.append(i)
print("The list without dups ", l2)

#8. Reverse string using recursion
def reverse(str):
    if len(str) <= 1:
        return str
    else:
        return reverse(str[1:])+str[0]

str = "Hello"
print(reverse(str))

#9. Find pairs of integers in list so that their sum is equal to a given integer x
print("Problem 9")
l1 = [2, 4, 3, 7, 8, 6, 5, 0, 0, 3]
num = 9
l = len(l1)
m = 0
while True:
    n = m + 1
    while True:
        if n == l:
            break
        if (l1[m] + l1[n]) == num:
            print(l1[m], l1[n])
        n = n + 1
    m = m + 1
    if m == l:
        break

#10. Compute the first n Fibonacci numbers
n = 10
i = 2
l1 = [0, 1]
while i < n:
    l = len(l1)
    l1.append(l1[l-2]+l1[l-1])
    i += 1
print("Fibonacci list")
print(l1)

#11. Check if a string is a palindrome
s1 = "malayalam"
print(s1 == s1[::-1])

#12. Print all the permutations of a given string
import itertools as it
s1 = "madhavv"
l2 = []
l1 = list(it.permutations(s1))
for x in l1:
# Converting a tuple to a string using the join method
    l2.append("".join(x))
print("The list of permutations ", l2)
