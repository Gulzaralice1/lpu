# write a program to find greates two imter
def greates(num1,num2):
    greates = None
    if(num1 >= num2):
        greates = num1
    else:
        greates = num2
    return greates
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
print(greates(num1,num2))