from Models.Beast import Beast
from datetime import date


class Oiseau(Beast):
    def __init__(self, nom, poid, taille, sexe, dateNaiss, arrive,couleur:str,cage:bool):
        super().__init__(nom, poid, taille, sexe, dateNaiss, arrive)
        self.Couleur=couleur
        self.Cage=cage


    def __str__(self):
        return f"""
        {Beast.__str__()} 
        Couleur: {self.Couleur}
        Captivité: {self.Cage}
        """