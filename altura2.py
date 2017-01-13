 # -*- utf-8 -*-
def csort(lista):
    ordenado = []
    c = []
    for i in range(231):
        c.append(0)
    for d in lista:
        c[d]+=1
    for indice in range(1,230):
        c[indice]+=c[indice-1]
    for d in lista:
        ordenado.append(0)
    for indice in range(len(lista)):
        c[lista[indice]]-=1
        ordenado[c[lista[indice]]]=lista[indice]
    return ordenado

x = input()
while (x):
    y = input()
    altura = []
    while (y):
        altura.append(input())
        y-=1    
    orden = csort(altura)
    print("%d" % orden[0], end=' ')
    for d in range(1,len(orden)):
        print(" %d" % (orden[d]), end=' ')
    print()
    x-=1
