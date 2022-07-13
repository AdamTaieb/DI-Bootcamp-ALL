#ex1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# lol = list(zip(keys, values))
# print(lol)

#ex2

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# age = family.items()
# payment = []

# for name, age in age: 
#     price = 0
#     if age < 3:
#         price = 0
#     elif 3 < age < 12:
#         price = 10
#     else: 
#         price = 15
#     payment.append((name, price))
   
# print(payment)

#ex3

# brand = {
#     "name": "Zara",
#     "creation_date": 1975, 
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton "],
#     "number_stores": 7000,
#     "major_color" : {
#         "France": "blue",
#         "Spain": "red",
#         "Us": ["pink", "green"]
#     }
# }

# brand['number_stores'] = 2
# print(brand)

# a = brand["type_of_clothes"][1]
# b = brand["number_stores"]
# c = brand["creator_name"]
# print(f"zara's clients can be {a}, they have {b} stores, and the creator is {c}")

# brand["country_creation"] = "Spain"
# print(brand)

# # for items in brand:
# #     if ("international_competitors" in brand.keys()):
# #         brand["international_competitors"].append('Desigual')
# # print(brand)

# brand.pop('creation_date')
# print(brand)

# yo = brand["international_competitors"][-1]
# print(yo)

# yo1 = brand["major_color"]["Us"]
# print(yo1)

# le = len(brand)
# print(le)

# for value in brand.keys():
#     print(value)

# more_on_zara = { "creation_date": 1975, "number_stores": 10000} 

# brand.update(more_on_zara)
# print(brand)

# h = brand["number_stores"]
# print(h)

#ex4

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# disney_users = [0, 1, 2, 3, 4]
# disney_users_A = dict(zip(users, disney_users))
# print(disney_users_A)

# disney_users_B = dict(map(reversed, disney_users_A.items()))
# print(disney_users_B)

# # disney_users_C = disney_users_A(sorted(disney_users_A.items))
# # print(disney_users_C)
# sorted_dict = {key: value for key, value in sorted(disney_users_A.items())}
# print(sorted_dict)

#daily challenge 1

# word = input("gimme a word: ")
# b = {k: v for v, k in enumerate(word)}
# print(b)

#daily challenge 2

# items_purchase = {
#   "Water": 4,
#   "Bread": 3,
#   "TV": 1000,
#   "Fertilizer": 20,
#   "hello": 8,
#   "ush": 9,
#   "jei": 0
# }

# a = items_purchase.keys()

# for items in items_purchase.values():
#     wallet = 100
#     if wallet > items:
#         print([f"${items}"])
    

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$350"
for items in items_purchase.values():
    wallet = "$350"
    if wallet > items_purchase.values():
        print(items_purchase.keys)
    else:
        print("nothing")