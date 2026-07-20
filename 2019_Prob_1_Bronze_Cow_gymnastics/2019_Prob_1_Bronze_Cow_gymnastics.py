def examine(meet):
    global cur_cow, pair_cow
    cur_rank = meet.index(str(cur_cow))
    pair_rank = meet.index(str(pair_cow))
    if cur_rank < pair_rank:
        return "c"
    else:
        return "p"

consis_pair = 0
userinfo = (input("K and N: ")).split()
k = int(userinfo[0])
n = int(userinfo[1])
meets = []

for i in range(k):
    meets.append(input("Meeting {0}: ".format(i+1)))

for cur_cow in range(n):
    cur_cow += 1
    pair_cow = cur_cow + 1
    while pair_cow < n+1:
        check_consis = examine(meets[0])
        for i in range(len(meets)):
            if examine(meets[i]) != check_consis:
                check_consis = 0
        if check_consis != 0:
            consis_pair += 1
        pair_cow += 1
print(consis_pair)
