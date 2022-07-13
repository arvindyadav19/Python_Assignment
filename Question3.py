# 3) A bartender is writing a simple program to determine whether he should 
# serve drinks to someone. 
# He only serves drinks to people 18 and older and when he's not on break.
# You need to Take input from the user as age and 
# also take input from the user whether he is on
# break or no. Your output should be “serve drink” 
# if conditions satisfies else “dont serve”.

age = int(input("Enter Your Age:"))

is_on_break = input("Is bartender on break Yes or No?")

if(age>=18 and is_on_break == "No"):
    print("Serve Drink")    
elif(age>=18 and is_on_break == "Yes"):
    print("Don't Serve")

elif(age<18):
    print("Don't Serve")

else:
    print("Enter Valid Options")