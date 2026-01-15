# Map Function
"""Map() function applies a given function to all items in an input list (or any other iterable) and returns a map object(iterator).
This is particularly useful for transforming data in a list comprehensively"""
#Lambda Function
even_num = lambda num : num % 2==0
print(even_num(15))


## Lambda function with map

numbers=[5, 8, 9, 10, 4]
square = lambda num : num ** 2
print(list(map(square, numbers)))


# MAP multiple iterables
list1 = [5, 6,7]
list2 = [8, 9, 10]
add_numbers = list(map(lambda a, b: a+b, list1, list2))
print(add_numbers)


# Map function for converting string numbers into integer
num_list = ['1','2','3','4','5']
print(list(map(int, num_list)))

# Map function for converting uppercase string into lower case
location = ["MUMBAI", "PUNE", "SOLAPUR","AKKALKOT"]
print(list(map(str.lower, location)))


# Map function for list of dictionaries
def get_name(people):
    return people['name']

people = [{'name':"JACK",'age': 25}, {'name':"Smith", 'age':30}]

print(list(map(get_name, people)))