from math import *

Liste15Premier=NbePremierInf2(15)
Liste100Premier=NbePremierInf2(100)

def EstPremier(n):
    "Entrée: n(int),Renvoie si n est premier:True ou False"
    assert type(n)==int and n>=0
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
##Crible d'Erastosthène
def NbePremiersInf1(n):
    "Entrée, n(int), renvoie tous les nombres premiers inférieurs à n et le nombre de nombres premiers inférieurs à n"
    NbePn=0
    for i in range(2,n):
        if EstPremier(i):
            print(i,end=" ")
            NbePn+=1
    return ("Il y a ", NbePn," nombres premiers inférieurs à", n)

def NbePremierInf2(n):
    "Entrée, n(int), renvoie tous les nombres premiers inférieurs à n et le nombre de nombres premiers inférieurs à n"
    Lpremier=[False, False] + [True for k in range(n-2)]
    for u in range(1, n):
        if Lpremier[u]==True:
            i=u
            while i*u<n:
                Lpremier[i*u]=False
                i+=1
    return Lpremier







##Raréfaction des nombres entiers
def Pn(n):
    "Entrée: n(int), Renvoie le nombre de nombres premiers inférieurs à n"
    NbePn=0
    for a in NbePremierInf2(n):
        if a:
            NbePn+=1
    return NbePn
