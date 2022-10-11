import py
import pytest
def Reservoir_status(): # Affichage du réservoir
    Reservoir_Max = float(input("Le nombre de litres total de son réservoir est "))
    Reservoir_actuel = float(input("et il en contient actuellement "))
    Reservoir_vérification(Reservoir_actuel, Reservoir_Max)
    while Reservoir_vérification(Reservoir_actuel, Reservoir_Max) == False:
        print("Erreur de saisie. Le réservoir ne peut pas contenir plus de "+str(Reservoir_Max)+" litres")
        Reservoir_status()
    return Reservoir_actuel, Reservoir_Max

def Reservoir_vérification(Reservoir_actuel, Reservoir_Max): # Vérification du réservoir (ne peut pas contenir plus que le maximum de litres)
    if Reservoir_actuel < Reservoir_Max:
        return True
    elif Reservoir_actuel == Reservoir_Max:
        print("Le réservoir est déjà plein. Bonne journée!")
        exit()
    else:
        return False

def pompe(prix_ordinaire, prix_diesel, prix_super): # Choix du type de carburant
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

def Remplissage(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel): # Remplissage du réservoir et calcul du prix total à payer
    choix_remplissage= input("Souhaitez - vous faire le plein (P) ou choisir un montant fixe (M) ? ")
    Prix_Total = 0
    if choix_remplissage == "P" or choix_remplissage == "p": # Remplissage du réservoir jusqu'à la capacité maximale ou jusqu'à ce que le client arrête
        print("Remplissage !")
        Choix_arret_modif = 1
        while (Reservoir_actuel < Reservoir_Max) and Choix_arret_modif == 1:
            Choix_arret = input("Appuyez sur Entrée pour ajouter un litre ou sur A pour arrêter le remplissage.")
            if Reservoir_Max - Reservoir_actuel > 1 and Choix_arret != "A" or Choix_arret != "a":
                Prix_Total += prix_ordinaire
                Reservoir_actuel += 1
                print("État du réservoir d'essence : " + str(Reservoir_actuel) + " litres sur "+ str(Reservoir_Max))
                print("Coût (jusqu'à maintenant) : " + str(Prix_Total) + "$")
            elif Choix_arret == "A" or Choix_arret == "a":
                    Choix_arret_modif = 0
            else:
                Prix_Total += prix_ordinaire * (Reservoir_Max - Reservoir_actuel)
                Reservoir_actuel = Reservoir_Max
                print("État du réservoir d'essence : " + str(Reservoir_actuel) + " litres sur " + str(Reservoir_Max))
                print("Coût (jusqu'à maintenant) : " + str(Prix_Total) + "$")

    elif choix_remplissage == "M" or choix_remplissage == "m": # Remplissage du réservoir jusqu'à ce que le montant choisi du client soit atteint ou jusqu'à ce que le réservoir soit plein
        Montant = float(input("Quel montant voulez - vous mettre dans le réservoir ? "))
        print("Remplissage !")
        Reservoir_final= float(Montant/ prix_ordinaire+ Reservoir_actuel)
        if Reservoir_final > Reservoir_Max:
            Reservoir_final = Reservoir_Max
        Choix_arret_modif = 1
        while Reservoir_actuel < Reservoir_final and Choix_arret_modif == 1:
            Choix_arret = input("Appuyez sur Entrée pour ajouter un litre ou sur A pour arrêter le remplissage.")
            if Reservoir_final - Reservoir_actuel > 1 and Choix_arret != "A" or Choix_arret != "a":
                Prix_Total += prix_ordinaire
                Reservoir_actuel += 1
                print("État du réservoir d'essence : " + str(Reservoir_actuel) + " litres sur " + str(Reservoir_Max))
                print("Coût (jusqu'à maintenant) : " + str(Prix_Total) + "$")
            elif Choix_arret == "A" or Choix_arret == "a":
                Choix_arret_modif = 0
            else:
                if  (Reservoir_Max-Reservoir_actuel)*prix_ordinaire <= Montant:
                    Prix_Total = (Reservoir_Max-Reservoir_actuel)*prix_ordinaire +Prix_Total
                else:
                    Prix_Total = Montant
                    print("État du réservoir d'essence : " + str(Reservoir_final) + " litres sur " + str(Reservoir_Max))
                    print("Coût (jusqu'à maintenant) : " + str(Prix_Total) + "$")
    else:
        print("Erreur de saisie. Veuillez choisir entre P et M")
        Remplissage(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)
    print("Terminé!")
    if validation_code_promo(code_promotionnel) == True : # Vérification du code promotionnel et calcul du prix final
        print("---------------------------------------------------------")
        print("Le montant final est : "+str(Prix_Total*0.7)+"$")
        print("Faites bonne route !")
    else:
        print("---------------------------------------------------------")
        print("Le prix montant final est :  "+str(Prix_Total)+"$")
        print("Faites bonne route !")
        exit()

def validation_code_promo(code_promotionnel): # Vérification du code promotionnel
    print("---------------------------------------------------------")
    validation = input("Si vous connaissez le code promotionnel RABAIS+, entrez - le maintenant pour obtenir 30% de rabais : ")
    if validation == code_promotionnel:
        print("Code valide.")
        return True;
    else:
        print("Code non valide.")
        return False;

def config_pompe():
    print("Configuration de la pompe à essence ...")
    prix_ordinaire = float(input("Prix de l ' essence ordinaire ($/L) : "))
    prix_diesel = float(input("Prix de l ' essence diesel ($/L) : "))
    prix_super = prix_ordinaire * 1.10
    code_promotionnel = input("Le code secret du jour est: ")
    print("∗∗∗∗∗∗∗∗∗∗")
    return prix_ordinaire, prix_diesel, prix_super, code_promotionnel

prix_ordinaire, prix_diesel, prix_super, code_promotionnel = config_pompe() # On appelle la fonction config_pompe() et on récupère les valeurs de retour
print("Une autombile arrive.")
Reservoir_actuel, Reservoir_Max= Reservoir_status() # On appelle la fonction Reservoir_status() et on récupère les valeurs de retour
pompe(prix_ordinaire, prix_diesel, prix_super) # On appelle la fonction pompe() et on lui passe les valeurs de retour de config_pompe()




