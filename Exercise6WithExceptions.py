"""
Define a function to test if a number received as argument is a prime number or not

A prime number is:
    an int
    greater than 1
    that can only be divided by 1 and by itself
    
"""

def isPrime(aNumber):
    """
    isPrime returns True or False depending on the fact that aNumber
    is a prime number or not
    
    Parameters
    ----------
    aNumber : the int to be tested

    Returns
    -------
    True if aNumber is a prime number.
    False if aNumber is not a prime number.

    Exceptions
    -------
    TypeError if aNumber is not an int
    ValueError if aNumber is an int <= 1
    
    """
    if not isinstance(aNumber, int):
        raise TypeError(f"Wrong type of argument received {aNumber}: it should an int")
    
    if aNumber <= 1:
        raise ValueError(f"Wrong argument value received {aNumber}: it should be > 1")
    
    for divisor in range(2,aNumber):
        if aNumber % divisor == 0: # divisor "is a divisor" of aNumber
            return False
    
    return True

if __name__ == "__main__":
    
    # try:
       
    #     isPrime(4.56)
    # except ValueError as ex:
    #     print("ValueError detected:", ex, "!!")
    # except TypeError as ex:
    #     print("TypeError detected:", ex, "!!")
        
    while True:
        value=input("Enter a number to be tested or 'stop' to stop the script: ")    
        if value == 'stop':
            print("Bye!")
            break
        try:
            value=int(value)
            if isPrime(value):
                print(value, "is a prime number")
            else:
                print(value, "is a not prime number")
        except ValueError as ex:
            print("ValueError detected:", ex, "!!")
        except TypeError as ex:
            print("TypeError detected:", ex, "!!")
            