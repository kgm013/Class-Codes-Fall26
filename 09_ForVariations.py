# for i in range(3):
#     print(i)
'''
0
1
2
'''

# for i in range(4):
#     print("i")
'''
i
i
i
i
'''

'But what if I dont want to start from 0'
# for i in range(10, 13):
#     print(i)
'''
10
11
12
We already know that when there is only one number present in the brackets, it is the
upper bound - never actually run this. For instance:
for i in range(3) starts from i = 0 and runs till i<3

Now when we have two numbers, the first is considered the starting point whereas the second becomes upper bound
STARTING PT IS INCLUDED
ENDING PT IS EXCLUDED



Well what if i want to print numbers from 9 to 1 - DECREMENT
We need to change the step size. Since we want to decrement, we will use a negative
step size
FYI: The default step size is 1
'''

# for i in range(9, 0, -1):
#     print(i)
'In this case, 9 is the starting pt (included) whereas 0 in the ending pt (excluded)'


'Write a code without the mod operator that prints all odd numbers from 1 to 10'
for i in range(1, 11, 2):
    print(i)