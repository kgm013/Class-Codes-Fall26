# DECLARE i : INTEGER
# for i in range(5):
#     print(i)
'''
In python, loops always start from 0
Therefore, the number (or variable) passed in brackets is THE UPPER BOUND
    Therefore the loop runs till i<(5)

Now I want the same output using a while loop

Unlike a for loop, while loops do not have integrated counters in them
Therefore, I now need to manually manage the counter
'''

# DECLARE Musa : INTEGER
Musa = 0

while Musa < 5:
    print(Musa)
    Musa += 1 # This is the same as writing Musa = Musa + 1