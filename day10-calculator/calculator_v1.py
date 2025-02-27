from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    while should_continue:
        num2 = float(input("What's the next number? "))
        operation_symbol = input("Pick an operation: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
    
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input(f"Type 'y'to continue calculating with {answer}, type 's' to start over, or type 'n' to exit. ") == 'y':
            num1 = answer
        elif 's':
            calculator()
        #FIX ME: Debug so code doesn't continue infinitely 
        else:
            should_continue = False

calculator()
