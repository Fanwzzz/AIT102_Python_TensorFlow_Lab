x1 = int(input("Please enter the 1st number: "))
x2 = int(input("Please enter the 2nd number: "))
x3 = int(input("Please enter the 3rd number: "))
x4 = int(input("Please enter the 4th number: "))
x5 = int(input("Please enter the 5th number: "))

if x1 >= x2 and x1 >= x3 and x1 >= x4 and x1 >= x5:
    biggest = x1
elif x2 >= x3 and x2 >= x4 and x2 >= x5:
    biggest = x2
elif x3 >= x4 and x3 >= x5:
    biggest = x3
elif x4 >= x5:
    biggest = x4
else:
    biggest = x5

print(f"The biggest number among {x1}, {x2}, {x3}, {x4}, {x5} is : {biggest}")