def Reservoir_status():
    Reservoir_Max = float(input("Le nombre de litres total de son réservoir est "))
    Reservoir_actuel = float(input("et il en contient actuellement "))
    if Reservoir_vérification(Reservoir_actuel, Reservoir_Max) == True:
	    return Reservoir_actuel, Reservoir_Max
	else Reservoir_vérification(Reservoir_actuel, Reservoir_Max) == False:
		print("Erreur de saisie. Le réservoir ne peut pas contenir plus de "+str(Reservoir_Max)+" litres")
		Reservoir_status()

def Reservoir_vérification(Reservoir_actuel, Reservoir_Max):
    if Reservoir_actuel < Reservoir_Max:
        return True
    elif Reservoir_actuel == Reservoir_Max:
        print("Le réservoir est déjà plein. Bonne journée!")
        exit()
    else:
        return False

Reservoir_status()

|when you enter A, it stops the while loop, but if you press enter, it continues