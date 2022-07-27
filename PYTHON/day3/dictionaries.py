# user_a = {
#     'first_name': 'Bob',
#     'last_name': 'Ross',
#     'age': 52,
#     'adress': 'Tel-Aviv',
#     'family': [('Jessica', 34), ('Tommy', 8)],
# }

#you can use functions related to the data type of the value like upper here for strings

# print(user_a['first_name'].upper())

# print(user_a.keys())

# for key in user_a.keys():
#     print(key)

# for value in user_a.values():
#     print(value)

# for key, value in user_a.items():
#     print(key, value)

#delete 
# user_a.pop('first_name')
# print(user_a)

# del user_a['last_name']
# print(user_a)

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# yo = sample_dict["class"]["student"]["marks"]["history"]
# print(yo)

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }

# sample_dict.pop('salary')
# sample_dict.pop('name')
# print(sample_dict)

#useful stuff

#zip
# lista = ['Yossi', 'Lise', 'Avner']
# listb = [1991, 1992, 1984]
# listc = ['Tel-Aviv', 'Ramat-Gan', 'Givataim']

# res = list(zip(lista, listb, listc))
# print(res)

#list comprehension
# square_num = []
# for n in range(5, 10):
#     if n % 2 == 0:
#         square_num.append(n)
#         continue.
#     square_num.append(n**2)
# print(square_num)

# square_num = [n**2  if n % 2 != 0 else n  for n in range(5,10)]
# print(square_num)

#dictionarry comprehesnion

# dictionary_comp = {key: value for key, value in enumerate('ABC')}
# print(dictionary_comp)
