from date_de_naissance import DateDeNaissance

class Person:

    def __init__(self, nom : str , prenom : str, date : DateDeNaissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date = date

    
    def __str__(self) -> str:
        return f"Je suis {self.prenom} {self.nom}, je suis né le {self.date}"


date=DateDeNaissance(13,10,2000)
test=Person("Romain","Liu",date)
print(test)