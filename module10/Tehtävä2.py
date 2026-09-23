import time

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alinkerros = alin_kerros
        self.ylinkerros = ylin_kerros
        self.nykyinenkerros = alin_kerros

    def kerros_ylös(self):
        time.sleep(1)
        self.nykyinenkerros = self.nykyinenkerros + 1
        print(f"Hissi on nyt kerroksessa {self.nykyinenkerros}")

    def kerros_alas(self):
        time.sleep(1)
        self.nykyinenkerros = self.nykyinenkerros - 1
        print(f"Hissi on nyt kerroksessa {self.nykyinenkerros}")


    def siirry_kerrokseen(self, kohdekerros):
        while self.nykyinenkerros < kohdekerros:
            self.kerros_ylös()

        while self.nykyinenkerros > kohdekerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []

        for i in range(hissien_maara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

        
talo = Talo(1, 7, 3)


talo.aja_hissia(1, 5)
time.sleep(1)
talo.aja_hissia(2, 3)
time.sleep(1)

