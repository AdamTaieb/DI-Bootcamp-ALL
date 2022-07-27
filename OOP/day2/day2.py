# class Door:
#     def __init__(self) -> object:
#         is_opened = True

#     def open(self):
#         is_opened = True
#         print("door is opened")
    
#     def close(self):
#         self.is_opened = False
#         print("door is closed")

# class BlockedDoor(Door):

#     def __init__(self) -> object:
#         is_opened = False

#     def open(self):
#         raise Exception("Cannot Open Blocked door")
    
#     def close(self):
#         raise Exception("Cannot Close Blocked door")

# door = Door()
# door.open()
# door.close()
# print(door.is_opened)


# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

#   def new_name(self, rename):
#     self.name = rename


# first_person = Person("John", 36)
# # first_person.show_details()
# first_person.new_name("Johnsko")

# class PlayerCharacter:
#     membership = True
#     def __init__(self, name, age):
#         if (PlayerCharacter.membership):
#             self.name = name
#         self.age = age

#     def shout(self):
#         print(f'my name is {self.name}')
#         return 'Done'

# player1 = PlayerCharacter('Cindy', 19)
# player2 = PlayerCharacter('Tom', 21)
# # print(player1.name, player1.age)
# # print(player2.name, player2.age)
# # # print(player1.run())
# print(player1.name)
# print(player2.membership)
# print(player2.shout())
# print(player1.shout())

# class A():

#     def dothis(self):
#         print("doing this in A")


# class B(A):
#     pass


# class C():
#     def dothis(self):
#         print("doing this in C")


# class D(B, C):
#     pass

# d_instance = D()
# d_instance.dothis() 

# from typing import List, Dict

# class Family:

#     def __init__(self, last_name:str, members:List[Dict]) -> object:
#         self.last_name = last_name
#         self.members = members

#     def born(self, child) -> None:
#         self.members.append(child)
#         print("Congrats for the new baby!")

#     def is_18(self, name):
#         for member in self.members:
#             if name == member['name']:
#                 if member['age'] >= 18:
#                     return True
#                 else:
#                     return False
#         raise ValueError(f"No such member with name {name}")

#     def family_presentation(self):
#         members_print = ''

#         for member in self.members:
#             members_print += f'''Name: {member['name']}, Age: {member['age']}\n'''
        
#         output = f""" The {self.last_name} Family
#         ------------------\n{members_print}
#         """
#         print(output)


# data = [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]

# straussFamily = Family('Strauss', data)

# new_child = {'name':'Tommy','age':0,'gender':'Male','is_child':True}

# straussFamily.born(new_child)

# straussFamily.family_presentation()

