yritykset = 0

while yritykset < 5:
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttajatunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break

    else:
        yritykset = yritykset + 1

if yritykset == 5:
    print("Pääsy evätty")