# get input from user x, y, z
# x, y, z and we store it in a list
# get the max and store it in a variable called max_num

# The below code is asking the user to input three numbers. 
# Then it is adding those numbers to a list.
# Then it is finding the maximum number in the list.

def find_max():
    # ask user for three numbers
    x = int(input('what is your first number: '))
    y = int(input('what is your second number: '))
    z = int(input('what is your third number: '))

    # create an empty list to store user input
    list_of_numbers = []

    # append user inut to list
    list_of_numbers.append(x)
    list_of_numbers.append(y)
    list_of_numbers.append(z)

    # find the maximum number in user input
    max_num = max(list_of_numbers)

    # Print user input
    # print(max_num)
    return max_num

find_max()