leiviska = int(input("Anna leiviskät: "))

naula = int(input("Anna naulat: "))

luoti = float(input("Anna luodit: "))

grammat = (leiviska * 20 * 32 + naula *32 + luoti) * 13.3
kilot = int(grammat // 1000)
ekstra_grammat = round(grammat % 1000, 2)

print("Massa nykymittojen mukaan:")
print(kilot, "kilogrammaa ja", ekstra_grammat, "grammaa")
