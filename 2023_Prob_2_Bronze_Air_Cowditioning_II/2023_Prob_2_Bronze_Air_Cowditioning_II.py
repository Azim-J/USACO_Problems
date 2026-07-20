'''
get input
Put cow info in dict ( {1: 2} means Stall 1 needs to be 2 units down.)
Put air conditioners info into nested list [[2, 9, 2, 3], [1, 6, 2, 8]...]
for every subset of AC list:
    make dict like cow info dict for affected stalls
    (check) for every item in AC dict:
        if item in cow dict:
            if cow dict val > AC dict val:
            return False
'''

def int_list(l):
    for (i, v) in enumerate(l):
        l[i] = int(v)

def generate_subsets(input_set):
    # Convert the input set to a list to handle indexing
    input_list = list(input_set)
    subsets = []
    
    # Total number of subsets is 2^n (where n is the length of the input list)
    total_subsets = 1 << len(input_list)
    
    for subset_mask in range(total_subsets):
        subset = []
        for i in range(len(input_list)):
            # Check if the i-th element is in the current subset
            if subset_mask & (1 << i):
                subset.append(input_list[i])
        subsets.append(subset)
    
    return subsets

def check_ACs(ac_set):
    global cow_dict
    ac_dict = {}
    for l in ac_set:
        for i in range(l[0], l[1]+1):
            if i in ac_dict:
                ac_dict[i] += l[2]
            else:
                ac_dict[i] = l[2]
    for stall in range(99):
        want = cow_dict.get(stall+1)
        has = ac_dict.get(stall+1)
        if want != None:
            if has == None:
                return None
            elif has < want:
                return None
    cost = 0
    for ac in ac_set:
        cost += ac[3]
    return cost


user_info = input("N and M: ").split()
n = int(user_info[0])
m = int(user_info[1])
cow_dict = {}
for i in range(n):
    user_info = input("Cow {0} info: ".format(i+1)).split()
    int_list(user_info)
    for i2 in range(user_info[0], user_info[1]+1):
        if i2 in cow_dict:
            if cow_dict[i2] < user_info[2]:
                cow_dict[i2] = user_info[2]
        else:
            cow_dict[i2] = user_info[2]

            
ac_list = []
for i in range(m):
    user_info = input("AC {0} info: ".format(i+1)).split()
    int_list(user_info)
    ac_list.append(user_info)

subset_list = generate_subsets(ac_list)
money_list = []
for sub in subset_list:
    money = check_ACs(sub)
    if money != None:
        money_list.append(money)
print(min(money_list))

'''
|2|2|2|2|2|0|3|3|3|0|
|4|4|2|2|2|2|2|2|2|0|
'''
