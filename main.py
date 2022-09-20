import py

def main():
    config_pompe()
    automobile()
    pompe(prix_ordinaire, prix_diesel, prix_super)
    code_promo(code_promotionnel)

def config_pompe():
    print('Configuration de la pompe à essence...')
    prix_ordinaire: int = input("Quel est le prix de l'essence ordinaire? ")
    prix_diesel = input("Quel est le prix du diesel? ")
    prix_super = prix_ordinaire * 1.10
    code_promotionnel = input("Le code secret du jour est: ")
    return prix_ordinaire, prix_diesel, prix_super, code_promotionnel;

def automobile():
    print("Une autombile arrive...")
    Reservoir_Max= input("Le nombre de litres total de son réservoir est ")
    Reservoir_actuel= input("Le nombre de litres actuel du réservoir est ")
    return Reservoir_actuel and Reservoir_Max;

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
    if choix_remplissage == "P" or choix_remplissage == "p":
        Prix_Total = (Reservoir_Max - Reservoir_actuel) * prix_ordinaire
        print("Le prix total est de "+str(Prix_Total)+" $")
        return Prix_Total;
    elif choix_remplissage == "M" or choix_remplissage == "m":
        Montant = int(input("Quel montant voulez - vous mettre dans le réservoir ?"))
        if Montant >0 and Montant <= (Reservoir_Max - Reservoir_actuel) * prix_ordinaire:
                Nb_Litres = Montant / prix_ordinaire
                print("Le réservoir est rempli à "+str(Nb_Litres+Reservoir_actuel)+" litres")
        elif Montant > (Reservoir_Max - Reservoir_actuel) * prix_ordinaire:
                print("Le réservoir est rempli à "+str(Reservoir_Max)+" litres")
                print("Le montant de "+str(Montant)+" $ n'a pas été utilisé")
        else:
            print("Erreur de saisie. Impossible de mettre un montant négatif dans le réservoir")
            Remplissage_Ordinaire(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)
    else:
        print("Erreur de saisie. Veuillez choisir entre P et M")
        Remplissage_Ordinaire(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)

def Remplissage_Diesel(Reservoir_actuel, Reservoir_Max, prix_diesel, code_promotionnel):
    choix_remplissage= input("Souhaitez - vous f a i r e l e p l e i n (P) ou c h o i s i r un montant f i x e (M) ?")
    if choix_remplissage == "P" or choix_remplissage == "p":
        Prix_Total = (Reservoir_Max - Reservoir_actuel) * prix_diesel
        print("Le prix total est de "+str(Prix_Total)+" $")
        return Prix_Total;
    elif choix_remplissage == "M" or choix_remplissage == "m":
        Montant = int(input("Quel montant voulez - vous mettre dans le réservoir ?"))
        if Montant >0 and Montant <= (Reservoir_Max - Reservoir_actuel) * prix_diesel:
                Nb_Litres = Montant / prix_diesel
                print("Le réservoir est rempli à "+str(Nb_Litres+Reservoir_actuel)+" litres")
        elif Montant > (Reservoir_Max - Reservoir_actuel) * prix_diesel:
                print("Le réservoir est rempli à "+str(Reservoir_Max)+" litres")
                print("Le montant de "+str(Montant)+" $ n'a pas été utilisé")
        else:
            print("Erreur de saisie. Impossible de mettre un montant négatif dans le réservoir")
            Remplissage_Diesel(Reservoir_actuel, Reservoir_Max, prix_diesel, code_promotionnel)
    else:
        print("Erreur de saisie. Veuillez choisir entre P et M")
        Remplissage_Diesel(Reservoir_actuel, Reservoir_Max, prix_diesel, code_promotionnel)

def Remplissage_Super(Reservoir_actuel, Reservoir_Max, prix_super, code_promotionnel):
    choix_remplissage= input("Souhaitez - vous f a i r e l e p l e i n (P) ou c h o i s i r un montant f i x e (M) ?")
    if choix_remplissage == "P" or choix_remplissage == "p":
        Prix_Total = (Reservoir_Max - Reservoir_actuel) * prix_super
        print("Le prix total est de "+str(Prix_Total)+" $")
        return Prix_Total;
    elif choix_remplissage == "M" or choix_remplissage == "m":
        Montant = int(input("Quel montant voulez - vous mettre dans le réservoir ?"))
        if Montant >0 and Montant <= (Reservoir_Max - Reservoir_actuel) * prix_super:
                Nb_Litres = Montant / prix_super
                print("Le réservoir est rempli à "+str(Nb_Litres+Reservoir_actuel)+" litres")
        elif Montant > (Reservoir_Max - Reservoir_actuel) * prix_super:
                print("Le réservoir est rempli à "+str(Reservoir_Max)+" litres")
                print("Le montant de "+str(Montant)+" $ n'a pas été utilisé")
        else:
            print("Erreur de saisie. Impossible de mettre un montant négatif dans le réservoir")
            Remplissage_Super(Reservoir_actuel, Reservoir_Max, prix_super, code_promotionnel)
    else:
        print("Erreur de saisie. Veuillez choisir entre P et M")
        Remplissage_Super(Reservoir_actuel, Reservoir_Max, prix_super, code_promotionnel)

    def code_promo(code_promotionnel):
        validation = input("Voulez - vous utiliser un code promotionnel (O/N)?")
        if validation == "O" or validation == "o":
            validation_code = input("Entrez le code promotionnel")
            if validation_code == code_promotionnel:
                print("Code promotionnel valide")
                return True
            else:
                print("Code promotionnel invalide")
                return False