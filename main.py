from spillbrett import Spillebrett
from celle import Celle
oppgi_rader = int(input("Oppgi antall rader: "))
oppgi_kolonner = int(input("Oppgi antall kolonner: "))
spillbrett = Spillebrett(oppgi_rader, oppgi_kolonner)
fortsette = ""
spillbrett._lagTomtRutenett()
spillbrett._leggCellerIRutenett()
spillbrett._generer()
spillbrett.tegnBrett()
while fortsette == "" "" "and fortsette != "q" """:
    spillbrett.oppdatering()
    spillbrett.tegnBrett()
    print("Generasjon: ", spillbrett._generasjonsnummer)
    print("Antall levende celler: ", spillbrett.antallLevende())
    fortsette = input("Press enter for aa fortsette. Skriv inn q og trykk enter for å avslutte: ")
