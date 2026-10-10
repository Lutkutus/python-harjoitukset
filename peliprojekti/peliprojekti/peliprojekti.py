import random

from pathlib import Path

kansio = Path(__file__).parent

class Esine:
    def __init__(self, nimi, paino, arvo=0):
        self.nimi = nimi
        self.paino = paino
        self.arvo = arvo

class Huone:
    def __init__(self, nimi, esine, kuva):
        self.nimi = nimi
        self.esine = esine
        self.kuva = kuva

class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.reppu = []
        self.sijainti = sijainti
        self.tehtava = None
        self.mummon_tehtava = "ei aloitettu"
        self.raha = 0.0
        self.myyja_tavattu = False
        self.ending = None

    def liiku(self, huone):
        self.sijainti = huone
        print(f"Menit paikkaan {huone.nimi}")
        print(huone.kuva)

    def keraa_esine(self):
        if self.sijainti.esine != None:
            self.reppu.append(self.sijainti.esine)
            print(f"Löysit esineen {self.sijainti.esine.nimi}!")
            self.sijainti.esine = None
        else:
            print("Täällä ei ole mitään.")

#Seivaus
def tallenna_peli(pelaaja, roskikset):
    with open(kansio / "save.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(pelaaja.sijainti.nimi + "\n")

        tiedosto.write(",".join(str(roskis) for roskis in roskikset) + "\n")

        if pelaaja.tehtava is None:
            tiedosto.write("Ei tehtavaa\n")
        else:
            tiedosto.write(pelaaja.tehtava + "\n")

        tiedosto.write(str(pelaaja.raha) + "\n")

        for esine in pelaaja.reppu:
            tiedosto.write(f"{esine.nimi};{esine.paino};{esine.arvo}\n")

        tiedosto.write("Mummon tehtävä;" + pelaaja.mummon_tehtava + "\n")
        tiedosto.write("Myyjä tavattu;" + str(pelaaja.myyja_tavattu) + "\n")


    print("Peli tallennettu!")

#Lataus
def lataa_peli(pelaaja, piritori, puisto, smarket, roskikset):
    try:
        with open(kansio / "save.txt", "r", encoding="utf-8") as tiedosto:
            rivit = tiedosto.readlines()

        pelaaja.nimi = rivit[0].strip()

        sijainti = rivit[1].strip()

        if sijainti == "Piritori":
            pelaaja.sijainti = piritori

        elif sijainti == "Puisto":
            pelaaja.sijainti = puisto

        elif sijainti == "S-Market":
            pelaaja.sijainti = smarket

        # Ladataan roskisten tila

        tallennetut_roskikset = rivit[2].strip().split(",")

        for i in range(3):
            roskikset[i] = tallennetut_roskikset[i] == "True"

        # Ladataan tehtävä

        tehtava = rivit[3].strip()

        if tehtava == "Ei tehtavaa":
            pelaaja.tehtava = None
        else:
            pelaaja.tehtava = tehtava


        # Ladataan reppu
        pelaaja.raha = float(rivit[4].strip())

        pelaaja.mummon_tehtava = "ei aloitettu"
        pelaaja.myyja_tavattu = False
        pelaaja.ending = None

        for rivi in rivit[5:]:
            tiedot = rivi.strip().split(";")

            if tiedot[0] == "Mummon tehtävä":
                pelaaja.mummon_tehtava = tiedot[1]

            elif tiedot[0] == "Myyjä tavattu":
                pelaaja.myyja_tavattu = tiedot[1] == "True"

        for rivi in rivit[5:]:
            tiedot = rivi.strip().split(";")

            if tiedot[0] == "Mummon tehtävä":
                pelaaja.mummon_tehtava = tiedot[1]

            elif tiedot[0] == "Myyjä tavattu":
                pelaaja.myyja_tavattu = tiedot[1] == "True"

            else:
                nimi = tiedot[0]
                paino = float(tiedot[1])
                arvo = float(tiedot[2])

                esine = Esine(nimi, paino, arvo)
                pelaaja.reppu.append(esine)

        # Palautetaan Piritorin alkuperäinen tila ensin
        piritori.esine = Esine("Lääkeruisku", 0.1)

        if pelaaja.mummon_tehtava == "valmis":
            piritori.esine = None

        # Jos ruisku on jo repussa, sitä ei saa uudestaan

        for esine in pelaaja.reppu:
            if esine.nimi == "Lääkeruisku":
                piritori.esine = None


        print("Peli ladattu!")
        print(f"Tervetuloa takaisin {pelaaja.nimi}!")
        print(f"Olet paikassa {pelaaja.sijainti.nimi}")
        print(pelaaja.sijainti.kuva)

        return True

    except FileNotFoundError:
        print("Tallennusta ei löytynyt.")
        return False

#Kaikki muut funktiot

def aloitus_keskustelu(pelaaja):
    kysymys1 = False
    kysymys2 = False

    print("\nHeräät Piritorin penkiltä.")
    print("Viereisellä penkillä istuu varsin omituinen hemmo.")
    print("Menet juttelemaan hänelle.")

    while True:
        print("\nMitä haluat kysyä?")
        print("1. Mikä on elämän tarkoitus?")
        print("2. Kuka sää oot?")

        valinta = input("Valitse: ")

        if valinta == "1":
            print('\n"Voi kuules... Elämän tarkoitus on olla hyvä ihminen."')
            kysymys1 = True

        elif valinta == "2":
            print('\n"Ei sillä ole väliä."')
            kysymys2 = True

        else:
            print("Tuntematon valinta.")

        if kysymys1 == True and kysymys2 == True:
            print("\nHemmo katsoo sinua hetken.")
            print('"Kuule, voisikkos jeesaa mua yhessä jutussa?"')
            print('"Käyppä ostaa mulle bisse tosta Ässästä."')
            print("\nHuomaat, että sinulla ei ole yhtään rahaa.")

            pelaaja.tehtava = "Hae Hemmolle bisse"

            print(f"\nSait tehtävän: {pelaaja.tehtava}")
            break

def nayta_reppu(pelaaja):
    print(f"Rahaa: {pelaaja.raha:.2f} €")

    if len(pelaaja.reppu) == 0:
        print("Reppu on tyhjä.")

    else:
        print("Repussa on:")

        for esine in pelaaja.reppu:
            print(esine.nimi)

def s_market(pelaaja, roskikset, piritori):
    if pelaaja.tehtava == "Hemmon tehtävät valmis":
        auta_nalkaista(pelaaja)

    while pelaaja.ending is None:
        print("\nS-Market")
        print("1. Mene kauppaan")
        print("2. Palauta pullot")
        print("3. Poistu")

        valinta = input("Valitse: ")

        if valinta == "1":
            kauppa(pelaaja)

        elif valinta == "2":
            palauta_pullot(pelaaja, roskikset)

        elif valinta == "3":
            print("Poistuit S-Marketista.")
            pelaaja.liiku(piritori)
            break

        else:
            print("Tuntematon valinta.")
    
def palauta_pullot(pelaaja, roskikset):
    palautusraha = 0
    uusi_reppu = []

    for esine in pelaaja.reppu:

        if esine.nimi == "Tölkki" or esine.nimi == "Pieni pullo" or esine.nimi == "Iso pullo":
            palautusraha += esine.arvo

        else:
            uusi_reppu.append(esine)

    if palautusraha == 0:
        print("Sinulla ei ole palautettavia pulloja.")

    else:
        pelaaja.reppu = uusi_reppu

        pelaaja.raha += palautusraha
        pelaaja.raha = round(pelaaja.raha, 2)

        print(f"Palautit pullot ja sait {palautusraha:.2f} €.")
        print(f"Sinulla on nyt {pelaaja.raha:.2f} €.")

        # Roskikset täyttyvät uudestaan
        for i in range(3):
            roskikset[i] = False

        print("Puiston roskiksiin on ilmestynyt taas tavaraa...")

def kauppa(pelaaja):
    while pelaaja.ending is None:
        print("\nS-Market")
        print(f"Rahaa: {pelaaja.raha:.2f} €")
        print("1. Bisse 1,04 €")
        print("2. Marlboro Punanen 11,30 €")
        print("3. Poistu kaupasta")
        if lopetukset_auki(pelaaja):
            print(f"4. 100-pack bisseä — kaikki rahasi ({pelaaja.raha:.2f} €)")
        valinta = input("Mitä haluat ostaa? ").strip()
        if valinta == "1":
            osta_tuote(pelaaja, "Bisse", 0.33, 1.04)
        elif valinta == "2":
            osta_tuote(pelaaja, "Marlboro Punanen", 0.12, 11.30)
        elif valinta == "3":
            print("Poistuit kaupasta.")
            return
        elif valinta == "4" and lopetukset_auki(pelaaja):
            if pelaaja.raha <= 0:
                print("Sinulla ei ole rahaa ostokseen.")
            elif input("Käytätkö varmasti kaikki rahasi 100 bisseen? k/e: ").strip().lower() == "k":
                pelaaja.raha = 0.0
                for i in range(100):
                    pelaaja.reppu.append(Esine("Bisse", 0.33))
                print("\nOstit sata bisseä ja käytit viimeisenkin eurosi.")
                print("Ilta venyy... Lopulta kaikki sumenee...")
                print("\nBAD ENDING - Näin tapahtui viimeksikin.")
                pelaaja.ending = "bad"
        else:
            print("Tuntematon valinta.")

def osta_tuote(pelaaja, nimi, paino, hinta):
    if pelaaja.raha >= hinta:
        pelaaja.raha -= hinta
        pelaaja.raha = round(pelaaja.raha, 2)

        tuote = Esine(nimi, paino)
        pelaaja.reppu.append(tuote)

        print(f"Ostit tuotteen: {nimi}")
        print(f"Rahaa jäljellä: {pelaaja.raha:.2f} €")

    else:
        print(f"Sinulla ei ole tarpeeksi rahaa.")
        print(f"{nimi} maksaa {hinta:.2f} €.")

def puhu_hemmolle(pelaaja):

    #Hemmon eka tehtävä
    if pelaaja.tehtava == "Hae Hemmolle bisse":

        for esine in pelaaja.reppu:
            if esine.nimi == "Bisse":
                pelaaja.reppu.remove(esine)

                print('\n"Ai, että... Bisseä!."')
                print("Annoit bissen hemmolle.")

                pelaaja.raha += 3.30
                pelaaja.raha = round(pelaaja.raha, 2)

                print("Hemmo antoi sinulle 3,30 €.")

                pelaaja.tehtava = "Hae hemmolle Marlboro Punanen ja 2 bisseä"

                print('\n"Kuules, mulla olis sulle vielä yks homma."')
                print('"Hae mulle Marlboro Punane ja pari bisseä lisää."')
                print(f"\nUusi tehtävä: {pelaaja.tehtava}")
                return

        print('\n"No missäs se mun bisse on?"')

    #Hemmon toka tehtävä

    elif pelaaja.tehtava == "Hae hemmolle Marlboro Punanen ja 2 bisseä":

        bisseja = 0
        marlboro = None

        for esine in pelaaja.reppu:

            if esine.nimi == "Bisse":
                bisseja += 1

            elif esine.nimi in ("Marlboro Punanen", "Marlboron Punane"):
                marlboro = esine


        if bisseja >= 2 and marlboro is not None:

            pelaaja.reppu.remove(marlboro)

            poistettu = 0

            for esine in pelaaja.reppu[:]:
                if esine.nimi == "Bisse" and poistettu < 2:
                    pelaaja.reppu.remove(esine)
                    poistettu += 1

            print("\nAnnoit hemmolle Marlboro Punasen ja 2 bisseä.")
            print('"Nyt alkaa näyttää hyvältä."')

            pelaaja.raha += 17.50
            pelaaja.raha = round(pelaaja.raha, 2)


            print("Hemmo antoi sinulle 17.50 €!")

            aloita_piritehtava(pelaaja) 
        
        else:
            
            print('\n"Ei sulla vielä oo kaikkea mitä mä pyysin."')

            if marlboro is None:
                print("Puuttuu: Marlboron Punanen")

            if bisseja < 2:
                print(f"Puuttuu bissejä: {2 - bisseja}")

    elif pelaaja.tehtava == "Hemmon seuraava tehtävä":
        # Vanha tallennus saattoi jäädä tähän aiempaan välivaiheeseen.
        aloita_piritehtava(pelaaja)

    elif pelaaja.tehtava == "Hae Hemmolle piriä":
        piri = next((e for e in pelaaja.reppu if e.nimi == "Piri"), None)
        if piri is None:
            print('"Käy siellä puistossa. Se tyyppi osaa auttaa."')
            print("Tarvitset ostokseen 30,00 €.")
        else:
            pelaaja.reppu.remove(piri)
            pelaaja.raha = round(pelaaja.raha + 120, 2)
            pelaaja.tehtava = "Hemmon tehtävät valmis"
            print("\nAnnoit pirin Hemmolle.")
            print('"Kiitti sä oot nyt kyl blessannu mua hirveesti"')
            print("Hemmo antaa sinulle 120,00 €.")
            print('"Kannattaa käyttää ne harkitusti."')
            print(f"Sinulla on nyt {pelaaja.raha:.2f} €.")
            print("\nHemmon tehtävät on tehty!")

    elif lopetukset_auki(pelaaja):
        print('"Kiitti vielä. Muista käyttää ne rahat harkitusti."')

    else:
        print('"Ei mulla just nyt oo sulle mitään."')

def puhu_mummolle(pelaaja):

    if pelaaja.mummon_tehtava == "ei aloitettu":

        print('\n"Voi hyvänen aika... Olen kadottanut lääkeruiskuni."')
        print('"Se taisi jäädä jonnekin Piritorille."')
        print('"Voisitko etsiä sen minulle?"')

        pelaaja.mummon_tehtava = "etsi ruisku"

        print("\nSait tehtävän: Etsi Mummon kadonnut lääkeruisku.")


    elif pelaaja.mummon_tehtava == "etsi ruisku":

        ruisku = None

        for esine in pelaaja.reppu:
            if esine.nimi == "Lääkeruisku":
                ruisku = esine


        if ruisku is not None:

            pelaaja.reppu.remove(ruisku)

            print('\n"Siinähän se on!"')
            print('"Kiitos kun löysit ruiskuni."')

            print('\n"Minulla taisi olla täällä viiden euron seteli..."')
            print("Mummo kaivaa taskujaan ja antaa sinulle setelin.")

            pelaaja.raha += 10
            pelaaja.raha = round(pelaaja.raha, 2)

            print("\nHuomaat, että Mummo antoikin vahingossa 10 euroa.")
            print("Et sano asiasta mitään.")
            print(f"Sinulla on nyt {pelaaja.raha:.2f} €.")

            pelaaja.mummon_tehtava = "valmis"

            print("\nMummon tehtävä suoritettu!")


        else:

            print('\n"Etkö ole vielä löytänyt ruiskuani?"')
            print('"Kannattaa tutkia Piritoria."')


    elif pelaaja.mummon_tehtava == "valmis":

        print('"Kiitos vielä ruiskuni löytämisestä!"')

def puhu_myyjalle(pelaaja):
    if pelaaja.tehtava != "Hae Hemmolle piriä":
        return
    if not pelaaja.myyja_tavattu:
        print('\nSanot: "Se Piritorilla istuva äijä lähetti mut."')
        print('"Joo, thats my bro. Se tekis 30 euroa."')
        pelaaja.myyja_tavattu = True
    if any(e.nimi == "Piri" for e in pelaaja.reppu):
        print('"Veli sullahan on se jo."')
        return
    print(f"\nRahaa: {pelaaja.raha:.2f} €. Piri maksaa 30,00 €.")
    print("1. Osta\n2. Poistu")
    valinta = input("Valitse: ").strip()
    if valinta == "1":
        if pelaaja.raha < 30:
            print(f"Rahaa puuttuu vielä {30 - pelaaja.raha:.2f} €. Voit palata myöhemmin.")
        else:
            osta_tuote(pelaaja, "Piri", 0.01, 30.00)
            print("Vie ostos Hemmolle Piritorille.")
    elif valinta != "2":
        print("Tuntematon valinta.")

def puhu(pelaaja):
    if pelaaja.sijainti.nimi == "Piritori":
        print("\nKenelle haluat puhua?\n1. Hemmo\n2. Poistu")
        valinta = input("Valitse: ").strip()
        if valinta == "1":
            puhu_hemmolle(pelaaja)
        elif valinta == "2":
            print("Poistuit keskustelusta.")
        else:
            print("Tuollaista henkilöä ei ole.")
    elif pelaaja.sijainti.nimi == "Puisto":
        print("\nKenelle haluat puhua?\n1. Mummo\n2. Poistu")
        if pelaaja.tehtava == "Hae Hemmolle piriä":
            print("3. Puiston tyyppi")
        valinta = input("Valitse: ").strip()
        if valinta == "1":
            puhu_mummolle(pelaaja)
        elif valinta == "2":
            print("Poistuit keskustelusta.")
        elif valinta == "3" and pelaaja.tehtava == "Hae Hemmolle piriä":
            puhu_myyjalle(pelaaja)
        else:
            print("Tuollaista henkilöä ei ole.")
    elif pelaaja.sijainti.nimi == "S-Market":
        if lopetukset_auki(pelaaja):
            auta_nalkaista(pelaaja)
        else:
            print("Täällä ei ole ketään, jolle haluaisit puhua.")


    elif pelaaja.sijainti.nimi == "S-Market":
        print("Täällä ei ole ketään, jolle haluaisit puhua.")

def tutki(pelaaja, roskikset):
    print(f"Lähdit tutkimaan paikkaa {pelaaja.sijainti.nimi}.")

    if pelaaja.sijainti.nimi == "Puisto":
        tutki_roskis(pelaaja, roskikset)

    elif pelaaja.sijainti.nimi == "S-Market":
        print("Täällä ei ole mitään tutkittavaa.")

    else:
        pelaaja.keraa_esine()

def tutki_roskis(pelaaja, roskikset):
    roskis = input("Minkä roskiksen tutkit? 1, 2 vai 3: ")

    if roskis not in ["1", "2", "3"]:
        print("Tuollaista roskista ei ole.")
        return

    numero = int(roskis) - 1

    if roskikset[numero] == True:
        print("Roskis on tyhjä.")

    else:
        roskikset[numero] = True

        loyto = random.choice([Esine("Tölkki", 0.02, 0.10), Esine("Pieni pullo", 0.05, 0.20), Esine("Iso pullo", 0.1, 0.45)])

        pelaaja.reppu.append(loyto)

        print(f"Löysit: {loyto.nimi}!")
        print(f"Sen pantti on {loyto.arvo:.2f} €")

def lue_tiedosto(nimi):
    try:
        with open(kansio / nimi, "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())

    except FileNotFoundError:
        print(f"Tiedostoa {nimi} ei löytynyt.")

def lopetukset_auki(pelaaja):
    return pelaaja.tehtava == "Hemmon tehtävät valmis"

def aloita_piritehtava(pelaaja):
    pelaaja.tehtava = "Hae Hemmolle piriä"
    print('\n"Vielä yks juttu. Voisitko hakee mulle piriä?"')
    print('"Puistosta löytyy yks tyyppi, jolta sitä vois hakee. Sano et mä lähetin sut."')
    print("\nSait tehtävän: Hae Hemmolle piriä.")
    print("Puistoon on ilmestynyt uusi tyyppi.")

def auta_nalkaista(pelaaja):
    if pelaaja.tehtava != "Hemmon tehtävät valmis":
        return

    print("\nNäet seinää vasten istuvan tyypin, joka...")
    # Kirjoita tähän lisää omaa tekstiä print-komennoilla.

    print(f"Sinulla on {pelaaja.raha:.2f} €.")
    vastaus = input("Haluatko lahjoittaa kaikki rahasi? k/e: ").lower()

    if vastaus == "k":
        if pelaaja.raha > 0:
            print(f"Lahjoitit hänelle {pelaaja.raha:.2f} €.")
            pelaaja.raha = 0.0
            pelaaja.ending = "good"
            print("GOOD ENDING - olit hyvä ihminen!")

        else:
            print("Sinulla ei ole rahaa lahjoitettavaksi.")

    else:
        print("Jatkat matkaa kauppaan.")

def lahde_kamppiin(pelaaja, piritori):
    if pelaaja.tehtava != "Hemmon tehtävät valmis":
        return

    if pelaaja.sijainti != piritori:
        print("Metroasemalle pääsee Piritorilta.")
        return

    metroasema = Huone("Metroasema", None, "")
    pelaaja.liiku(metroasema)

    while True:
        print("\n1. Kävele laiturille")
        print("2. Palaa Piritorille")
        valinta = input("Valitse: ")

        if valinta == "1":
            print("\nKävelet laiturille.")
            print(metro_kuva)
            print("Oletko varma, HSL a-b lippu on nykyään 100 euroa?")
            vastaus = input("Ostatko lipun ja lähdet Kamppiin? k/e: ").lower()

            if vastaus == "k":
                if pelaaja.raha >= 100:
                    pelaaja.raha -= 100
                    pelaaja.raha = round(pelaaja.raha, 2)
                    pelaaja.sijainti = Huone("Kamppi", None, "")
                    pelaaja.ending = "mid"

                    print("Ostit lipun ja nousit metroon.")
                    print("Saavut Kamppiin. Piritori jää taakse.")
                    print("MID ENDING")
                    return

                else:
                    print("Sinulla ei ole tarpeeksi rahaa.")

            elif vastaus == "e":
                print("Et ostanut lippua.")

            else:
                print("Tuntematon valinta.")

        elif valinta == "2":
            pelaaja.liiku(piritori)
            return

        else:
            print("Tuntematon valinta.")

#Visuaalit

piritori_kuva = r"""
    ===========================================
                     Piritori
    ===========================================
                          
 /----------------/------------------/--------------/|
/                /                  /              / |
|---------------|------------------|--------------|  |
|               |                  |              |  |
| []    []   [] |  [] [] [] [] []  |  []  []  []  |  |
|               |                  |              |  |
| []    []   [] |  []    []    []  |  []  []  []  |  |
|               |                  |              |  /
|  1   ___      |   2   ___        |   3  ___     | /
|______|_|______|_______| |________|______| |_____|/
        

___________________________________________________
 _________        ________
/________/|      /_______/|  
|       |        |       |   /------------------/|
                            /------------------/ |
                            |                 |  |
                            |      Hissit     |  |
                            |      Metroon    |  /
                            |                 | /
                            |_________________|/

__________________________________________________

 /-----------------------------------------------/|
/-----------------------------------------------/ |
|  __________________       S-Market            | |
|  |                |         _____             | |
|  |________________|         |   |             | /  
|_____________________________|___|_____________|/
            
"""
puisto_kuva = r"""
    ===================================
                  Puisto
    ===================================

_________________________________________________
|__|____|__|_|___|__|__|___|_|____|__|___|__|___| 
|_|___|___|___|___|___|___|____|_|__|___|_____|_|
                                     __
      /////                        _(__)_
        ________        ////      (_)__(_)
       /_______/|      _=_           ||
       |      |        |_|  1        ||
___________________________              /////
      .           .        \____________________
________________________ .      .        .
                        \________    .
    _=_                         |            .
    |_|  2    /\    ////        |      .
             /__\               \_______________
            /____\                        _=_
            /____\                        |_|  3
  ////      /____\         /////      
              ||                       /////
_________________________________________________
|__|____|__|_|___|__|__|___|_|____|__|___|__|___| 
|_|___|___|___|___|___|___|____|_|__|___|_____|_|
"""

smarket_kuva = r""" 

                                                     ____________________
   ========================================         / |                 |
                  S-market                         /  |     Pullon      |
   ========================================       /   |    Palautus     |
_________________________________________________/    |    __________   |
|________________________________________________|    |   |__[]___[]_|  |
|   ||             |   ||   |                    |    |                 |
|   ||             |   ||   |  <--  Kauppa       |    |_________________|
|   ||             |   ||   |                    |   /
|   ||             |   ||   |                    |  /
|   ||             |   ||   |                    | /
|   |/             |   |/   |____________________|/      





________________________________________________________________________


"""
metro_kuva = r"""               
_____________________________________________________________________________
_________________________________ |  | |__________________________________
                                /||  | |                               / |
_______________________________/ /|  | |______________________________/  |
______   ______   ______      | | |  | |__   ______   ______   ______ | /|
|    |   |    |   |    |      | | |  | | |   |    |   |    |   |    | |/ |
|____|   |____|   |____|      | | |  | |_|   |    |   |____|   |____| | /
______________________________|/|_|  | |_____|____|___________________|/
__________________________________|  | |_____( )____________________________
                            .     |  | |     /|\             .            /
            .                     |  | |      |    .                     /
.                       .         |__|/      / \                        /
                .                           .               .          /
______________________________________________________________________/
                                                                     |
_____________________________________________________________________|

"""

#Peli alkaa:

lue_tiedosto("intro.txt")
lue_tiedosto("ohjeet.txt")

ika = int(input("Anna ikäsi: "))

if ika < 12:
    print("Olet liian nuori pelaamaan tätä peliä.")


else:

    # Esineet
    ruisku = Esine("Lääkeruisku", 0.1)

    # Huoneet
    piritori = Huone("Piritori", ruisku, piritori_kuva)
    puisto = Huone("Puisto", None, puisto_kuva)
    smarket = Huone("S-Market", None, smarket_kuva)

    # Roskikset
    roskikset = [False, False, False]

    jatka = input("Haluatko jatkaa tallennettua peliä? k/e: ").lower()

    if jatka == "k":
        pelaaja = Pelaaja("", piritori)
        ladattu = lataa_peli(pelaaja, piritori, puisto, smarket, roskikset)

        if ladattu == False:
            nimi = input("Anna nimesi: ")
            pelaaja = Pelaaja(nimi, piritori)
            print(f"Tervetuloa peliin, {pelaaja.nimi}!")
            print(pelaaja.sijainti.kuva)

            aloitus_keskustelu(pelaaja)
    else:
        nimi = input("Anna nimesi: ")
        pelaaja = Pelaaja(nimi, piritori)

        print(f"Tervetuloa peliin, {pelaaja.nimi}!")
        print(pelaaja.sijainti.kuva)

        aloitus_keskustelu(pelaaja)
    komento = ""

    while komento != "lopeta": 
        print("\nPäävalikko")
        print("1. Näytä reppu")
        print("2. Tutki")
        print("3. Liiku")
        print("4. Puhu")
        print("5. Näytä tehtävä")
        print("6. Tallenna peli")
        print("7. Lataa peli")
        print("8. Lopeta")

        komento = input("Anna komento: ").lower()

        if komento == "1":
            nayta_reppu(pelaaja)

        elif komento == "2":
            tutki(pelaaja, roskikset)

        elif komento == "3":
            print("1. Piritori")
            print("2. Puisto")
            print("3. S-Market")

            if pelaaja.tehtava == "Hemmon tehtävät valmis" and pelaaja.sijainti == piritori:
                print("4. Kävele metroasemalle")

            paikka = input("Minne menet? ")

            if paikka == "1":
                pelaaja.liiku(piritori)

            elif paikka == "2":
                pelaaja.liiku(puisto)

            elif paikka == "3":
                pelaaja.liiku(smarket)
                s_market(pelaaja, roskikset, piritori)

            elif paikka == "4" and pelaaja.tehtava == "Hemmon tehtävät valmis" and pelaaja.sijainti == piritori:
                lahde_kamppiin(pelaaja, piritori)

            else:
                print("Tuntematon paikka.")

        elif komento == "4":
            puhu(pelaaja)

        elif komento == "5":

            if pelaaja.tehtava is None:
                print("Sinulla ei ole aktiivista tehtävää.")

            else:
                print(f"Aktiivinen tehtävä: {pelaaja.tehtava}")

        elif komento == "6":
            tallenna_peli(pelaaja, roskikset)

        elif komento == "7":
            lataa_peli(pelaaja, piritori, puisto, smarket, roskikset)

        elif komento == "8":
            print("Peli suljetaan.")
            break

        else:
            print("Tuntematon komento.")

        if pelaaja.ending == "good" or pelaaja.ending == "mid":
            print("Peli päättyi. Kiitos pelaamisesta!")
            break

        elif pelaaja.ending == "bad":
            print("\nAamu koittaa. Kaikki alkaa alusta...")

            nimi = pelaaja.nimi
            pelaaja = Pelaaja(nimi, piritori)
            piritori.esine = Esine("Lääkeruisku", 0.1)
            roskikset = [False, False, False]

            print(pelaaja.sijainti.kuva)
            aloitus_keskustelu(pelaaja)

