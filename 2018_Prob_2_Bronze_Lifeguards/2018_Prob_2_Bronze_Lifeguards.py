'''Logic
Get N
Put N cow starttime into list
Put N cow endtime into list
max_time=0
Repeat:
Try to fire one cow
for t in range 1000
    see if works in min list
        goto corresponding max list
        if works
            add time to max time'''

def verify(t):
    global start_t, end_t
    for i in range(len(end_t)):
        s = start_t[i]
        e = end_t[i]
        if s <= t and t+1 <= e:
            return True
    return False
                

n = int(input("N: "))
start_t = []
end_t = []
for i in range(n):
    userinfo = input("Lifeguard {0} times: ".format(i+1)).split()
    start_t.append(int(userinfo[0]))
    end_t.append(int(userinfo[1]))
    
max_time = 0
f_cow = []
for i in range(n):
    cur_time = 0
    f_cow.append([start_t[i], end_t[i]])
    start_t.pop(i)
    end_t.pop(i)
    for t in range(1000):
        if verify(t) == True:
            cur_time += 1
    if cur_time > max_time:
        max_time = cur_time
    start_t.insert(i, f_cow[0][0])
    end_t.insert(i, f_cow[0][1])
    f_cow.clear()

print(max_time)
