lista=['11','2','3','4']
nova=[]
total=0

#converte a lista str para int
for x in range(0, len(lista)):
    lista[x]= int (lista[x])
for soma in lista:
    total+=soma
print(total)



