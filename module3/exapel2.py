print("Kuinka monta kiloa banaaneja?")
banaanit = int(input("Banaaneja: "))

print("Kuinka monta kiloa omenoita?")
omenat = int(input("Omenoita: "))

print("Kuinka monta kiloa appelsiineja?")
appelsiinit = int(input("Appelsiineja: "))

banaani_hinta = round(banaanit * 2.85, 2)
omena_hinta = round(omenat * 3.15, 2)
appelsiini_hinta = round(appelsiinit * 4.05, 2)

hinta_yhteensä = round(banaani_hinta + omena_hinta + appelsiini_hinta, 2)
print(f"Banaanien hinta on: {banaani_hinta: .2f}")
print(f"Omenien hinta on: {omena_hinta: .2f}")
print(f"Appelsiinien hinta on: {appelsiini_hinta: .2f}")
print(f"Hinta yhteensä on: {hinta_yhteensä: .2f}")




