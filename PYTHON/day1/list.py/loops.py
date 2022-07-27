
for num_a in range(1, 11):
    
    mult_table_num = ""

    for num_b in range(1, 11):
        mult_table_num += f'{num_a * num_b}|'

    print(mult_table_num)

a_str = 'ABCDE'

for char in a_str:
    print(char)
a_list = [1, 2, 'a', 'Text', [1, {1, 2, 3, 4, 5}]]

for item in a_list:
    print(item)

for idx, item in enumerate(a_list):
    print(idx, item)

# for i in range : loop through a sequence of numbers or when you want to start looping from the midlle of a sequence like:

for num in range(0,10):
    print(num)

names = ['Yossi', 'Lisz', 'Roi', 'Roy', 'Rashad']
for name_idx in range(2, len(names)):
    print(names[name_idx])

#enumerate is to use with a sequence and form a tuple

for idx, name in enumerate(names):
    if idx == 2:
        print("breaking the loop")
        break
    print(idx, name)

# while loop : 

password = input('password: ')
while password != 'ABC':
    print('looping')
    password = input('password: ')
    if password == 'ACB':
        print('break')
        break
else: 
    print('correct password provided')
