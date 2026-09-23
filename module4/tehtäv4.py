vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0:
    print("Vuosi on karkausvuosi.")

elif vuosi % 100 == 0:
    print("Vuosi ei ole karkausvuosi.")

elif vuosi % 4 == 0:
    print("Vuosi on karkausvuosi.")

else:
    print("Vuosi ei ole karkausvuosi.")

