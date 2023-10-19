def addition(x, y):
    # adding two numbers
    return x + y

def subtraction(x, y):
    # subtracting two numbers
    return x - y

def multiplication(x, y):
    # multipling two numbers
    return x * y

def division(x, y):
    # divide two numbers
    if(y == 0): 
       raise ValueError("Dividend value can't be zero.")
    return x / y

def modulo(x, y):
    # modulo of two numbers
    if(y == 0): 
       raise ValueError("Dividend value can't be zero.")
    return x % y