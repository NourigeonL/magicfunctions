from magic_lib import MagicClass

def test_magicFunction1():
    assert MagicClass.magicFunction("reverseString","vahbunA") == "Anubhav"

def test_magicFunction2():
    arr = [0,0,0,0,1,0,0,0,0]
    assert MagicClass.magicFunction("fibonacciSearch",arr, 1) == 4

def test_magicFunction3():
    magic = MagicClass.magicFunction
    arr = ["Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert MagicClass.magicFunction("fizzBuzz",9,15) == arr