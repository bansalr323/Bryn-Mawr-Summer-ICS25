#Pass by Value vs. Pass by Reference: 

'''
"I'm passing something into a function" <= my function has a parameter and I pass in the argument to the parameter.
'''

def example(num): 
    print(num + 1) 

example(5)

def example2(num): 
    num = num + 10 

number = 15 
print(number) 
example2(number)
print(number) 

'''This did not work because it is passing the value vs. passing the number.'''

def example3(mylist): 
    mylist.append("Hello from example3")

strings = ["Hello", "World"]
print(strings) 
example3(strings)
print(strings) 

'''
When we pass in a list (or any mutable object), then we're passing in the reference of the list itself(so both python and example3
know the adress of our list)

Things get passed in as value (immutable): 
    - integers 
    - floating point numbers 
    - booleans (true or false)

Things get passed as its reference (mutable): 
    - Lists 
    - Dictionaries 
'''
