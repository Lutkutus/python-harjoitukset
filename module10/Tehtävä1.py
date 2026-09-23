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

h = Hissi(1, 7)
h.siirry_kerrokseen(5)
time.sleep(1)
print("Mennään takaisin alas!")
time.sleep(1)
h.siirry_kerrokseen(1)
time.sleep(1)
print("Nyt ollaan alhaalla!")