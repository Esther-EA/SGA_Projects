import random
# Create a list of integers between 5.5 and 20.5. Write a python program using the lambda function that does the following

numbers = [5, 8, 6, 9, 5, 6, 9, 15, 7, 14]
# for i in range(5, 21):
#     numbers.append(i + round(random.random(), 1))

# count the even and odd numbers in the list . Use the lambda function to do this
odd = len(list(filter(lambda x: x % 2 != 0, numbers)))
even = len(list(filter(lambda x: x % 2 == 0, numbers)))
print("Odd numbers in the list are: ", odd)
print("Even numbers in the list are: ", even)

# square and cube every number in the list. Use the lambda function to do this
square = list(map(lambda x: x ** 2, numbers))
cube = list(map(lambda x: x ** 3, numbers))

# print the result of the above two operations in the form of a list
print("Square of the numbers in the list are: ", square)
print("Cube of the numbers in the list are: ", cube)