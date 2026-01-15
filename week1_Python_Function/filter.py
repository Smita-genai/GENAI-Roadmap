# Filter() - This function filter out the items from list(or any other iterator) based on condition returns True

# Example 1
def even(num):
    if num % 2 == 0:
        return True
    

numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(even, numbers)))


# Example 2
# filter with lambda function
list1 = [1,2,3,4,5,6,7,8,9,10]
greater_than_five = list(filter(lambda n: n>5, list1))
print(greater_than_five)

# Example 3
# filter with lambda function and multiple conditions
list2 = [3,4,5,6,7,8,9,20,10]
even_and_greater_than_five = list(filter(lambda n: n > 5 and n % 2 == 0, list2))
print(even_and_greater_than_five)

# Filter() to check if the age is greater than 25 in dictionary
def get_age_greater_than_25(people):
    return people['age'] > 25

details = [{'name':"JACK",'age': 25}, {'name':"Smith", 'age':30}]
print(list(filter(get_age_greater_than_25, details)))