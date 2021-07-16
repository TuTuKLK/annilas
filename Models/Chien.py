from Models.Beast import Beast
from datetime import date



class Chien(Beast):
    def __init__(self, nom, poid, taille, sexe, dateNaiss, arrive, collier:str,dressage:bool, race:str):
        super().__init__(nom, poid, taille, sexe, dateNaiss, arrive)
        self.Collier=collier
        self.Dressage=dressage
        self.Race=race

    def __str__(self):
        return f"""
        {Beast.__str__()} 
        Couleur du collier: {self.Collier}
        Dressé: {self.Dressage}
        Race: {self.Race}
        """