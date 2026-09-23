def laske_summa(lista):
    summa = 0

    for luku in lista:
        summa = summa + luku

    return summa

luvut = [4, 7, 4, 444, 11, 678]

tulos = laske_summa(luvut)

print(tulos)
