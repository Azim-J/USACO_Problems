'''
iii7
'''
def recover(start, end):
    global length, log, maxb, minb
    if end == length-1:
        maxb += end-start+1
        if start == 0:
            minb = 1
        return 1
    elif start == 0:
        key = log[end+1] # The key to solving the problem!
        if key > end+1:
            return None
        if key == end+1:
            minb = 1
            maxb = 1
            return 1
        if key < end+1:
            minb = 2
            maxb = end-start-key+2
            return 1
    else:
        key = log[end+1]
        if key < end-start+1:
            if key-end+start-1 > 1:
                minb += 1
            if key == 0:
                minb -= 1
                maxb -= 1
            minb += 1
            maxb += end-start-key+2
            return 1
        elif key == end-start+1:
            minb += 1
            maxb += 1
            return 1
        return 1
def use_recover():
    global log, length, maxb, minb
    i = 0
    while i < length:
        if log[i] == -1:
            s = i
            while log[i] == -1:
                i += 1
                if i == length:
                    break
            i -= 1
            e = i
            check = 0
            check = recover(s, e)
            if check == None:
                print(-1)
                return ""
        elif log[i] == 0:
            minb += 1
            maxb += 1
            
        i += 1
        
    print(minb, maxb)

length = int(input("Length: "))
log = input("Partial log: ").split()
for i in range(length):
    log[i] = int(log[i])
minb = 0
maxb = 0
if log[0] > 0:
    print(-1)
else:
    use_recover()            
