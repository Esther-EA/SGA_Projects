# Creating a dictionary with key:value pairs as name;squares

# Example 10: Create a Dictionary called squares - lets consider numbers in range 6

# Not using dictionary comprehension
squares = {}
for x in range(5, 16):
    squares[x] = x*x
print(squares)  