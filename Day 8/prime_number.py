def prime_checker(number):
    prime = True
    
    for i in range(2, number):
    
        if number % i == 0:
            prime = False
        

    return prime



n = int(input("Check this number: "))

print(prime_checker(n))