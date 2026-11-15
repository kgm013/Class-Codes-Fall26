'''
Arrays are a collection of items of the SAME datatype stored in a single variable

An array is a contigous chunk of memory - there are no gaps in the memory. Each element is
adjacent to one another
Since it is a contigous chunk you would need to RESERVE SPACE BEFOREHAND
    Therefore, you need to know the size of the array beforehand

PYTHON DOES NOT HAVE A DATASTRUCTURE NAMED ARRAYS
    Python acc has a much more superior datastruture known as lists
    - Lists are NOT fixed length
    - Lists can store multiple datatypes at once

YOUR EXAMINER DOES NOT WANT YOU TO USE LISTS
WE ARE SUPPOSED TO PRETEND THAT WE HAVE ACCESS TO AN ARRAY - NOT A LIST

The first element of an array in Python is 0, NOT 1
'''


'An array of STRINGS'
# DECLARE Students : ARRAY [0:3] OF STRING
Students = ["Hussain", "Usman", "Zunaira"]
# print(Students)

'Now I want to access an element (a singular element) from the array'
name = Students[2]
# print(name)
# print(Students[0])


'''
Your examiner sometimes asks you to add values in the array at runtime

Take the input of 5 names from a user and store them

Repetitive -> Loop
    FOR

Where do I store these 5 values?
variables are an option but too complicated
Use an array to input all these elements

We initialize an empty array and then use the append function
append - add at the end
'''

StuName = []
for i in range(5):
    name = input("Pls enter name: ")
    StuName.append(name)

print(StuName)

'If I now want to add a value at index 1 for instance'
StuName[1]="skfhks"
print(StuName)
