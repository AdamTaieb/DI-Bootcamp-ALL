# #ex2
# import json

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# data = json.loads(sampleJson)
# a = data['company']['employee']['payable']['salary']
# print(a)

# data['company']['employee']['birth_date'] = '09/06/2003'
# print(data)

# with open('sampleJson.json', 'w') as f:
#     json.dump(data, f, indent = 2, sort_keys=True)



#ex1
# import random

# words_list = []

# def get_words_from_file():
#     f = open('/Users/adamtaieb/Desktop/DI-Bootcamp-ALL/OOP/day4/word.txt')
#     data = f.readlines()
#     for i in range(len(data)):
#         words_list.append(data[i].strip('\n'))
#     return words_list

# print(get_words_from_file())

# def get_random_sentence(length):
#     length = int(input("give me a number between 2 and 20: "))
#     if (length < 2):
#         print("error") 
#     elif (length > 20):
#         print("error")
#     else:
#         for i in range(length):
#             print(random.choice(words_list).lower(), end = ' ')
# get_random_sentence(6)


#daily challenge
