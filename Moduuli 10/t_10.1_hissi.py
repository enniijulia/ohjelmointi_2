class Hissi:
    def __init__(self,alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def hissi_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def hissi_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -=1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self,tavoite_kerros):
        while self.nykyinen_kerros < tavoite_kerros:
            self.hissi_ylös()
        while self.nykyinen_kerros > tavoite_kerros:
            self.hissi_alas()

h = Hissi(1,11)
h.siirry_kerrokseen(4)
h.siirry_kerrokseen(1)

