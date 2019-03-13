"""
Python does offer magic methods like sum() and others, please try to write down your algorithms or coding
instructions clearly without using any shortcuts
"""

print('it is running...')

# Multiply 3 and any number
def mult(number):
    return 3 * number


# testing:
print(mult(4))  #12


# adds two numbers together
def add(a, b):
    return a + b


#testig:
print(add(112, 45))  #157


"""
Using data structures like list, can you find the total or the values in that list.
Do not use a function like sum(someList), that would be cheating ;-)
"""
# Data structure
numbers = [1, 2, 3, 6]
def sumOfListNumbers(someList):
    subtotal = 0
    for index in range(0, len(someList)):
        subtotal = subtotal + someList[index]
    return subtotal


#testing:
myNumbers = [1, 1, 2, 3, 5]
print(sumOfListNumbers(myNumbers))  #12


# Program checker (do not change the lines below)
assert sumOfListNumbers(numbers) == 12
assert mult(4) == 12
assert add(1, 3) == 4
