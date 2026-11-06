'''
Take as input from the user an integer(n)
You need to print the sum of values from 0-n
        Eg: n = 5
            -> 0+1+2+3+4+5

Need input from user
    Variable
    prompt

I know I will have to sum multiple numbers
Therefore, ik I will end up using a loop
    Do I know the count -> seems so
        FOR LOOP

NEED TO STORE THE SUM somewhere asw
    variable
    It is important that you INITIALISE YOUR SUM TO 0

Suppose the user enters 3
    What do I want?
    0+1+2+3

for i in range(3):
    sum = sum + i

sum = 0
In first iteration we will have i = 0
sum = sum + 0 -> sum = 0+0 -> sum = 0

Second Iteration i = 1
sum = sum + 1   -> sum = 0+1    -> sum = 1

Third Iteration i = 2
sum = sum + 2   -> sum = 1 + 2  -> sum = 3

Now i will become 3 and the LOOP WILL TERMINATE
    Rmmbr, for loop runs till < i
    But we have only done 0+1+2

For any value that the user enters, the summation process will stop BEFORE we
add the value entered by the user :(

therefore, we will have to run teh loop for user's input + 1
'''

# DECLARE Num, Sum : INTEGER
Num = int(input("Please enter a number: "))
Sum = 0

for i in range(Num+1):
    Sum = Sum + i

print(Sum)