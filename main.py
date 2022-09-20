

print('Configuration de la pompe à essence...')
    prix_ordinaire=input("Quel est le prix de l'essence ordinaire?")
    prix_diesel=input("Quel est le prix du diesel ?")
    prix_super= prix_ordinaire*1.10
    code_promotionnel= input("Le code secret du jour est :")

function automobile()
    print("Une autombile arrive...")
    Reservoir_Max= input("Le nombre de litres total de son réservoir est ")
    Reservoir_actuel= input("Le nombre de litres actuel du réservoir est ")
    return Reservoir_actuel and Reservoir_Max;

function pompe(prix_ordinaire, prix_diesel, prix_super) {
    print ("Veuillez sélectionner le type d'essence parmi:")
    print ("- [O] r d i n a i r e :"+str(prix_ordinaire)+" $ / l i t r e")
    print ("- [D] i e s e l :"+str(prix_diesel)+" $ / l i t r e")
    print ("- [S] u p e r :"+str(prix_super)+" $ / l i t r e")
    choix = input("Votre choix :(O/D/S)")
    if choix == "O":
        Remplissage_Ordinaire(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)
    elif choix == "D":
        Remplissage_Diesel(Reservoir_actuel, Reservoir_Max, prix_diesel, code_promotionnel)
    elif choix == "S":
        Remplissage_Super(Reservoir_actuel, Reservoir_Max, prix_super, code_promotionnel)
    else:
        print("Erreur de saisie")
        pompe(prix_ordinaire, prix_diesel, prix_super)

function Remplissage_Ordinaire(Reservoir_actuel, Reservoir_Max, prix_ordinaire, code_promotionnel)
    choix_remplissage= input("Souhaitez - vous f a i r e l e p l e i n (P) ou c h o i s i r un montant f i x e (M) ?")