# 1.
try: 
    a = 1 / 0
except ZeroDivisionError as e: 
    print(f"Error: {e}")

#3.
# try :
    # x = 1
# finally :
    # print(“finally”) #reversed quatation mark -> “. 
          
# 4. What exception types can be caught by the following handler 'except'?
'''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
           '''

# src: https://docs.python.org/3.9/library/exceptions.html#exception-hierarchy

# 5. What is wrong with using the above type of exception handler?
# it can cause an unstable code run, harder to find root cause and debug code errors 

# 6. IOError - will happen when the file can't be found or the file does exist but there is a permission error which can cause the same exception
    # ZeroDivisionError - will happen when trying to divide a number by 0

# 7. 
with open("words.txt", "w") as my_name:
    # 8.
    my_name.write("Lev")

# 9. 
with open("words.txt", "r") as name:
    output = name.read()
    print(output)

# 10.
with open("hebrew_words.txt", "w") as heb_words:
    heb_words.write("שלום")

with open("hebrew_words.txt", "r") as heb_words:
    output = heb_words.read()
    print(output[::-1])