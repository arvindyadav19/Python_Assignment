# Q9) Given 2 integr input a and b, print their sum. However, if sums(addition) is
# in the range of 10..19 inclusive, are forbidden, so in that case just print 20.

a = int(input("Enter the number 1:"))
b = int(input("Enter the number 2:"))

sum = a+b
if(sum >=10 and sum <=19):
    print(20)
else:
    print(sum)
