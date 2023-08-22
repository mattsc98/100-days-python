import math


def calc_num_cans(h, w, coverage):
    
    cans = (h * w) / coverage
    print(cans)
    rounded_cans = math.ceil(cans)
    return rounded_cans

h = input("Enter height: ")
w = input("Enter width: ")
coverage = 5.0

cans = calc_num_cans(float(h), float(w), coverage)
print(f"You will need {cans} cans")
    
    