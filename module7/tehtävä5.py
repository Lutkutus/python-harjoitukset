def karsi_parittomat(lista):
    uusi_lista = []

    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista


alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8]

karsittu = karsi_parittomat(alkuperainen)

print("Alkuperäinen lista:", alkuperainen)
print("Karsittu lista:", karsittu)
