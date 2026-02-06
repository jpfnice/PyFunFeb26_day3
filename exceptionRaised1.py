
def add(operand1, operand2):
    if not isinstance(operand1, int):
        raise Exception("The first parameter of add() must be an int!")
    if not isinstance(operand1, int):
        raise Exception("The second parameter of add() must be an int!")
    temp=operand1+operand2
    return temp

print(add(4, 4))
print("End of the script")
