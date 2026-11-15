'''
Take as input from the user 5 different positive integers and display the
largest one of them

Multiple Inputs -> Repetitive -> LOOPS
    Which Loop?
        Count is known -> FOR Loop

Whenever we need to find a max value, we always start with a very small value
'''

# DECLARE max, UserIn : INTEGER
max = 0
for i in range(5):
    UserIn = int(input("Please enter a positive Integer: "))
    if UserIn > max:
        max = UserIn

print(f"The largest value you input was {max}")