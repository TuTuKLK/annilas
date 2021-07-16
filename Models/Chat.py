from Models.Beast import Beast
from datetime import date


class Chat(Beast):
    def __init__(self, nom, poid, taille, sexe, dateNaiss, arrive, caractere:str, griffe:bool, poil:str):
        super().__init__(nom, poid, taille, sexe, dateNaiss, arrive)
        self.Caractere=caractere
        self.Griffe=griffe
        self.Poil=poil


    def __str__(self):
        return f"""
        {Beast.__str__(self )}
        Caractère: {self.Caractere}
        Griffe: {self.Griffe}
        Poil: {self.Poil}
        """ 
        # chanceSurvi: {Beast.Survi(self)}
        # Etat: {Beast.etat(self)}
    # def __str__(self):
    #     return f"""
    #     Nom:{self.Nom} est un {type(self).__name__} {self.Sexe}
    #         Agé de {self.Age}, soit {self.Age*7}
    #         Poid: {self.Poid} Kg
    #         Taille: {self.Taille} cm
    #         Date d'arrivé: {self.Arrive}
    #         Caractère: {self.Caractere}
    #         Griffe: {self.Griffe}
    #         Poil: {self.Poil}
    #     """ 
