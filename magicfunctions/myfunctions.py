from array import array
import string


def magicFunction1(str: string) -> string:
    """
    Reverse the given string. For example, if the string is “vahbunA”, then the result will be “Anubhav”.
    :param str: The string to reverse.

    :return: the string reversed.
    """

    return str[::-1]

def magicFunction2(arr: array, x: int) -> int:
    """
    Research the position of the given number in the given array using so Fibonacci Search Algorithm

    :param arr: The list.
    :param x: The value to search.

    :return: The position of the number in the list.
    """

    def FibonacciGenerator(n):
        if n < 1:
            return 0
        elif n == 1:
            return 1
        else:
            return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)
    
    m = 0 
    while FibonacciGenerator(m) < len(arr):
        m = m + 1 
    offset = -1    
    while (FibonacciGenerator(m) > 1):
        i = min( offset + FibonacciGenerator(m - 2) , len(arr) - 1)
        if (x > arr[i]):
            m = m - 1
            offset = i
        elif (x < arr[i]):
            m = m - 2
        else:
            return i        
    if(FibonacciGenerator(m - 1) and arr[offset + 1] == x):
        return offset + 1
    return -1