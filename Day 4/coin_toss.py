import random

choice = input("Pick heads or tails \n").lower()
ch = 0

if(choice == "heads"):  
    ch = 0
else :
    ch = 1

coin = random.randint(0, 1)

if(ch == coin):
    print(f"YAHHOOO you got {choice}!")
else:
    print("Yare yare daze..")