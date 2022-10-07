import py
import pytest
def Reservoir_status():
    Reservoir_Max = float(input("Le nombre de litres total de son réservoir est "))
    Reservoir_actuel = float(input("et il en contient actuellement "))
    return Reservoir_actuel, Reservoir_Max

def Reservoir_vérification(Reservoir_actuel, Reservoir_Max):
    if Reservoir_actuel < Reservoir_Max:
        return True
    elif Reservoir_actuel == Reservoir_Max:
        print("Le réservoir est déjà plein. Bonne journée!")
        exit()
    else:
        print("Erreur de saisie. Le réservoir ne peut pas contenir plus de "+str(Reservoir_Max)+" litres")
        Reservoir_status()
        Reservoir_vérification(Reservoir_actuel, Reservoir_Max)

def pompe(prix_ordinaire, prix_diesel, prix_super):
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - - Affichage sur la pompe                                                                  - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print ("Veuillez sélectionner le type d'essence parmi :")
    print ("- [O]rdinaire :"+str(prix_ordinaire)+" $ / litre")
    print ("- [D]iesel :"+str(prix_diesel)+" $ / litre")
    print ("- [S]uper:"+str(prix_super)+" $ / litre")
    choix = input("Votre choix (O, S ou D) : ")
    if choix == "O" or choix == "o":
        Remplissage(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)
    elif choix == "D" or choix == "d":
        Remplissage(Reservoir_actuel, Reservoir_Max, prix_diesel, code_promotionnel)
    elif choix == "S" or choix == "s":
        Remplissage(Reservoir_actuel, Reservoir_Max, prix_super, code_promotionnel)
    else:
        print("Erreur de saisie")
        pompe(prix_ordinaire, prix_diesel, prix_super)

def Remplissage(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel):
    choix_remplissage= input("Souhaitez - vous faire le plein (P) ou choisir un montant fixe (M) ? ")
    Prix_Total = 0
    if choix_remplissage == "P" or choix_remplissage == "p":
        print("Remplissage !")
        while (Reservoir_actuel < Reservoir_Max) or Enter == "A":
            Reservoir_actuel += 1
            if Reservoir_Max-Reservoir_actuel < 1:
                Prix_Total += prix_ordinaire
            print("Le réservoir contient maintenant "+str(Reservoir_actuel)+" litres")
            Enter= input("Appuyez sur Entrée pour ajouter un litre")
            Prix_Total = (Reservoir_Max - Reservoir_actuel) * prix_ordinaire;
    elif choix_remplissage == "M" or choix_remplissage == "m":
        Montant = float(input("Quel montant voulez - vous mettre dans le réservoir ? "))
        if Montant >0 and Montant <= (Reservoir_Max - Reservoir_actuel) * prix_ordinaire:
                Nb_Litres = Montant / prix_ordinaire
                print("Le réservoir est rempli à "+str(Nb_Litres+Reservoir_actuel)+" litres")
                Prix_Total = Montant
        elif Montant > (Reservoir_Max - Reservoir_actuel) * prix_ordinaire:
                print("Le réservoir est rempli à "+str(Reservoir_Max)+" litres")
                print("Le montant de "+str(Montant-Prix_Total)+" $ n'a pas été utilisé")
                Prix_Total = (Reservoir_Max - Reservoir_actuel) * prix_ordinaire
        else:
            print("Erreur de saisie. Impossible de mettre un montant négatif dans le réservoir")
            Remplissage(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)
    else:
        print("Erreur de saisie. Veuillez choisir entre P et M")
        Remplissage(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)
    print("Le prix total est de "+str(Prix_Total)+" $")
    if validation_code_promo(code_promotionnel)==True:
        print("Le prix total est de "+str(Prix_Total*0.7)+" $")
        print("Merci et à bientôt")
    else:
        print("Le prix total est de "+str(Prix_Total)+" $")
        print("Merci et à bientôt")
        exit()

def validation_code_promo(code_promotionnel):
    validation = input("Si vous connaissez le code promotionnel RABAIS+, entrez - le maintenant pour obtenir 30% de rabais : ")
    if validation_code == code_promotionnel:
        print("Code valide.")
        return True;
    else:
        print("Code non valide.")
        while Essai_2 == "O" or Essai_2 == "o":
            Essai_2 = input("Voulez - vous réessayer avec un autre code ? (O/N) ")
            if Essai_2 == "O" or Essai_2 == "o":
                validation= input("Veuillez entrer le code promotionnel : ")
                if validation_code == code_promotionnel:
                    print("Code valide.")
                    return True;
                    break
                else:
                    print("Code non valide.")
            elif Essai_2 == "N" or Essai_2 == "n":
                return False;
                break
            else:
                print("Erreur de saisie. Veuillez entrer O ou N")

def config_pompe():
    print("Configuration de la pompe à essence ...")
    prix_ordinaire = float(input("Prix de l ' essence ordinaire ($/L) : "))
    prix_diesel = float(input("Prix de l ' essence diesel ($/L) : "))
    prix_super = prix_ordinaire * 1.10
    code_promotionnel = input("Le code secret du jour est: ")
    print("∗∗∗∗∗∗∗∗∗∗")
    return prix_ordinaire, prix_diesel, prix_super, code_promotionnel

prix_ordinaire, prix_diesel, prix_super, code_promotionnel = config_pompe()
print("Une autombile arrive.")
Reservoir_actuel, Reservoir_Max= Reservoir_status()
Reservoir_vérification(Reservoir_actuel, Reservoir_Max)
pompe(prix_ordinaire, prix_diesel, prix_super)




