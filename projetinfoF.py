from tkinter import *
from math import log

### Projet FAURAX

def NP(n=7):
    "Fonction base pour ce projet. Entrée : n entier naturelle plus grand que 0"
    assert n>0,'n superieur a 0'
    if n==1:
        return False                            # Si n=1 , je renvoie directement False
    if n==2:
        return True                             # Si n=2 , je renvoie directement Vrai
    if n%2==0:
        return False                            # cela me premet de reduire la complexité du programme car dans mon range je ne prend que les nombres impairs
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True                                # renvoie les nombres premiers

## 1 Decomposition facteurs premiers
    
    """Tout nombre se décompose en produit de facteur premiers, et on pourrait montrer que tout nombre se décompose aussi en somme de 2 nombre premier"""

def DCNP(n):
    "je décompose un nombre en la suite de ces nombres prems, Entrée un entier naturelle plus grand que 1"
    assert n>1,"n doit être plus grand que 1 , le nombre 1 n'est pas premier"
    Lvaleurs=[]                               # Ceci est ma liste de decomposition en nombres premiers , Ex Lvaleurs=[2,2,5,5] pour n=100
    Ltuples=[]                                # Ceci est ma liste de tuples , Ex Ltuples=[(2,2),(5,2)] pour n=100 avec la second membre qui est l'exposant
    diviseur=2
    while NP(n)==False:                       # Je m'arrête que la nombre est premier
        if n%diviseur==0:                     # Si il est divisible , je remplace ma valeur et je garde le même diviseur, sinon j'augmente le diviseur de 1
            n=n//diviseur
            if diviseur not in Lvaleurs:             
                Lvaleurs.append(diviseur)                                    # Si je ne l'ai pas encore rencontrer , j'ajoute le diviseur a mes listes
                Ltuples.append((diviseur,1))
            else:
                Ltuples[-1]=(diviseur,Ltuples[-1][1]+1)                   # Sinon j'augmente l'exposant dans mon tuple
            
        else:
            diviseur+=1
    if n not in Lvaleurs:             
        Lvaleurs.append(n)           # Si je ne l'ai pas encore rencontrer , j'ajoute le dernier terme a mes listes
        Ltuples.append((n,1))
    else:
        Ltuples[-1]=(n,Ltuples[-1][1]+1)
    return Ltuples                                 # Renvoie la Liste de tuples


## 2 Crible Eratosthene

"""On réalise le crible d'Eratosthene"""
    
def Erh(n=100):
    "On faite le crible , Entrée: n entier naturelle plus grand ou égale à 1, Sortie : liste des nombres premiers"
    assert n>=1,'pour éviter les mauvais calculs , on prendra un n>=1'
    
    L=[]                                               #C'est ma liste de nombres premiers
    LB=[True for k in range(n)]                        #C'est la liste de True/False
    LB[0]=False
    
    passeur=2
    
    
    while True:                                       # Le principe est de cocher les cases multiples des nombres premiers, puis de faire de même avec le suivant en
        for i in range(passeur-1,len(LB),passeur):    # utilisant index pour aller chercher la case la plus proche non coché
           LB[i]=False
        L.append(passeur)
        if True in LB:
            passeur= LB.index(True)+1
        else:
            return L                              
            

""" Ce crible est pratique pour faire une liste des nombres premiers, On va beaucoup l'utiliser dans les programmes suivants"""

## 4 Les Jumeaux         ( By Colin Perret )

def NombresPremiersJumeauxBool(n):
    "sous fonction, je veux un n plus grand ou égale a 2, entier et naturelle"
    assert n>1,'n>=2'
    if NP(n)==True and NP(n+2)==True:
        return True
    else:
        return False                                        # Ceci est le programme booléen qui me servira dans la suite


def NombresPremiersJumeaux(n):
    "Entrée : n entier et renvoie le couple (n,n+2) si ils sont tous les deux premiers"
    assert n>1,'n>=2 please'
    if NombresPremiersJumeauxBool(n):
        return (n,n+2)
    else:
        return "Ce n'est pas un nombre premier jumeaux"     # On modifie le programme pour que ce soit un peu plus poussé

        

def NbrsJumeaux(n):
    "Entrée : n entier et renvoie le nombre de nombres premiers jusqu'à n et la liste de ces nombres"
    assert n>1,'please n>=2'
    compteur=0          
    L=[]
    for i in range (3,n+1,2):                              # Afin de réduire la complexité , je ne prend que les entier impair a partir du rang 3
        if NombresPremiersJumeauxBool(i):
            compteur+=1
            L.append(NombresPremiersJumeaux(i))
    return compteur and L

    
def NiemeJumeaux(n):
    "Entrée : n entier et renvoie "
    i=3                                                   # i est ma variable, qui va passer tout les nombres impaires jusqu'a qu'il est trouver n jumeaux
    compteur=0
    while compteur!=n:
        if NombresPremiersJumeauxBool(i)==True:
            compteur+=1
        i+=2
    return (NombresPremiersJumeaux(i-2))                  # Je retranche -2 car j'ai ajouter +2 en trop a la fin de mon while
