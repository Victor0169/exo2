def AnneeBisextile(annee):
    return not annee%400 or ( annee%100 and not annee%4)
    


def NombreDeJour(mois):
    if mois >12 :
        NombreDeJour(mois)
    Valren=[1,3,5,7,8,10,12]
    if mois in ValRen:
        print("Le mois à 31 jours")
    elif mois!=2:
        print("Le mois à 30 jours")
    else:
        if AnneeBisextile(annee)==True:
            print("Le mois a 29 jours")
        else :
            print("Le mois a 28 jours")


