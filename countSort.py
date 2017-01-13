# -*- utf-8 -*-
def coutingSort(lista) :
	ordenado = []
	c = []
	for i in range(231):
		c.append(0)
	for d in lista:
		c[d]+=1
	for indice in range(1,230):
		c[indice]+=c[indice-1]
	for indice in range(len(lista)-1,0):
		c[lista[indice]]-=1
		ordenado.insert(c[lista[indice]],lista[indice])
	return ordenado

lista = [7,1,5,3,1,2,2]
print(coutingSort(lista))
