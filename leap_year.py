print("Weclome to leap year calculator")
leap = False

year = int(input("Which year would you like to check? "))

if year%4 == 0:
    leap = True

    if year%100 == 0:
        leap = False

        if year%400 == 0:
            leap = True


print(f"The year {year} is leap year? {leap}")