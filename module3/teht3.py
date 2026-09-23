print("Mikä on suorakulmion kanta?")
kanta_str = input("Suorakulmion kanta: ")
print("Mikä on suorakulmion korkeus?")
korkeus_str = input("Suorakulmion korkeus: ")
kanta = float(kanta_str)
korkeus = float(korkeus_str)
piiri = kanta * 2 + korkeus * 2
pintaala = kanta * korkeus
print("Suorakulmion piiri on: " + str(piiri))
print("Suorakulmion pinta-ala on: " + str(pintaala))
