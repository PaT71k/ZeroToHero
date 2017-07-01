class Osoba(object):
    def __init__(self, ime, god):
        self.ime = ime
        self.god = god

    def sayname(self):
        print('Dobar dan. Moje ime je {}'.format(self.ime))

    def __str__(self):
        return self.ime + self.god.__str__()

markoOsoba = Osoba('Marko', 14)
ivanOsoba = Osoba('Ivan', 18)

print(ivanOsoba.god - markoOsoba.god)
print (markoOsoba.ime, ivanOsoba.ime)

markoOsoba.sayname()
print (markoOsoba.__str__())

