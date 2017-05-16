class Osoba(object):
    def __init__(self, ime, god):
        self.ime = ime
        self.god = god


markoOsoba = Osoba('Marko', 14)
ivanOsoba = Osoba('Ivan', 18)

print(ivanOsoba.god - markoOsoba.god)
print (markoOsoba.ime, ivanOsoba.ime)

