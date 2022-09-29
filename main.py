import py
import pytest
print('Configuration de la pompe à essence...')
prix_ordinaire= int(input("Quel est le prix de l'essence ordinaire? "))
prix_diesel = int(input("Quel est le prix du diesel? "))
prix_super = prix_ordinaire * 1.10
code_promotionnel= input("Le code secret du jour est: ")
print("Une autombile arrive...")
Reservoir_Max= float(input("Le nombre de litres total de son réservoir est "))
Reservoir_actuel= float(input("Le nombre de litres actuel du réservoir est "))

def Reservoir(Reservoir_actuel, Reservoir_Max):
    if Reservoir_actuel < Reservoir_Max:
        return True
    elif Reservoir_actuel == Reservoir_Max:
        print("Le réservoir est déjà plein")
    else:
        print("Erreur de saisie. Le réservoir ne peut pas contenir plus de "+str(Reservoir_Max)+" litres")
        Reservoir_Max = float(input("Le nombre de litres total de son réservoir est "))
        Reservoir_actuel = float(input("Le nombre de litres actuel du réservoir est "))
        Reservoir(Reservoir_actuel, Reservoir_Max)

def pompe(prix_ordinaire, prix_diesel, prix_super):
    print ("Veuillez sélectionner le type d'essence parmi:")
    print ("- [O] r d i n a i r e :"+str(prix_ordinaire)+" $ / l i t r e")
    print ("- [D] i e s e l :"+str(prix_diesel)+" $ / l i t r e")
    print ("- [S] u p e r :"+str(prix_super)+" $ / l i t r e")
    choix = input("Votre choix :(O/D/S)")
    if choix == "O" or choix == "o":
        Remplissage_Ordinaire(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)
    elif choix == "D" or choix == "d":
        Remplissage_Diesel(Reservoir_actuel, Reservoir_Max, prix_diesel, code_promotionnel)
    elif choix == "S" or choix == "s":
        Remplissage_Super(Reservoir_actuel, Reservoir_Max, prix_super, code_promotionnel)
    else:
        print("Erreur de saisie")
        pompe(prix_ordinaire, prix_diesel, prix_super)

def Remplissage_Ordinaire(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel):
    choix_remplissage= input("Souhaitez - vous f a i r e l e p l e i n (P) ou c h o i s i r un montant f i x e (M) ?")
    Prix_Total = (Reservoir_Max - Reservoir_actuel) * prix_ordinaire
    if choix_remplissage == "P" or choix_remplissage == "p":
        print("Le prix total est de "+str(Prix_Total)+" $")
        return Prix_Total;
    elif choix_remplissage == "M" or choix_remplissage == "m":
        Montant = float(input("Quel montant voulez - vous mettre dans le réservoir ?"))
        if Montant >0 and Montant <= (Reservoir_Max - Reservoir_actuel) * prix_ordinaire:
                Nb_Litres = Montant / prix_ordinaire
                print("Le réservoir est rempli à "+str(Nb_Litres+Reservoir_actuel)+" litres")
                return Montant;
        elif Montant > (Reservoir_Max - Reservoir_actuel) * prix_ordinaire:
                print("Le réservoir est rempli à "+str(Reservoir_Max)+" litres")
                print("Le montant de "+str(Montant-Prix_Total)+" $ n'a pas été utilisé")
                return Prix_Total;
        else:
            print("Erreur de saisie. Impossible de mettre un montant négatif dans le réservoir")
            Remplissage_Ordinaire(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)
    else:
        print("Erreur de saisie. Veuillez choisir entre P et M")
        Remplissage_Ordinaire(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)

def Remplissage_Diesel(Reservoir_actuel, Reservoir_Max, prix_diesel, code_promotionnel):
    Prix_Total = (Reservoir_Max - Reservoir_actuel) * prix_ordinaire
    choix_remplissage= input("Souhaitez - vous f a i r e l e p l e i n (P) ou c h o i s i r un montant f i x e (M) ?")
    if choix_remplissage == "P" or choix_remplissage == "p":
        print("Le prix total est de "+str(Prix_Total)+" $")
        return Prix_Total;
    elif choix_remplissage == "M" or choix_remplissage == "m":
        Montant = float(input("Quel montant voulez - vous mettre dans le réservoir ?"))
        if Montant >0 and Montant <= (Reservoir_Max - Reservoir_actuel) * prix_diesel:
                Nb_Litres = Montant / prix_diesel
                print("Le réservoir est rempli à "+str(Nb_Litres+Reservoir_actuel)+" litres")
                return Montant;
        elif Montant > (Reservoir_Max - Reservoir_actuel) * prix_diesel:
                print("Le réservoir est rempli à "+str(Reservoir_Max)+" litres")
                print("Le montant de "+str(Montant-Prix_Total)+" $ n'a pas été utilisé")
                return Prix_Total;
        else:
            print("Erreur de saisie. Impossible de mettre un montant négatif dans le réservoir")
            Remplissage_Diesel(Reservoir_actuel, Reservoir_Max, prix_diesel, code_promotionnel)
    else:
        print("Erreur de saisie. Veuillez choisir entre P et M")
        Remplissage_Diesel(Reservoir_actuel, Reservoir_Max, prix_diesel, code_promotionnel)

def Remplissage_Super(Reservoir_actuel, Reservoir_Max, prix_super, code_promotionnel):
    choix_remplissage= input("Souhaitez - vous f a i r e l e p l e i n (P) ou c h o i s i r un montant f i x e (M) ?")
    Prix_Total = (Reservoir_Max - Reservoir_actuel) * prix_ordinaire
    if choix_remplissage == "P" or choix_remplissage == "p":
        print("Le prix total est de "+str(Prix_Total)+" $")
        return Prix_Total;
    elif choix_remplissage == "M" or choix_remplissage == "m":
        Montant = float(input("Quel montant voulez - vous mettre dans le réservoir ?"))
        if Montant >0 and Montant <= (Reservoir_Max - Reservoir_actuel) * prix_super:
                Nb_Litres = Montant / prix_super
                print("Le réservoir est rempli à "+str(Nb_Litres+Reservoir_actuel)+" litres")
                Prix_Total = Montant
                return Montant;
        elif Montant > (Reservoir_Max - Reservoir_actuel) * prix_super:
                print("Le réservoir est rempli à "+str(Reservoir_Max)+" litres")
                print("Le montant de "+str(Montant-Prix_Total)+" $ n'a pas été utilisé")
                return Prix_Total;
        else:
            print("Erreur de saisie. Impossible de mettre un montant négatif dans le réservoir")
            Remplissage_Super(Reservoir_actuel, Reservoir_Max, prix_super, code_promotionnel)
    else:
        print("Erreur de saisie. Veuillez choisir entre P et M")
        Remplissage_Super(Reservoir_actuel, Reservoir_Max, prix_super, code_promotionnel)

def validation_code_promo(code_promotionnel):
    validation = input("Voulez - vous utiliser un code promotionnel (O/N)?")
    if validation == "O" or validation == "o":
        validation_code = input("Entrez le code promotionnel")
        if validation_code == code_promotionnel:
            print("Code promotionnel valide")
            return True;
        else:
            print("Code promotionnel invalide")
            code_promo(code_promotionnel)
    elif validation == "N" or validation == "n":
        print("Aucun code promotionnel n'a été utilisé")
        return False;
    else:
        print("Erreur de saisie. Veuillez choisir entre O et N")
        code_promo(code_promotionnel)



if __name__ == '__main__':
    Reservoir(Reservoir_actuel, Reservoir_Max)
    Prix_Total=pompe(prix_ordinaire, prix_diesel, prix_super)
    print("Le prix total est de "+str(Prix_Total)+" $")
    if validation_code_promo(code_promotionnel) == True:
        rabais_en_pourcentage = 0.1
        Prix_Total = Prix_Total - Prix_Total * rabais_en_pourcentage
        print("Le prix total est de "+str(Prix_Total)+" $")
    else:
        print("Le prix total est de "+str(Prix_Total)+" $")
        print("Merci d'avoir utilisé notre pompe à essence!")


