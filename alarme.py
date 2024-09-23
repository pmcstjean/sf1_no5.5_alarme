####
# Énoncé
####
# Générez 3 booléens aléatoires représentants l'état de trois composantes d'un
# système d'alarme : détecteur-de-mouvement, fenêtre-ouverte et porte-verrouillée.

# Deux autres booléens vont servir pour la configuration du système
# Un booléen viendra dire si le système est armé ou non.
# Un booléen viendra dire si le mode présent est activé.


# Votre programme devrait détecter une intrusion et afficher "ALARME" si le système est armé et que :
# - les portes ne sont pas verrouillées
#    ou si
# - le mode-présent est désactivé et qu'il y a soit du mouvement ou une fenêtre ouverte


import random

ARMÉ = True  # à changer pour tester votre code
MODE_PRÉSENT = True  # à changer aussi

# VARIABLES
choix = [True, False]
portes_verrouillées: bool = random.choice(choix)
fenêtre_ouverte:bool = random.choice(choix)
mouvement: bool = random.choice(choix)



# LOGIQUE
print("\nTest du système en cours....\n"
      f"{ARMÉ=}\n"
      f"{MODE_PRÉSENT=}\n"
      f"{mouvement=}\n"
      f"{fenêtre_ouverte=}\n"
      f"{portes_verrouillées=}")


# TODO afficher le résultat


