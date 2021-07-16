from datetime import date
from abc import abstractclassmethod
import random


class Beast():
    def __init__(self,nom:str,poid:float,taille:float,sexe:str,dateNaiss:date,arrive:date):
        self.Nom=nom
        self.Poid=poid
        self.Taille=taille
        self.Sexe=sexe
        self.DateNaiss=dateNaiss
        self.Arrive=arrive

    def __str__(self):
        return f"""
        Nom:{self.Nom} est un {type(self).__name__} {self.Sexe}
        Agé de {self.Age} ans, soit {self.Age*7} ans en Age humain
        Poid: {self.Poid} Kg
        Taille: {self.Taille} cm
        Date d'arrivé: {self.Arrive}""" 

    def _get_Age(self)->int:
        return int((date.today() - self.DateNaiss).days / 365.2425)
    Age = property(_get_Age)

    def crier(self):
        print(f"{self.Nom} pousse un cri")


    def _get_chanceSurvi(self):
        return random.randint(1,5)
    chanceSurvi=property()
    def Survi(self):
        return self.Survi

    def etat (self):
        if self.chanceSurvi == 5:
            return "Mort"
        else: return "Vivant"