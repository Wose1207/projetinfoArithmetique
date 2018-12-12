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
    
    """Tout nombre se décompose en produit de facteur premiers, et on pourrait montrer que tout nombre pair se décompose aussi en somme de 2 nombre premier"""
    
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
    
def DCNPv2(n):
    "je décompose un nombre pair en 2 nombres premiers, Entrée un entier naturelle pair plus grand ou égale à 4 car 2 est le plus petit nombre premier"
    assert n>=4 and n%2==0," J'aimerais un nombre plus grand ou égale a 4  et Impair"
    for i in range(2,n-1):
        if NP(i) and NP(n-i):
            return (i,n-i)
                                 # Programme trivial , ce qui est d'ailleurs étontant c'est que cela semble marcher pour tout nombre plus grand ou égale a 4
            
        
    
    
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

## 3 Deserts de nombres premiers

""" On s'interesse ici a la rarification des nombres premiers , on part de l'idée qu'il existe une infinité de nombre premiers . Commençons par voir la limite et la vitesse de convergence , en utilisant le crible"""

def LimiteNP(n):
    "n est le rang telle que l'on va calculer Pn/n, c'est un entier naturelle plus grand que 1"
    assert n>1,"n>=2"
    return len(Erh(n))/n        # Oui il semble que cela tend vers 0, étudions sa vitesse de convergence
    
def VitesseNP(n):
    return LimiteNP(n)/(1/log(n))  # Sur python il semble que 'log' signifie la fonction logarythme neperien, soit de base normale et non de base 10
                                   # il semble que cela tend vers 1






""" Je vais mintéresser mtn a la croissance des déserts de nombres premiers , c'est a dire l'espace ou il n'y a plus de nombres premiers . L'objectif est dans un premier temps de créer le programme désert, puis dans un second temps d'y reprensenter graphiquement"""

def Desert(n):
    "Je cherche le nombre N telle que entre N et N+n il n'y est pas de nombre premiers : Entrée un nombre naturel entier plus grand que 1"
    assert n>1 and n%2==0,'Cela ne sert a rien de prendre des nombres impaires et n>1'
    passeurVar=n                               
    passeurFixe=n+1                                    # Peut importe de où on part, l'important c'est de ne pas partir en boucle infini donc passeurVar = Passeurfixe-1
    while True:
        if NP(passeurVar)==False:                      # Je modifie mon passeur variable jusqu'à que ce soit un nombre premier
            passeurVar-=1
        else:
            if passeurFixe-passeurVar==n:
                return (passeurVar,"Voici le désert:",[k for k in range(passeurVar+1,passeurVar+n)])
                                      # Si j'ai mon désert, alors je renvoie N=passseurvar
            else:
                passeurFixe=passeurVar+n
                passeurVar=passeurFixe-1
                
def GraphDesert(n):
    "... Building..."
                






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






## 5 Spirale Euler    

"""Dans un premier temps je vais calculer le ratio des nombres premiers presents sur les 4 premiers diagonales partant de 1,2,3 et 4 par rapport au total des nombres premiers ( en fonction d'un nombre de tour), puis nous nous interresseront au problemes d'Euler et de Uliam . Il existe 4 suites pour representer graphiquement la spirale , que je note u v w et z"""

def Spirale(d):
    "d est la diagonale, un tour c'est par rappport a la diagonale 1, soit la suite Un , donc exemple : le premier tour va de uo a u1-1 , ie de 1 a 6 , la deuxieme ect"
    L=[2,3]
    nombre=0
    U=1
    V=2
    W=3
    Z=4
    for i in range(0,d-1):
        U=U+8*i+6
        if NP(U):
            L.append(U)
        V=V+8*i+8
        if NP(V):
            L.append(V)
        W=W+8*i+10
        if NP(W):
            L.append(W)
        Z=Z+8*i+12
        if NP(Z):
            L.append(Z)
    
    ratio=len(L)/len(Erh(Z))
    Ratio=int(ratio*1000)/1000
    return Z,Ratio,"  Voici le ratio des nombres premiers présents sur les diagonales "
    #return L
        
""" cela marche nickel , on initialise en disant que le ratio du premier tour est de 1 , normal . Puis on voit que le ratio tend vite vers 0 .
Maintenant je peux aller chercher le numero de la diagonale telle que le ratio est plus petit que 0.1 par exemple
Je peux aussi créer la spirale graphiquement"""


def GraphSpi(d):
    "d est le nombre de tour"
    main=Tk()
    main.geometry('600x800+200+200')
    main.title("Spirale Euler")
    
    canvas=Canvas(main,height=800,width=600)
    canvas.pack()
    
    canvas.create_text(280,70,text="SPIRALE D'EULER",font="Arial 18 italic")
    canvas.create_text(280,700,text=Spirale(d)[2],font="Arial 9")
    canvas.create_text(280,650,text=Spirale(d)[1],font="Arial 12")
    U,V,W,Z=1,2,3,4
    
    x=300
    y=350
    k=1
    
    
    for i in range(1,Spirale(d)[0]+1):
        
        #U,V,W,Z=U+8*(i-1)+6,V+8*(i-1)+8,W+8*(i-1)+10,Z+8*(i-1)+12
        if NP(i):
            if i==U or i==V or i==W or i==Z:
                canvas.create_text(x,y,text=i,fill='red',font="bold")
            else:
                canvas.create_text(x,y,text=i,fill='blue')
        else:
            canvas.create_text(x,y,text=i,fill='black')
        if i>=U and i<V:
            x-=35
        if i>=V and i<W:
            y+=35
        if i>=W:
            x+=35
        if i<U:
            y-=35
        
        if i==Z:
            U,V,W,Z=U+8*(k-1)+6,V+8*(k-1)+8,W+8*(k-1)+10,Z+8*(k-1)+12
            k+=1
    
    main.mainloop()
        
"""Ici n'est pas l'objectif , je dois percevoir des diagnoales de nombres premiers dans la Spirale. Le problème d'Euler dit que les nombres premiers ont tendance a se concentrer sur des diagonales, je vais donc faire un point a chaque fois que le nombre est premier, en reprenant la structure de mon ancien programme"""
        
def GraphSpi2(d):
    "d est le nombre de tours, lors de l'utilisation du programme , pour percevoir le phenomène de Euler, veuillez mettre un nombre de tours de l'ordre de 150, au delà le programme est très complexe ( pour 200 cela dure 20s) , et en dessous on ne voit pas bien le phenomène, veullez appuyer sur enter(ou return)"""
    main=Tk()
    main.geometry('1000x1000+200+200')
    main.title("Spirale DE TOTO")
    
    def clavier(event):
        touche=event.keysym
        if touche=="Return":
            canvas.create_text(500,30,text='On voit clairement que les nombres premiers en spirales suivent des diagonales précisent')
            canvas.create_line(123,1000,1000,123)
            canvas.create_line(0,883,883,0)
            canvas.create_line(0,643,643,0)
            canvas.create_line(363,1000,1000,363)
        #if touche=="a":
            #canvas.create_line
            
    canvas=Canvas(main,height=1000,width=1000)
    canvas.pack()
    canvas.focus_set()
    canvas.bind("<Key>",clavier)
    
    
    U,V,W,Z=1,2,3,4
    
    x=500
    y=500
    k=1
    
    
    for i in range(1,Spirale(d)[0]+1):
        
        #U,V,W,Z=U+8*(i-1)+6,V+8*(i-1)+8,W+8*(i-1)+10,Z+8*(i-1)+12
        if i==1:
            canvas.create_text(x,y,text=".",fill='red',font="Arial 8 bold")
        if NP(i):
            canvas.create_text(x,y,text=".",fill='black',font="Arial 8 bold")
        if i>=U and i<V:
            x-=3
        if i>=V and i<W:
            y+=3
        if i>=W:
            x+=3
        if i<U:
            y-=3
        
        if i==Z:
            U,V,W,Z=U+8*(k-1)+6,V+8*(k-1)+8,W+8*(k-1)+10,Z+8*(k-1)+12
            k+=1
    
    main.mainloop()
        
"""On peut voir que les nombres premiers suivent des diagonales, précisent , sur la fenetre, veuillez appuyer sur la touche enter pour voir les diagonales"""
        
        
        
        
        
    
        
