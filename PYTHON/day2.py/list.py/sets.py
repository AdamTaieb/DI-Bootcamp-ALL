#sets

#a_set = {1,2,3,4}
#print(type(a_set))
#a_set=set({})

duplicates_list = [1,1,1,2,2,'a','c']
list_to_set = set(duplicates_list)
print(list_to_set)

colors_a = {'red', 'green', 'blue', 'pink'}
colors_b = {'grey', 'green', 'blue', 'yellow'}

print("intersecton: ", colors_a.intersection(colors_b))
print("union: ", colors_a | colors_b)
print("without intersection: ", colors_a ^ colors_b)
print("difference a - b :", colors_a - colors_b)
