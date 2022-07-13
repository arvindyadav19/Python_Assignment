# Q7) Take 3 integer input values, a b c, and print their sum. However, if one of
# the values is the same as another of the values, it does not count towards the sum.

a = int(input("Enter first value:"))
b = int(input("Enter second value:"))
c = int(input("Enter third value:"))



if(a == b ):
    sum = a+c
    print(sum)
elif( b == c):
    sum = a+b
    print(sum)
elif(a == c):
    sum = b+c
    print(sum)
else:
    sum = a+b+c
    print(sum)