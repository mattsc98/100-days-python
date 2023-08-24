from art import logo



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add, 
    '-' : subtract,
    '*' : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("Whats the first number "))

        
    print("Pick out an operation: ")
    for operation in operations:
        print(operation)
    operation_symbol = input("Pick one: ")

    num2 = float(input("Whats the second number "))

    answer = operations[operation_symbol](num1, num2)
    print(answer)

    while(True):
        stop = input("Stop? (y/n) ")
        if stop == "y":
            break
        
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick one: ")
        num3 = float(input("Whats the next number "))
        
        new_answer = operations[operation_symbol](answer, num3)
        print(new_answer)
        
        
calculator()