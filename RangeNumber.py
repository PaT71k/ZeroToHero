def ran_check(broj, manji, veci):
    return broj in range(manji, veci)

tekst = "Upiši broj: "
unosBroj = input(tekst)
Broj = int(unosBroj)

tekst2 = "Upiši manji broj: "
unosBrojmanji = input (tekst2)
Brojmanji = int(unosBrojmanji)

tekst3 = "Upiši veći broj: "
unosBrojveci = input(tekst3)
Brojveci = int(unosBrojveci)

if ran_check(Broj,Brojmanji,Brojveci):
    print("Broj je u rasponu¨!")
else:
    print("Broj nije u rasponu!")
