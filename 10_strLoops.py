# DECLARE sen1, sen2 : STRING
sen1 = "Messi is the goat"

'I want to print all characters of this sentence'
# for i in sen1:
#     print(i)

sen2 = "mujhAy khana khaAna hai"


'''
write a code that counts the number of (a)s in sen2

every character needs to be checked
if it is an a, we will count it otherwise do nothing

how to check a character
    IF STATEMENT

How to count?
    We need to maintain a counter
    variable that increments by 1 whenever i comes across an a
    initialise this to 0

How do we check allll characters?
    Loop 
    we just saw that for loops make it v easy to go through a string 
'''

# count = 0
# for i in sen2:
#     if i == "a":
#         count += 1
#
# print(count)
'''
The code in its current state will not include capital A in the count
BUTTTTTTT I WANT BOTH As :(

'''

# count1 = 0
# count2 = 0
#
# for i in sen2:
#     if i == "a":
#         count1 += 1
#
#     if i == "A":
#         count2 += 1
#
# print(count1+count2)
'The above will give a correct answer, so will the following'

# count = 0
# for i in sen2:
#     if i == "a" or i == "A":
#         count += 1
#
# print(count)

'''
While both the above mentioned techniques are correct, they have a flaw
    Suppose you were to count all vowels, in that you would have to create
    10 conditional checks instead of 5 

.lower() will take a string and convert all characters to lower case
For instance, any of the followings strings: YES, Yes, yEs, yeS, yes
will all be converted to "yes"

and yes, .upper() also exists
'''

count = 0
for i in sen2:
    if i.lower() == "a":
        count += 1

print(count)