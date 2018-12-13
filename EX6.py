##6 Nombre de mercenne


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
        
        return True, Mn(n)
    return False
        