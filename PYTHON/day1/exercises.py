
#ex1
# my_fav_numbers = {6, 26, 8, 2003, 12}
#my_fav_numbers.add(11)
#my_fav_numbers.add(10)
#print(my_fav_numbers)
#my_fav_numbers.pop()
#print(my_fav_numbers)

#friend_fav_numbers = {25, 29, 78, 56}
#print("intersection: ",  my_fav_numbers |  friend_fav_numbers)

#ex2
#since they represent value that you can't update, you cannot change, add or remove items in a tuple. 

#ex3

#basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#del basket[0]
#print(basket)
#del basket[2]
#print(basket)
#basket.append('Kiwi')
#print(basket)

#basket.insert(0, 'Apples')
#print(basket)

#id = basket.count('Apples')
#print(id)

#basket.clear()
#print(basket)

#ex4

#a float is a number with decimal places whereas an integer doesn't have decimal points, it's a whole number

#we can use a for loop like so:
#nums = range(0, 10)
#float_nums = []
#for number in nums:
 #   f = number / 10
  #  float_nums.append(f)
    
#print(float_nums)


#ex5

#for i in range(0, 21):
#    print(i)
 #   if i % 2 == 0:
  #      print(i)



#while True:
  #  name = input("what is your name?  ")
   # if name == 'adam':
   #     break

#ex 7

#basket = str(input("what are your favorite fruit? ")).split()
#fruit = str(input("enter fruit: "))

#if fruit in basket:
#    print("You chose one of your favorite fruits! Enjoy!")
#else:
 #   print("You chose a new fruit. I hope you enjoy")

#daily challenge



#for user_inp in range(1, user_inp_1+1):
    
#    mult_table_num = ''

 #   for num_b in range(1, user_inp_1+1):
  #      mult_table_num = f'{user_inp * num_b}'.split()

   # print(mult_table_num)

#user_inp = int(input("chose a number: "))
#user_inp_1 = int(input("chose a length: "))
#numbers = [i * user_inp for i in range (1,user_inp_1+1)]
#print(numbers)

#daily challenge 2

# user_inp = input("write a string with duplicate letters")
# user_1 = "".join(dict.fromkeys(user_inp))
# print(user_1)

#ex9

# family = ['brad', 'jessica', 'tomy']

# ages = []

# for member in family:
#     age = int(input(f"{member}'s age is: "))
#     price = 0
#     if 3 >= age <= 12:
#         price = 10
#     elif age > 12:
#         price = 15
#     ages.append((member, age, price))

# print(ages)

# teenagers = [('David', 17), ('Tommy', 18), ('Bob', 23)]
# teens_restricted = []

# for index, member in enumerate(teenagers):
#     age = member[1]
#     name = member[0]
#     if not (16 <= age <= 21):
#         # teens that are not eligible
#         teens_restricted.append(index)

# for restricted in teens_restricted:
#     id = restricted[0]
#     del teenagers[id]

# print("eligible teens: ", teenagers)
# print("restricted teens: ", teens_restricted)

