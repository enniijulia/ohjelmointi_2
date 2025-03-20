class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self,nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self,tuntimäärä):
        self.kuljettu_matka += tuntimäärä * self.tämänhetkinen_nopeus

auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(60)

auto1.kulje(1.5)

print(f'Kuljettu matka {auto1.kuljettu_matka} tuntia')