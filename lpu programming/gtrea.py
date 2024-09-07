def grea(num1,num2,num3):
    grtest = None
    if(num1 > num2):
        if(num1 > num3):
            grtest = num1
    elif(num3 > num1):
        if(num3 > num2):
            grtest = num3
    elif(num2 > num1):
        if(num2 > num3):
            grtest = num2
    return grtest

num1 = int(input())
num2 = int(input())
num3 = int(input())
print("'greatest'")
print(grea(num1,num2,num3))