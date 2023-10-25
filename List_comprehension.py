list1 = [0,2,3,4,5,6,7,8]
list_odd = []
list_even = []
list_conv = []
list_odd = [x for x in list1 if (x%2) == 1]
list_even = [x for x in list1 if (x%2) == 0]
print(list_odd)
print(list_even)

list_conv = [x if (x%2) == 0 else x*2 for x in list1]
print(list_conv)
