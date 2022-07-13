# # 4) Write a Program to check whether a person can watch MA15+ rated movie.
#  On the basis of the following condition.
# 1) The person is at least 15 years old.
# 2) They have parental supervision.
# You need to take 2 input from the user, asking for age and whether parent is accompaning or no
# Your output should show “Can watch movie” or “Cannot watch the movie”

age = int(input("Enter Age Of Person:"))

if(age<15):
    print("Can't Watch The Movie")

else:
    is_parent_is_accompaning = input("Is person's parent is accompaning YES or NO ?:")

    if(age >= 15 and is_parent_is_accompaning == "YES"):
        print("Can Watch The Movie")
    elif(age >= 15 and is_parent_is_accompaning == "NO"):
        print("Can't Watch The Movie")
    else:
        print("Enter valid values")

