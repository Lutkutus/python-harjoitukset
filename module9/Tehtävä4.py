import random

class Auto:
   
    def __init__(self, rekisteri, huippunopeus, tamhetknop = 0, kuljettu_matka = 0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tamhetknop = tamhetknop
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, muutos):
        self.tamhetknop = self.tamhetknop + muutos

        if self.tamhetknop > self.huippunopeus:
            self.tamhetknop = self.huippunopeus

        if self.tamhetknop < 0:
            self.tamhetknop = 0

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.tamhetknop * tunnit

autot = []

for i in range(1, 11):
    rekisteri = (f"ABC-{i}")
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteri, huippunopeus)
    autot.append(auto)


kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        muutos = random.randint(-10, 15)

        auto.kiihdytä(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False


print("Sija | Rekisteri | Huippunopeus (km/h) | Nopeus (km/h) | Kuljettu matka (km)")

autot.sort(key=lambda auto: auto.kuljettu_matka, reverse=True)

sija = 1

for auto in autot:
    print(f"{sija:<5}| {auto.rekisteri:<10}| {auto.huippunopeus:<20}| {auto.tamhetknop:<14}| {auto.kuljettu_matka:<2}")
    sija = sija + 1

