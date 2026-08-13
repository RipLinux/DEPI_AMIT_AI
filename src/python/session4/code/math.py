def factorial(n: int):
    ''' 
    Calculate n! using for.
 
    Parameters
    ----------
    num : int
    
    Returns
    -------
    int
    '''
    result = 1
    if n == 0 or n ==1:
        return 1
    elif n < 0:
        raise ValueError("factorial is in undefined for nagtive value")
    for i in range (1,n+1):
        result *=i
    return print (result)

def is_prime (num: int):
    """
    Check whether a number is prime.
 
    Parameters
    ----------
    num : int
    Number to test.
    
    Returns
    -------
    bool
    True if prime, otherwise False.
    """
    for i in range (2,num):
        if num % i == 0:
            return False
        return True

def common_divisors(num1: int,num2:int):
    limit = min (num1,num2)
    divisors = []

    for divisor in range(1,limit+1):
        if num1 % divisor == 0 and num2 %divisor == 0:
            divisors.append(divisor)
    return divisors