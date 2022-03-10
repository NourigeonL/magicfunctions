from magic_lib import magicfunctions

def test_magicFunction1():
    assert magicfunctions.magicFunction1("vahbunA") == "Anubhav"

def test_magicFunction2():
    arr = [0,0,0,0,1,0,0,0,0]
    assert magicfunctions.magicFunction2(arr, 1) == 4

def test_magicFunction3():
    arr = ["Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert magicfunctions.magicFunction3(9,15) == arr