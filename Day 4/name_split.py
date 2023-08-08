import random

names_string = input("Give me yo names split by a ,\n")

names = names_string.split(",")

random_name = names[random.randint(0, len(names)-1)]

print(f"My dude {random_name}")