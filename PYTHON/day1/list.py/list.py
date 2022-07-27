number_list = [1,2,3,4,5]

for i in number_list:
    print(i)

#range(start, end, step)

print(number_list[0::2])
print(number_list[-1::-1])

number_list[2] = 33
print('updateded list:', number_list)

#addition
numbers_b = [6,7,8,9]
number_list += numbers_b
print(number_list) 

#multiplication
number_list *= 2
print(number_list)

a = [1,2,3,4,5]
a *= 2
print(a)

#list loops

for i in range(len(a)):
    print(i)

for i, val in enumerate(a):
    print(i)
    print(val)

#enumarate = looping from the start 
#i is to loop from the middle 
product = a[0]
for num in a[1:]:
    product *= num
print(product)

#adding items

b=[]
b.append(1)
print(b)

#insert (where it starts, what do i add)

b.insert(0, 0) 
print(b)

b.append(1)
print(b)

#remove only removes the first occurence of the selected items

b.remove(1)
print(b)

# delete a variable or the value of an index

del b[0] #or del b
print(b)

# pop removes the last element of a list

b += [2, 3, 4]
b.pop()
print(b)

# sorting items 

char_list = ['z', 'b', 'f', 'a', 'd']
sorted_char_list = sorted(char_list)
print(sorted_char_list)

#ex1

list1 = [5, 10, 15, 20, 25, 50, 20]
idx=list1.index(20)
print(idx)
list1[idx]=200
print(list1)

