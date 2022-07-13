# Q6) Take a input string from the User and your program should print the string with its first
# and last characters swapped, except under 2 conditions:
# 1) If the length of the string is less than two, print "Incompatible." .
# 2) If the first and last characters are the same, print "Two's a pair." .


input_string = input("Enter String:")

if (len(input_string) <2 ):
    print("Incompatible")
elif (input_string[0] == input_string[-1]):
    print("Two's a pair")
else:
    char_first = input_string[0]
    char_last = input_string[-1]
    sliced_string = input_string[1:-1]

    swapped_string = char_last+sliced_string+char_first

    print(swapped_string)


