#Project Euler #1: Multiples of 3 and 5 
#From hackerrank - Juan Cruz

def sumEuler(n):
    n3=int((n-1)//3)   #Se realizo una suma de infinitos elementos consecutivos
    n5=int((n-1)//5)
    n15=int((n-1)//15)
    m3=3*(n3*(n3+1)//2)
    m5=5*(n5*(n5+1)//2)
    m15=15*(n15*(n15+1)//2)
    Suma=m3+m5-m15
    print(int(Suma))
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumEuler(n)
    
