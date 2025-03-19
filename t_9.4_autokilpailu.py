import random

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

    def kulje(self, tunnit):
            self.kuljettu_matka += self.tämänhetkinen_nopeus * tunnit

autot = []
for i in range(1,11):
    huippunopeus = random.randint(100,200)
    autot.append(Auto(f'ABC-{i}', huippunopeus ))

tunti = 0
kilpailu_käynnissä = True

while kilpailu_käynnissä:
    tunti += 1
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_käynnissä = False

print("\nKilpailu päättyi!\n")
print(f"Kilpailuun kului {tunti} tuntia.")
print("\nLopputulokset:")
print(f"{'Rekisteri':<10}{'Huippunopeus (km/h)':<20}{'Kuljettu matka (km)':<20}{'Nopeus (km/h)'}")

for auto in autot:
    print(f"{auto.rekisteritunnus:<10}{auto.huippunopeus:<20}{auto.kuljettu_matka:<20.1f}{auto.tämänhetkinen_nopeus}")
