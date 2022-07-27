# # import random


# # P_MAP = {
# #     'r': -1,
# #     'p': 1,
# #     's': 2 
# # }

# # S_MAP = {
# #     'r': 2,
# #     'p': -1,
# #     's': 1 
# # }

# # R_MAP = {
# #     'r': 1,
# #     'p': 2,
# #     's': -1
# # }

# # def get_map(player_item):
# #     if player_item == 'r':
# #         return R_MAP
# #     if player_item == 's':
# #         return S_MAP
# #     if player_item == 'p':
# #         return P_MAP

# # class Game:
# #     def get_user_item(self):
# #         a = ''
# #         while a not in ('r','s','p'):
# #             print("please select a valid play ")
# #             a = input("select an item between rock, paper, scisor: ")
# #         else:
# #             return a
        
    
# #     def get_computer_item(self):
# #         a = 'r', 'p', 's'
# #         b = random.choice(a)
# #         return b
        
    
# #     def get_game_result(self, user_item, computer_item):
# #         a = 0
# #         b = 0
# #         c = 0
# #         user_item = self.get_user_item()
# #         computer_item = self.get_computer_item()
# #         print(f"Computer chose: {computer_item}")
# #         mapping = get_map(user_item)
# #         if mapping.get(computer_item) == 1:
# #             a += 1
# #             print(a)
# #             return 'it is a tie'
# #         if mapping.get(computer_item) == -1:
# #             b += 1
# #             print(b)
# #             return 'you win, the computer loses'
# #         c += 1
# #         print(c)
# #         return 'you lose, the computer wins'


# # g = Game()
# # print(g.get_game_result('s', 'r'))

# # def play():
# #     a = g.get_user_item
# #     b = g.get_computer_item
# #     c = g.get_game_result
# # play()

# import random
# a=""
# class Game:
#     def __init__(self) -> None:
#         win = 0
#         loss = 0
#         drew = 0
#         a=""
    
#     def get_user_item(self):
#         a= input("select (r)ock/(p)aper/(s)cissors : ")
#         b="r" 
#         c="p"
#         d="s"
#         if a==b or a==c or a==d:
#             return a
#         else :
#             print("You didn't choose the good option, choose again:" )
            
      

#     @staticmethod
#     def get_computer_item():
#         mylist = ["r","p","s"]
#         e = random.choice(mylist)
#         return e

#     def get_game_result(self):
#         user_item = self.get_user_item()
#         computer_item = self.get_computer_item()
#         if user_item==computer_item:
#             print(f"You selected {user_item}. The computer selected {computer_item}. You drew!")
#             drew += 1
#             print(drew)
#             return "draw"
#         if user_item=="s" and computer_item=="p":
#             print(f"You selected {user_item}. The computer selected {computer_item}. You won!")
#             win += 1
#             print(win)
#             return "win"
#         if user_item=="p" and computer_item=="r":
#             print(f"You selected {user_item}. The computer selected {computer_item}. You won!")
#             win += 1
#             print(win)
#             return "win"
#         if user_item=="r" and computer_item=="s":
#             print(f"You selected {user_item}. The computer selected {computer_item}. You won!")
#             win += 1
#             print(win)
#             return "win"
#         if user_item=="p" and computer_item=="s":
#             print(f"You selected {user_item}. The computer selected {computer_item}. You lost!")
#             loss += 1
#             print(loss)
#             return "loss"
#         if user_item=="r" and computer_item=="p":
#             print(f"You selected {user_item}. The computer selected {computer_item}. You lost!")
#             loss += 1
#             print(loss)
#             return "loss"
#         if user_item=="s" and computer_item=="r":
#             print(f"You selected {user_item}. The computer selected {computer_item}. You lost!")
#             loss += 1
#             print(loss)
#             return "loss"
        
        

# new_game = Game()    

# def play():
#     self=new_game.get_game_result()
# play()





