#Object Oriented Programming

#self is refernece to a specific object 

# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def run(self):
#         print('run')

# player1 = PlayerCharacter('Cindy', 20)
# player2 = PlayerCharacter('Tom', 20)
# print(player1.name, player1.age)
# print(player2.name, player1.age)

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat('yo', 3,)
# cat2 = Cat('yossi', 4)
# cat3 = Cat('Alon', 7)

# print(cat1.name, cat1.age)
# print(cat2.name, cat2.age)
# print(cat3.name, cat3.age)

# def oldest_cat(self, age1, age2, age3):
#     return max(age1, age2, age3)

# x = oldest_cat(cat1.age, cat2.age, cat3.age)
# print(x)
# print(print(f"The oldest cat is {self.name}, and is {x} years old."))

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height 
#     def bark(self):
#         print("{} goes woof".format(self.name) )
    
#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")

#     def fight(self, other_dog):
#         self.other_dog = other_dog.height
#         if self.height > self.other_dog:
#             print("{} is bigger".format(self.name))
#         else:
#             print("you lose")
    
# david_dog =Dog('Rex', 50)
# david_dog.jump()
# david_dog.bark()
# dog1 = Dog('Teacup', 20)
# dog1.bark()
# dog1.jump()
# david_dog.fight(dog1)

# ex3

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for elem in self.lyrics:
#             print(elem)
    
        
# lyrics1 = Song(["There’s a lady who's sure","all that glitters is gold", "and shes buying a stairway to heaven"])
# lyrics1.sing_me_a_song()

#daily Challenge

class Farm:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def add_animal(self, animal):
        self.animal = animal

animal1 = Farm('cow', 5)
animal2 = Farm('sheep', 0)
animal3 = Farm('goat', 12)
animal1.add_animal(animal1)

