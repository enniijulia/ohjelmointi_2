class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

auto1 = Auto("ABC-123", "142 km/h")

print(f'Auton {auto1.rekisteritunnus} huippunopeus on {auto1.huippunopeus}. Tämänhetkinen nopeus {auto1.tämänhetkinen_nopeus} ja kuljettu matka {auto1.kuljettu_matka}')
