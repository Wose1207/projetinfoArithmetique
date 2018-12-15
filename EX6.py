##6 Nombre de mercenne


""" On utilise le test de Lucas-Lehmer pour verifié la liste de Marin Marcenne , En testant la primalité de chaque de nombre de mercenne des rang p , nombre premiers de 3 a 257"""

def Sn(n):
    "Suite de Lucas-Lehmer"
    S=4
    for i in range(n):
        S=((S%Mn(n+2))**2)-2
    
    return S
    
        
def Mn(n):
    "Nombres de Mercenne"
    return (2**n)-1
    


def TestLucas(n):
    "Lucas-Lehmer le sang, n different de 2 superieur a 2"
    
    assert n>=3
    if Sn(n-2)%Mn(n)==0:
        
        return True
    return False
        
        
def LOOKAT():
    L=[2]
    for i in Erh(257+1)[1:]:
        if TestLucas(i):
            L.append(i)
    return L
    
    
    
##
            