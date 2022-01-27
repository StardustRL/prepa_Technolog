class DateDeNaissance:

    #classe qui permet de définir une date de naissance

    def __init__(self, day : int , month : int , year : int) -> None:
        self.jour = day
        self.mois = month
        self.annee = year

    

    def __verifJour(self) -> bool:

        if( self.jour < 1 or self.jour > 31):
            return False
        else:
            return True


    def __verifMois(self) -> bool:
        if ( self.mois < 1 or self.mois > 12):
            return False
        else :
            return True


    def verifDateNaissance(self) -> bool:
        if( self.__verifJour and self.__verifMois):
            return True
        else : 
            return False
        