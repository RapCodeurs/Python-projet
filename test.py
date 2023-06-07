def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_de_la_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_de_la_personne + " Quel est ton age ? ")
        try:
            age_int = int(age_str)
        except:
            print("Erreur: Vous devez rentrer un nombre pour l'age")
    return age_int


nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

print("Vous vous appelez " + nom1 + "," + " vous avez " + str(age1) + " ans.")
print("L'an prochain vous aurez " + str(age1 + 1) + " ans.")
print("Vous vous appelez " + nom2 + "," + " vous avez " + str(age2) + " ans.")
print("L'an prochain vous aurez " + str(age2 + 1) + " ans.")
print("Merci passez une bonne journée.")
