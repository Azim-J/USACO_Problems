'''
If we are finding crossing pairs with A:
ABBA - not a crossing pair ( A cross B, but B not really with A)
ABAB - Crossing pair!!! (A crosses B, B crosses A)
How it will identify crossing pair
for letter in [A, B, C,... Y, Z]:
    It will:
    Find index of first and second A (Example = A)
    Get sublist [firstindex+1:secondindex]
    For letter_2 in sublist:
        If not letter_2 repeats 2 times in list:
            +1 crossing pair

IMPORTANT crossing pair= crossing pair/2
'''
import math
original_log = input("Enter string of 52 letters: ")
log = []
for i in range(52):
    log.append(original_log[i])
pairs = 0

for letter_1 in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
    copy = log[:]
    index1 = copy.index(letter_1)
    copy.remove(letter_1)
    index2 = copy.index(letter_1)
    subset = log[index1+1:index2+1]
    if subset != []:
        for letter_2 in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            if subset.count(letter_2) == 1:
                pairs += 1
                
pairs = pairs/2
print(math.trunc(pairs))
