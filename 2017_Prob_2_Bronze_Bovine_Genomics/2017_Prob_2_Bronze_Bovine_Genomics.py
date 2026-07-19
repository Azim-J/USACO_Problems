'''Logic
Get data
Add spotty cow to list 1
Add normal cow to list 2
go through spotty cow list row i, add genome type to list 3
go through spotty cow list row i, add genome type to list 4
compare list 3 & 4, add to spot_loc accordingly'''

def get_data(l, type):
    global n
    for i in range(n):
        l.append(input(type + " cow {0}: ".format(i+1)))

def see_row(g, rl, row):
    for gene in g:
        cur_gene = gene[row]
        if cur_gene not in rl:
            rl.append(cur_gene)

def compare_row(spr, nor):
    global spot_loc
    for g in spr:
        if g in nor:
            return 0
    spot_loc += 1
    
spot_loc = 0
user_info = input("N & M: ").split()
n = int(user_info[0])
m = int(user_info[1])
spot_genes = []
norm_genes = []
get_data(spot_genes, "Spotty")
get_data(norm_genes, "Normal")

for row in range(m):
    spot_row = []
    norm_row = []
    see_row(spot_genes, spot_row, row)
    see_row(norm_genes, norm_row, row)
    compare_row(spot_row, norm_row)

print(spot_loc)
