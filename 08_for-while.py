"I want to take user input (int) and print all numbers from 0 - userIn USING A WHILE LOOP "

# DECLARE UserIn, count : INTEGER

# UserIn = int(input("Pls enter a number: "))
# count = 0
#
# while count <= UserIn:
#     print(count)
#     count += 1

'^This rlly isnt why while loops were made'
# DECLARE UserIn, count : INTEGER
# DECLARE flag : BOOL

# count = 0
# flag = False
#
# UserIn = int(input("Please enter a number: "))

# while flag == False:
'''
You can actually write the above mentioned condition in a much neater way in Python
'''
# while not flag:
#     print(count)
#     count += 1
#     if count > UserIn:
#         flag = True

'''
Other alternates available:
while flag != True
similarly, instead of writing 
    while flag == True
we can just write
    while flag
    
    
    
Another keyword we have in python is 
        break
As soon as your code runs the line containing this magic word, your loop STOPPPSSS
        THE LOOP WILL NOT COMPLETE THE CURRENT ITERATION EVEN
        Applicable to all loops
        
The following is an example of an inifinite loop
'''
# myFlag = True
# while myFlag:
#     print("Hello")

'Now lets see break in action'


UserIn = int(input("Pls enter a num: "))
count = 0
myFlag = True

# while myFlag is the same as writing while myFlag == True
while myFlag:
    print(count)
    count += 1  # count = count + 1
    if count > UserIn:
        break
    print("Hello")


print("Bye")