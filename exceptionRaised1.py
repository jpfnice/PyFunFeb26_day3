# ValueError, IndexError, Exception

def add(operand1, operand2):
    
    if not isinstance(operand1, int):
        raise Exception("The first parameter of add() must be an int!")
    if not isinstance(operand2, int):
        raise Exception("The second parameter of add() must be an int!")
    temp=operand1+operand2
    return temp


# here is an example of how we could handle the exception
# raised by add():
    
try:
    print(add(4, 4))
    print(add(4, 4.4)) # <=
    print(add(14, 5))
except Exception as ex:
    print("Exception raised:", ex)

print("End of the script")