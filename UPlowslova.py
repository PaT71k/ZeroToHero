def mala_velika(s):
    d = {"velika":0, "mala":0}
    for c in s:
        if c.isupper():
            d["velika"]+=1
        elif c.islower():
            d["mala"]+=1
        else: pass

    return d

s = input("Upiši rečenicu: ")
rjesenje = mala_velika(s)
print ("Rečenica: ", s)
print ("Broj velikih slova: ", rjesenje["velika"])
print ("Broj malih slova: ", rjesenje ["mala"])



