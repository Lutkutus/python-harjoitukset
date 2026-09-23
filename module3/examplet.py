import math

print("Mikä on ympyrän säde?")
säde = float(input("Säde on: "))

print("Mikä on neliön yhden sivun pituus?")
sivu = float(input("Sivun pituus on: "))

ympyrä_pintaala = round(math.pi * säde ** 2, 2)
neliö_pintaala = round(sivu ** 2, 2)

print("Ympyrän pinta-ala on: ", ympyrä_pintaala)
print("Neliön pinta-ala on: ", neliö_pintaala)
