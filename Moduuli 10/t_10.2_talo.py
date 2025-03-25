import random
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def hissi_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def hissi_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, tavoite_kerros):
        while self.nykyinen_kerros < tavoite_kerros:
            self.hissi_ylös()
        while self.nykyinen_kerros > tavoite_kerros:
            self.hissi_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for i in range(hissien_lkm)]

    def aja_hissiä(self, hissi_num, kohdekerros):
        if 0 <= hissi_num < len(self.hissit):
            print(f"Ajetaan hissiä {hissi_num} kerrokseen {kohdekerros}")
            self.hissit[hissi_num].siirry_kerrokseen(kohdekerros)


talo = Talo(1, 11, 4)

talo.aja_hissiä(1,5)
talo.aja_hissiä(2,8)
talo.aja_hissiä(3,2)

talo.aja_hissiä(1,1)
talo.aja_hissiä(2,1)
talo.aja_hissiä(3,1)