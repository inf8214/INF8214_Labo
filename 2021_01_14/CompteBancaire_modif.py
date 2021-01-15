#-*- coding: utf-8 -*-
'''
Classe CompteBancaire
'''
__auteur__ = "Alix Boc"
__date__   = "Hiver 2020"
__cours__  = "Inf8214"



class CompteBancaire:

    def __init__(self,noCompte,solde=0, marge=500):  # <-- 500$ de marge de crédit par défaut
        ''' Constructeur '''
        self.__noCompte = noCompte
        self.__solde = solde
        self.__marge = marge                         # <-- Ajout d'une propriété pour la marge de crédit

    ''' SERVICES '''
    def depot(self, montant):
        ''' Service de dépot'''
        self.__solde += montant

    def retrait(self, montant):
        ''' Le montant du retrait doit être inférieur au solde '''
        if ((self.solde + self.marge - montant) > 0) and (montant > 0):  # <-- On tient compte de la marge de crédit dans le calcul
            self.__solde -= montant
            return True
        return False

    ''' Mutateurs et accesseurs '''
    @property
    def noCompte(self):
        return self.__noCompte

    @property
    def solde(self):
        return self.__solde

    @property                        # <-- Accesseur pour la marge de crédit
    def marge(self):
        return self.__marge

    @marge.setter                    # <-- Mutateur pour la marge de crédit
    def marge(self, montant):
        self.__marge = montant

    def __str__(self):
        ''' Version chaine de caratères de l'objet '''
        return "[CB," + self.noCompte + "," + str(self.solde) + "," + str(self.marge) + "]"  # <-- On tient compte de la marge de crédit


class CompteCheque(CompteBancaire):
     def __str__(self):
        ''' Version chaine de caratères de l'objet '''
        return "[CC," + self.noCompte + "," + str(self.solde) + "," + str(self.marge) + "]"  # <-- On tient compte de la marge de crédit
