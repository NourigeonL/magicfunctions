# **The Magic Library !** - The library that gives you all the functions and class you need !
## Why ?
I decided to create this project during a night at 2am after remembering the videos "Why you suck at coding" of Ben Awad, about the algorithms asked during job interviews. He showed how to resolves this algorithm problem in very stupid ways but I was thinking : *Can we even do worse ?* Of course you can ! It also remembers me some coding exams during college when sometimes you even have to write C or even worse Java code on paper. I also remember a friend when sometimes we discussed about how to do something and when he didn't know exactly how we could it, it just said "... then we called the magic function ..." and here it is ! The library that (will) contain all famous algorithms that you need for job interviews, college exams, or just some common algorithm you need all the time. But to keep the idea of "calling magic function", the functions be named "reverseBinaryTree" or "magicSquare" but just "magicFunction1", "magicFunction2", etc. So that if during a job interview or an exam they ask you how to reverse a binary tree in python then you can write :
```python
from magicLib import magicfunction1263905

reversedTree = magicfunction1263905(theTree)
```

# Todo

- Everything of course
- For now, I'm just writing `magicFunction1`, `magicFunction2` etc. but I think having a code to classify the algorithm would be nice, like "the function starting by '420' are sorting algorithm"
- Create the ultimate function `magicfunction` that does whatever you want. It should be used like this :
    ```python
    reversedTree = magicfunction("reverseBinaryTree", tree)
    index = magicfunction("fibonacciSearch", arr, 60)
    ...
    ```
    The function will just call the right function with the given parameters

# Functions implemented
- Reverse String
    ```python
    magicFunction1(str) 
    # or
    MagicClass.magicFunction("reverseString",str)
    ```
- Fibonacci Search
    ```python
    magicFunction2(arr, x) 
    # or
    MagicClass.magicFunction("fibonacciSearch",arr, x)
    ```
- FizzBuzz
    ```python
    magicFunction3() 
    # or
    MagicClass.magicFunction("fizzBuzz")
    ```