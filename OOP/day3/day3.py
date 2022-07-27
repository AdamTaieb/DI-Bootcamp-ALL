
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
    
#     def __str__(self):
#         print(f'{self.amount} {self.currency}')
    
#     def __int__(self):
#         print(f'{self.amount}')

#     def __repr__(self):
#         print(f'{self.amount} {self.currency}')
    
#     def __add__(self, other):
#         if self.currency == other.currency:
#             return self.amount + other.amount
#         else:
#             return 'Cannot print that'
    
#     def __iadd__(self, other):
#         return self.amount + self.amount + other.amount



    
# c1 = Currency('dollars', 5)
# c1.__str__()
# c2 = Currency('dollars', 10)
# c2.__int__()
# c2.__repr__()
# c3 = Currency('shekels', 1)
# c4 = Currency('shekels', 10)

# print(c1.__add__(c3))
# print(c1.__iadd__(c2))

# class Alo:
#     def user():
#         x = int(input('gimme a number: '))
#         import random
#         a = random.randint(1,100)
#         print(f'the computer number is {a}')
#         if a == x:
#             print('you win')
#         else:
#             print('you lose')

#     user()

# import random
# import string
# letters = string.ascii_lowercase
# print ( ''.join(random.choice(letters) for i in range(10)) )


# import datetime
# today_date = datetime.date.today()
# print(today_date)

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# english_words = ["Hello", "Goodbye", "Welcome", "See you soon"]
# result = zip(french_words, english_words)
# print(dict(result))
# import turtle

# class Circle:
#     def __init__(self, radius: int):
#         self.radius = radius
#         self.diameter = radius * 2
    
#     @classmethod
#     def from_diameter(cls, diameter):
#         new_circle = Circle(diameter/2)
#         return new_circle

#     def area(self):
#         return 3.14 * self.radius ** 2

#     def print_circle(self):
#         output = turtle.circle(self.area())
#         return output

#     def __add__(self, circle):
#         return Circle(self.radius + circle.radius)
    
#     def __le__(self, circle):
#         return self.area() <= circle.area()
    
#     def __lt__(self, circle):
#         return self.area() > circle.area()

    
#     def __eq__(self, circle):
#         return self.area() == circle.area()
    
#     def __repr__(self):
#         return str()

    
# circle1 = Circle(2)
# print(f"cirlce 1: r-{circle1.radius} d-{circle1.diameter}")

# circle2 = Circle.from_diameter(7)
# print(f"cirlce 2: r-{circle2.radius} d-{circle2.diameter}")
# circle2.print_circle()

# circle3 = circle1 + circle2
# print(f'Circle 3: r-{circle3.radius} d-{circle3.diameter}')

# print(circle1 <= circle1)

# circle_list = [circle3, circle2, circle1]
# circle_list.sort()
# print(circle_list)