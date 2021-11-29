from spillbrett import Spillebrett
from celle import Celle

def testHentCelle():
    testSpillebrett = Spillebrett(3, 5)
    
    testRutenett = [[Celle(), Celle(), Celle(), Celle(), Celle()],
                    [Celle(), Celle(), Celle(), Celle(), Celle()],
                    [Celle(), Celle(), Celle(), Celle(), Celle()]]
    
    testSpillebrett._rutenett = testRutenett
    
    assert hasattr(testSpillebrett, "hentCelle"), f"manglende metode " \
                                        f"for Spillebrett: hentCelle()"
    
    for rad in range(3):
        for kolonne in range(5):
            resultat = testSpillebrett.hentCelle(rad, kolonne)
            assert isinstance(resultat, Celle), f"forvented at " \
                f"hentCelle({rad}, {kolonne}) returnerte et Celle-objekt," \
                f" funnet {type(resultat)}"
                
            assert resultat == testRutenett[rad][kolonne], "feil Celle " \
                f"objekt returnert av hentCelle({rad}, {kolonne}). Er du " \
                f"sikker på at indeksen til den returnerte cellen er riktig?"
    
    for rad in [-1, 4]:
        for kolonne in [-1, 6]:
            resultat = testSpillebrett.hentCelle(rad, kolonne)
            assert resultat is None, f"forventet at " \
                f"hentCelle({rad}, {kolonne}) returnerte None, " \
                f"funnet {type(resultat)}"


def testFinnNabo():
    testSpillebrett = Spillebrett(2, 3)
    
    assert hasattr(testSpillebrett, "finnNabo"), f"manglende metode " \
                                        f"for Spillebrett: finnNabo()"
    
    
    testRutenett = [[Celle(), Celle(), Celle()],
                    [Celle(), Celle(), Celle()]]

    testSpillebrett._rutenett = testRutenett
    
    resultat = testSpillebrett.finnNabo(1, 1)
    
    assert resultat is not None, ".finnNabo(0, 0) returnerte ingenting"
    
    assert type(resultat) == list, f"forventet at .finnNabo(0, 0) returnerte " \
        f"en liste av Celle-objekter, men den returnerte {resultat}"
    
    assert None not in resultat, "listen returnert av finnNabo(0, 0) " \
        "inneholder None-verdier, men den skal bare inneholde Celle-objekter"
    
    assert testRutenett[1][1] not in resultat, "listen returnert av " \
        ".finnNabo(0, 0) inneholder Celle-objekten med index [0][0], " \
        "men den bør bare inneholde naboer av denne Celle."
    
    assert len(resultat) == len(set(resultat)) == 5, "forvented at listen " \
        "returnert av .finnNabo(0, 0) inneholder 3 unike nabo Celle-objekter," \
        f" funnet {len(set(resultat))}"

    naboer = [testRutenett[0][1], testRutenett[1][0], testRutenett[1][1]]
    
    """assert set(resultat) == set(naboer), "listen returnert av .finnNabo(0, 0)" \
        " inneholder feil Celle-objekter. Er du sikker på at indeksen til " \
        "den returnerte cellen er riktig?" """

def testOppdatering():
    testSpillebrett = Spillebrett(4, 5)
    
    assert hasattr(testSpillebrett, "oppdatering"), f"manglende metode " \
                                        f"for Spillebrett: oppdatering()"
    
    testRutenett = [[Celle(), Celle(), Celle(), Celle(), Celle()],
                    [Celle(), Celle(), Celle(), Celle(), Celle()],
                    [Celle(), Celle(), Celle(), Celle(), Celle()],
                    [Celle(), Celle(), Celle(), Celle(), Celle()]]
    
    testRutenett[2][1].settLevende()
    testRutenett[2][2].settLevende()
    testRutenett[1][3].settLevende()
    
    testSpillebrett._rutenett = testRutenett
    
    testSpillebrett.oppdatering()
    
    levendeKoordinater = [(1,2), (2,2)]
    
    testSpillebrett.tegnBrett()
    
    for rad_idx in range(testSpillebrett._rader):
        for kol_idx in range(testSpillebrett._kolonner):
            
            skalVaereLevende = (rad_idx, kol_idx) in levendeKoordinater
            forvented, funnet = ("levende", "død") if skalVaereLevende \
                                else ("død", "levende")
            celle = testSpillebrett._rutenett[rad_idx][kol_idx]
            
            assert celle.erLevende() == skalVaereLevende, "Celle på rad " \
                f"{rad_idx} og kolonne {kol_idx} er {funnet}, men den " \
                f"skal vaere {forvented}"

def testAntallLevende():
    testSpillebrett = Spillebrett(3, 5)
    
    assert hasattr(testSpillebrett, "antallLevende"), f"manglende metode " \
                                        f"for Spillebrett: antallLevende()"
    
    
    testRutenett = [[Celle(), Celle(), Celle(), Celle(), Celle()],
                    [Celle(), Celle(), Celle(), Celle(), Celle()],
                    [Celle(), Celle(), Celle(), Celle(), Celle()]]
                    
    testRutenett[0][0].settLevende()
    testRutenett[1][1].settLevende()
    testRutenett[1][0].settLevende()
    testRutenett[1][2].settLevende()
    
    testSpillebrett._rutenett = testRutenett
    
    resultat = testSpillebrett.antallLevende()
    assert resultat is not None, ".antallLevende() returnerte ingenting"
    assert resultat == 4, "forventet antall levende " \
                f"celler i det oppgitte rutenettet til å være 4, " \
                f"men _antallLevende() returnerte {resultat}"
        
testHentCelle()
testFinnNabo()
testOppdatering()
testAntallLevende()