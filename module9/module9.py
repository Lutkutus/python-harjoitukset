
class Hero:
    sankarien_määrä = 0

    def __init__(self, nimi, tyyppi, ability, aseaani, huudahdus="Hei!"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.ability = ability
        self.huudahdus = huudahdus
        self.aseaani = aseaani
        Hero.sankarien_määrä = Hero.sankarien_määrä + 1

    def huuda(self, kerrat):
        for i in range(kerrat):
            print(f"{self.huudahdus}")

    def ase(self):
        print(self.aseaani)


hero1 = Hero("Junkrat", "DPS", "Rip Tire", "Blong... Boom!", "Beep Beep Boom Boom")
hero2 = Hero("Roadhog", "Tankki", "Hookki", "PHHANG", "BUHHAHHAHHAAA")

print(f"{hero1.nimi} on {hero1.tyyppi} ja hänellä on {hero1.ability} hän spämmää {hero1.huudahdus}")
print(f"{hero2.nimi} on {hero2.tyyppi} ja hänellä on {hero2.ability} hän spämmää {hero2.huudahdus}")

hero1.huuda(5)
hero1.ase()

hero2.huuda(2)
hero2.ase()

print(f"Sankarien määrä joukkueessa: {Hero.sankarien_määrä}")
