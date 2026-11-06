'''
Write a program that determines if a person is eligible for a special library
membership. To qualify:
    They must be at least 18 years old
    If they are a student, their ID must be valid (expiry year). Just ask if they have an ID or not and check
    the expiry year of the ID
    If they are not a student, they need to be a resident of Lahore

At the end, print if the user is eligible for a special library membership.
If not, tell why


We know that no one under 18 can be a member, so lets start with that
    I will ask the user for their age
        Variable to take input
        Prompt the user to input
        check if condition meets --> IF Statement

WE DON'T TAKE BOOLEAN INPUTS
'''

# DECLARE Age, idExp : INETEGER
# DECLARE isStd, city : STRING

Age = int(input("Please enter your age: "))
if Age < 18:
    print("Sorry ur too young :(")
else:
    isStd = input("Are you a student? answer with yes or no")
    if isStd == "yes":
        idExp = int(input("Please enter the expiry year of your ID: "))
        if idExp >= 2026:
            print("welcome to our gang")
        else:
            print("Please get a valid student id")
    else:
        city = input("Please tell what city you are from: ")
        if city == "Lahore":
            print("LHR LHR hai - welcommmeeee!")
        else:
            print("You need to either be a studnet or be a Lahori")