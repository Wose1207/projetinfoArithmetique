###Crible


def Erh(n=100):
    "On faite le crible"
    assert n!=0
    
    L=[]
    LB=[True for k in range(n)]
    LB[0]=False
    
    passeur=2
    
    
    while True:
        for i in range(passeur-1,len(LB),passeur):
           LB[i]=False
        L.append(passeur)
        if True in LB:
            passeur= LB.index(True)+1
        else:
            return L


###Nombres premiers jumeaux



def NombresPremiersJumeauxBool (n):
    """sous fonction"""
    Erh(n+2)
    if (n in L)==True and (n+2 in L)==True:
        return True
    else:
        return False


def NombresPremiersJumeaux (n):
    "Entrée : n entier et renvoie le couple (n,n+2) si ils sont tous les deux premiers"
    L = Erh(n+2)
    if (n in L)==True and (n+2 in L)==True:
        return (n,n+2)
    else:
        return "Ce n'est pas un nombre premier jumeaux"
        
        
def NbrsJumeaux(n):
    "Entrée : n entier et renvoie le nombre de nombres premiers jusqu'à n et la liste de ces nombres"
    compteur=0
    Ln=[]
    for i in range (1,n):
        if NombresPremiersJumeauxBool(i)==True:
            compteur+=1
            Ln.append(NombresPremiersJumeaux(i))
    return compteur and Ln
    
    
def NiemeJumeaux(n):
    "Entrée : n entier et renvoie "
    i=0
    compteur=0
    while compteur != n:
        if NombresPremiersJumeauxBool(i)==True:
            compteur+=1
        i+=1
    return (NombresPremiersJumeaux(i))

    
    
###Spirale et nombres premiers







