'''
Distibuteur Automatique de Billets
Illustration de l'utilisation de la classe CompteBancaire
'''
__auteur__ = "Alix Boc"
__date__   = "Hiver 2020"
__cours__  = "Inf8214"

from CompteBancaire_modif import CompteBancaire, CompteCheque


''' VERSION FINALE DE LA CLASSE - MODIFIÉE '''
print ("\nVersion finale - modifiée")
cb = CompteBancaire("1234",1000.0,800)  # <-- On peut ajouter un argument pour la marge (ici 800$)
print( cb )                             # <-- La marge de crédit apparaît dans la représentation en chaîne de caractères de l'objet

cb.retrait(2000)
print( cb )

cb.depot(1000)
print( cb )

cb.retrait(2500)
print( cb )

cb.marge = 1000000                     # <-- On peut modifier la marge
print('Marge de crédit :', cb.marge)   # <-- On peut afficher la marge

cb.retrait(250000)
print( cb )


''' HERITAGE '''
print ("\nExemple héritage")
cc = CompteCheque("99999")
print(cc)                                # <-- La marge de crédit apparaît dans la représentation en chaîne de caractères de l'objet
cc.depot(1000)
print(cc)
print('Marge de crédit :', cc.marge)     # <-- On peut afficher la marge (propriété héritée)