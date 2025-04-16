class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja
        print(f"Päätoimittaja: {self.päätoimittaja}")


class Kirja(Julkaisu):
    def __init__(self,nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä:{self.sivumäärä}")

julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for t in julkaisut:
    t.tulosta_tiedot()
    print()