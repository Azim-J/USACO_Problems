def get_data(l, type):
    global n
    for i in range(n):
        l.append(input(type + " cow {0}: ".format(i+1)))

def see_rows(g, rl, row1, row2, row3):
    for gene in g:
        gene_l = [gene[row1], gene[row2], gene[row3]]
        if gene_l not in rl:
            rl.append(gene_l)


def compare_rows(spr, nor):
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

for row1 in range(m-2):
    for row2 in range(row1+1, m-1):
        for row3 in range(row2+1, m):
            spot_row = []
            norm_row = []
            see_rows(spot_genes, spot_row, row1, row2, row3)
            see_rows(norm_genes, norm_row, row1, row2, row3)
            compare_rows(spot_row, norm_row)

print(spot_loc)
