size = input("What size pizza? ")
add_pepperoni = input("Do you want pepperoni? ")
extra_cheese = input("Do you want extra cheese? ")

price = 0

if size == 'S':
    price += 15

elif size == 'M':
    price += 20

else:
    price += 25

if add_pepperoni == 'Y':
    if size == 'S':
        price += 2
    else:
        price += 3

if extra_cheese == 'Y':
    price += 1

print(f"Your final bill is ${price}")