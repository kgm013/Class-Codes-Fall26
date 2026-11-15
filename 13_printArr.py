Students = ["Hussain", "Usman", "Zunaira"]
'How do I print all elements of this array'
# print(Students)

'''
There is a problem in the above method. The problem is that this method prints THE ENTIRE ARRAY - 
with the quotation marks and the commas and the brackets. Essentially the entire thing.

What I really want is to print JUST THE ELEMENTS FROM THE ARRAY
'''
# print(Students[0])
# print(Students[1])
# print(Students[2])
'''
THis method will take way too long when writing the code. Imagine if you have like
100 elements in an array.
RMMBR: Programmers are sust, kaahil, aalsi - they would never let this repetitive work happen

IN COMES LOOPS TO SAVE THE DAY
    WHICH LOOP?
        Is the count known?
        Yes -> for loop       
'''

# for i in range(3):
#     print(Students[i])

'What if I dont know the length of the array?'
# the len function simply finds out the length (the number of elements in the array)
# for i in range(len(Students)):
#     print(Students[i])

size = len(Students)
print(size)
# for i in range(size):
#     print(i)
#     print(Students[i])

'''
Note that strings are just an ARRAY OF CHARACTERS
Therefore, we can also use the len function while dealing with strings
'''
# print(len("Hello mate"))

# str1 = "Kya haal hai?"
# for i in str1:
#     print(i)

'''
why i sit that we have a more compact way or printing strings than we have for printing
arrays. even though strings are techincally arrays
Maza nae aaya :/

TURNS OUT, THERE ISSSS A MORE COMPACT WAY
'''

# for i in Students:
#     print(i)