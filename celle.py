class Celle:
    def __init__(self, doed = True ):
        self._doed = doed
    
    def settDoed(self):
        self._doed = True

    def settLevende(self): 
        self._doed = False

    def erLevende(self):
        if not self._doed:
            return True
        elif self._doed:
            return False
    
    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        else: 
            return "."
    
    def __repr__(self):
        return self.hentStatusTegn()       
    
    
    
def testCelle():
    dodCelle = Celle()
    assert dodCelle.erLevende() == False
    dodCelle.settLevende()
    assert dodCelle.erLevende() == True
    dodCelle.settDoed()
    assert dodCelle.erLevende() == False

testCelle()






