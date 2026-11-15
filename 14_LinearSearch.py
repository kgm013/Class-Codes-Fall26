Students = ["Heeba", "Umama", "Gul", "Saeed", "Usman"]
'''
I want to find the INDEX(position) of Gul in the array

Think of a picture book(Album)
    You keep turning pages until you get to the desired photograph

Lin search is essentially the same
    Keep going through elements until you get to the desired element

Repetitive Task -> Loops -> Count is know -> FOR LOOP
    How is count known?
    Idk what position the element I want to find (Gul in this case) is on
    We know the MAXIMUM number of elements we need to check
'''

# for i in range(len(Students)):
#     if Students[i] == "Gul":
#         print(i)

'This code has an inefficiency: even when the desired number is found, u check the rest'
# for i in range(len(Students)):
#     print(f"Curr element: {Students[i]}")
#     if Students[i] == "Gul":
#         print(i)
#         break

'Write the same code using a while loop (using a Flag)'
# Counter = 0
# Found = False
# while not Found:                #same as saying while Found == False
#     if Students[Counter] == "Heeba":
#         print(Counter)
#         Found = True
#     Counter += 1

'Finding sm1 who doesnt exist'
Counter = 0
Found = False
while not Found and Counter < 5:                #same as saying while Found == False
    if Students[Counter] == "Kashan":
        print(Counter)
        Found = True
    Counter += 1

if not Found:
    print("The name does not exist")