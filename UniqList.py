def uniq_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

l = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5]
rjesenje = uniq_list(l)
print (rjesenje)




