class Isä():
    def __init__(self, auto):
        self.auto = auto

class Äiti():
    def __init__(self, linna):
        self.linna = linna

class Minä(Isä, Äiti):
    def __init__(self, auto, linna, persoonallisuus):
        Isä.__init__(self, auto)
        Äiti.__init__(self, linna)
        self.persoonallisuus = persoonallisuus

minä = Minä("Volkswagen", "Suomenlinna", "Rohkea")

print(minä.auto)
print(minä.linna)
print(minä.persoonallisuus)

