# Finding the exponentiation of a number
print("Finding the exponentiation of a number")
x = int(input("Enter number: "))
y = int(input("Enter power: "))

#check if the power is 0
if (y==0):
    #return 1 if y is 0
    print(1)
# calculate the expo if power > 0
else:
    #calculate the exponential
    x = x**y
    print(x)
    
