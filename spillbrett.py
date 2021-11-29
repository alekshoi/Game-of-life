import random
from celle import Celle
from random import randint 
class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjonsnummer = 0
        self._rutenett = []

    def _lagTomRad(self):
        liste = []
        for _ in range(self._kolonner):
            liste.append(None)
        return liste

    def _lagTomtRutenett(self):
        nostet_liste = []
        for _ in range(self._rader):
            nostet_liste.append(self._lagTomRad())
        self._rutenett = nostet_liste
        return nostet_liste
    
    def _leggCellerIRutenett(self):
        self._rutenett = [[Celle(self) for _ in rad] for rad in self._rutenett]
    
    def _generer(self):
        for rad in self._rutenett:
            for celle in rad:
                tall = random.randint(0,2)
                if tall == 2:
                    celle.settLevende()
    
    def tegnBrett(self):
        for rad in self._rutenett:
            print("\n")
            for element in rad:
                print(element, end="")           
    
    def hentCelle(self, rad, kolonne):
        try:
            if (rad > self._rader-1 or rad < 0) or (kolonne > self._kolonner-1 or kolonne < 0):
                return None
            return self._rutenett[rad][kolonne]
        
        except IndexError:
            return None
            

    def finnNabo(self, rad, kolonne):
        naboer = []
        for i in range (-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    nabo = self.hentCelle(rad+i, kolonne+j)
                    if nabo is not None:
                        naboer.append(nabo)
        return naboer

    def oppdatering(self):
        doede_som_skal_bli_levende = []
        levende_som_skal_doe = []
        for i in range (self._rader):
            for j in range (self._kolonner):
                naboer = self.finnNabo(i, j)
                dode_counter = 0
                levende_counter = 0
                for nabo in naboer:
                    if nabo.erLevende():
                        levende_counter += 1
                    else:
                        dode_counter +=1 
                if (levende_counter < 2 or levende_counter > 3) and self._rutenett[i][j].erLevende():
                    levende_som_skal_doe.append(self._rutenett[i][j])

                if levende_counter == 3 and self._rutenett[i][j].erLevende() is False:
                    doede_som_skal_bli_levende.append(self._rutenett[i][j])
        
        for element in doede_som_skal_bli_levende:
            element.settLevende()
        for element in levende_som_skal_doe:
            element.settDoed()
        self._generasjonsnummer += 1
    
    def antallLevende(self):
        levende_counter = 0
        for under_liste in self._rutenett:
            for element in under_liste:
                if element.erLevende():
                    levende_counter += 1
        return levende_counter



            
                

    
    def __str__(self):
        return str(self._rutenett)
    
    



def testKonstruktoer():
    testSpillebrett = Spillebrett(3, 5)
        
    for variabel in ["_rader", "_kolonner", "_generasjonsnummer"]:
        assert hasattr(testSpillebrett, variabel), f"manglende variabel " \
                                                f"for Spillebrett: {variabel}"
    
    assert testSpillebrett._rader == 3, f"_rader var {testSpillebrett._rader} " \
                                        f"men det burde være 3"
                                        
    assert testSpillebrett._kolonner == 5, f"_kolonner var " \
                    f"{testSpillebrett._kolonner}, men det burde være 5"
                                        
    assert testSpillebrett._generasjonsnummer == 0, f"_generasjonsnummer var " \
                    f"{testSpillebrett._generasjonsnummer}, men det burde være 0"


def testLagTomRad(testSpillebrett):
    resultat = testSpillebrett._lagTomRad()
    beskjed = "forventet _lagTomRad() å returnere en rad av lengden 5 " \
            "(liste med 5 None verdier)"
    
    assert resultat is not None, f"{beskjed}, men ingenting ble returnert"
    
    assert type(resultat) == list, f"{beskjed}, men {resultat} ble returnert " \
                                f"(typen er ikke list)"
    
    assert len(resultat) == 5, f"lengden på raden returnert av _lagTomRad()" \
                            f" var {len(resultat)}, men den skal være 5"
    
    assert resultat == [None]*5, f"{beskjed}, men {resultat} ble returnert"

def testLagTomRutenett(testSpillebrett):
    resultat = testSpillebrett._lagTomtRutenett()
    beskjed = "forventet _lagTomtRutenett() å returnere en rutenett " \
            "(nøsted liste med None verdier)"
    
    assert resultat is not None, f"{beskjed}, men ingenting ble returnert"
    
    assert type(resultat) == list, f"{beskjed}, men {resultat} ble returnert " \
                                f"(typen er ikke list)"
                                
    assert len(resultat) == 3, f"rutenettet returnert av _lagTomtRutenett() " \
        f"skal inneholde 3 kolonner, men resultatet har lengde {len(resultat)}"

    for rad in resultat:
        assert type(rad) == list, f"{beskjed}, men typen av den indre " \
                                f"elementer er ikke list"
                                
        assert len(rad) == 5, f"Lengden på raden (indre liste) returnert " \
                            f"av _lagTomtRutenett() var {len(rad)}, men " \
                            f"den skal være 5"
                            
        assert rad == [None]*5, f"{beskjed} med 3 rader og 5 kolonner, men " \
                                "f{resultat} ble returnert"

def testLeggCellerIRutenett(testSpillebrett):
    testSpillebrett._leggCellerIRutenett()
    rutenett = testSpillebrett._rutenett
    
    for rad in rutenett:
        for verdi in rad:
            assert verdi is not None, "forventet at rutenettet ble fylt " \
                                    "med Celle-objekter, men funnet None"



