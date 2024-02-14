# Functions are essential in Python and in many other programming languages
# to create meaningful programs, because they allow us to decompose a
# program into manageable parts, they promote readability and code reuse.


def myFunction():
    print("Hello World")
    # Do this
    # Do something else

# call function

# pass parameters and arguments


"""
We can have the return statement inside a conditional, which is a common
way to end a function if a starting condition is not met:
"""

def hello(name):
    if not name:
        return
    print('Hello ' + name + '!')

hello("njjj")

# We can have the return statement inside a conditional, which is a common
# way to end a function if a starting condition is not met:

"""
If we call the function passing a value that evaluates to False , like an empty
string, the function is terminated before reaching the print() statement.
"""

