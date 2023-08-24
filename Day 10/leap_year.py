def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
                return True
            else:
                print("not leap year")
                return False
        else:
            print("leap year")
            return True
    else:
        print("not leap year")
        return False
        
def days_in_month(year, month):
    leap_year = is_leap_year(year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if leap_year:
        month_days[1] = 29
    
    return month_days[month-1]
    
    
year = int(input("year: "))
month = int(input("month: "))
days = days_in_month(year, month)
print(days)