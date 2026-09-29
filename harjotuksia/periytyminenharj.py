
class Varusmies:
    def __init__(self, nimi, sukunimi):
        self.nimi = nimi
        self.sukunimi = sukunimi

    def ilmoita_tiedot(self):
        print(f"{self.nimi} {self.sukunimi}")

class Miehisto(Varusmies):
    def __init__(self, nimi, sukunimi, arvo="Sotamies"):
        super().__init__(nimi, sukunimi)
        self.arvo = arvo

    def ilmoita_tiedot(self):
        super().ilmoita_tiedot()
        print(f"{self.arvo}")

class Henkilökunta(Miehisto):
    def __init__(self, nimi, sukunimi, arvo, tehtävä):
        super().__init__(nimi, sukunimi, arvo)
        self.tehtävä = tehtävä

    def ilmoita_tiedot(self):
        super().ilmoita_tiedot()
        print(f"{self.tehtävä}")

miehistö1 = Miehisto(input("Anna etunimesi: "), input("Anna sukunimesi: "), input("Anna sotilasarvosi: "))

miehistö1.ilmoita_tiedot()

print()

henk1 = Henkilökunta("Sofia", "Sotilas", "Vääpeli", "Logistiikka")
henk1.ilmoita_tiedot()
