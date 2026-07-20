'''
Store [Bessie, Buttercup, Belinda, Beatrice, Bella, Blue, Betsy, Sue]
Get input
Turn , ""Beatrice must be milked beside Blue" "Betsy must be milked beside Sue" into [[Beatrice, Blue], [Betsy, Sue]]
solution = 0
For every permutation:
    if works:
        if solution = 0 or solution > permutation:
            solution = permutation
'''

from itertools import permutations

def is_solution(sol, perm):
    for cow1 in sol:
        for cow2 in perm:
            if cow1 > cow2:
                return True
            if cow1 < cow2:
                return False

cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
n = int(input("Number of constraints: "))
constraints = []
for i in range(n):
    constraint = input("Constraint {0}: ".format(i+1)).split()
    constraints.append([constraint[0], constraint[5]])
    
perms = list(permutations(cows))

success = []
for perm in perms:
    valid = 1
    for constraint in constraints:
        cow1 = perm.index(constraint[0])
        cow2 = perm.index(constraint[1])
        if abs(cow1 - cow2) != 1:
            valid = 0
    if valid == 1:
        success.append(perm)
success.sort()
success = list(success[0])
for cow in success:
    print(cow)
