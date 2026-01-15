# Syntax
'''lambda is anonymous function created by using lambda keyword and have any number of arguments but only one expression'''
## lambda arguments : expression

# 1. Basic Function
def add(a,b):
    return a+b

print(add(6,7)) 

# Using Lambda Function
addition = lambda a, b : a + b
print(addition(10, 20))

# 2. Basic Function
def even(num):
    if num%2==0:
        return True
    return False
    
print(even(20))

#Using Lambda Function
even_num = lambda num : num % 2==0
print(even_num(15))


## Lambda function with map
# map() - a map function applies a given function to all items in the list nad returns a map object
numbers=[5, 8, 9, 10, 4]
square = lambda num : num ** 2
print(list(map(square, numbers)))