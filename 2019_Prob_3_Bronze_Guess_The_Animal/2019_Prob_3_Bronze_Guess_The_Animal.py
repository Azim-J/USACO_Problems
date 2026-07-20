from itertools import combinations
'''
Get N
add input to list [[animal, len, trait1, trait2, ...], [animal2...]]
put nums in list with index [[5, 0], [2, 1] [5, 2], [1, 3]...]
investigate biggest nums:
    for each subset(big to small):
        see if other has it, if yes:
            stop, update max if needed (subset size+1)
'''

def subset(setl):
    for i in range(len(setl), 0, -1):
        a = combinations(setl, i)
        subl = []
        for tup in a:
            tupl = []
            for item in tup:
                tupl.append(item)
            subl.append(tupl)
    return subl

def compare_lists(l1, l2):
    count = 0
    for v in l1:
        if v in l2:
            count += 1
    if count == len(l1):
        return True
    else:
        return False

max_t = 0
n = int(input("N: "))
all_l = []
hold = []
for i in range(n):
    user_info = input("Animal {0}: ".format(i+1)).split()
    user_info[1] = int(user_info[1])
    hold.append(user_info[1])
    all_l.append(user_info)
all_copy = all_l
while len(all_copy) > 0:
    nums = []
    for v in all_copy:
        nums.append(v[1])
    m = all_copy[nums.index(max(nums))]
    all_copy.remove(m)
    m_traits = m[2:]
    sub_traits = subset(m_traits)
    for v1 in sub_traits:
        for v2 in all_copy:
            if compare_lists(v1, v2) and len(v1)+2 > max_t:
                max_t = len(v1)+2

print(max_t)
    
