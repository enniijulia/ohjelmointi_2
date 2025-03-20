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

auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print(f'Auton nopeus kiihdytyksien jälkeen: {auto1.tämänhetkinen_nopeus} km/h')
auto1.kiihdytä(-200)
print(f'Auton nopeus hätäjarrutuksen jälkeen: {auto1.tämänhetkinen_nopeus} km/h')
