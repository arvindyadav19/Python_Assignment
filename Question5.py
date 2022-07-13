# 5) Write a Program that takes 2 input from the user as number and Print the output according to
# the following condition.:
# You need to print True if both the numbers are
# Smaller than 0, OR ...
# Greater than 0, OR ...
# Exactly 0
# Otherwise print False

num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))

# if((num1 and num2) == 0 or (num1 and num2) > 0 or (num1 and num2) < 0):
if(num1==0 and num2 ==0):
    print("True")
elif(num1 < 0 and num2 < 0):
    print("True")
elif(num1 >0 and num2 >0):
    print("True")
else:
    print("False")