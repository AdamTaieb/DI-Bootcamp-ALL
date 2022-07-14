# import random
# def calculation(a, b):
#     print(a + b, a - b)

# calculation(12, 10)

#ex1

# def display_message(title):
#     print("i love " + title)
# display_message("python") 

#ex2

# def favorite_book(title):
#     print("one of my favorite book is " + title) 
# favorite_book("la vie après la vie")

#ex3

# def describe_city(name, country):
#     print(name + " is in " + country)
# describe_city("paris", "france")

#ex5

# size = input("gimme a size ")
# sentence = input("gimme a sentence ")


# def make_shirt():
#     if size == "S":
#         print("the size of the shirt is " + size + " and the sentence is " + sentence)
#     elif size == 'M':
#         print("the size of the shirt is " + size + " and the sentence is " + sentence)
#     elif size == 'L':
#         print("the size of the shirt is " + size + " and the sentence is " + sentence)

        
# make_shirt()

#ex6

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians():
#     for i in magician_names:
#         print(i)
# show_magicians()

# def make_great():
#     for i in magician_names:
#         print(i + " the Great")
# make_great()

# show_magicians()

#ex7

# def get_random_temp(season):
#     if season == "winter":
#         return(random.randint(0, 16))
#     elif season == "spring":
#         return(random.randint(16, 23))
#     elif season == "summer":
#         return(random.randint(24, 32))
#     elif season == "autumn":
#         return(random.randint(32, 40))
# get_random_temp("autumn")
 
# def main():
#     temp = get_random_temp("autumn")
#     print(f"{temp}")
#     if temp == 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 < temp <= 16:
#         print("Quite chilly! Don’t forget your coat")
#     elif 16 <= temp < 23:
#         print("put a jacket")
#     elif 24 < temp <= 32:
#         print("put a hat")
#     elif 32 <= temp < 40:
#         print("put a swimming suit")
# main()



#daily challenge

# matrix = [
#    [7, "i" , 3],
#    ["T", "s", "i"],
#    ["h", "%", "x"],
#    ["i", " ", "#"],
#    ["s", " ", "M"],
#    ["$", "a", " "],
#    ["#", "t", "%"],
#    ["^", "r", "!"],
# ]

# decoded_word = ""
# for i in matrix:
#     if i != letter:
#         decoded_word += i
#     else:
#         add