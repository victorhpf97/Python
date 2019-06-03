#METODO BOLHA PARA ORDENACAO DE LISTA
lista = [5,6,8,3,2,7,9,1,4];
print('METODO BOLHA - BUBBLE SORT');
print('LISTA NO COMECO: ',lista);

x = 0;
tam = len(lista); #9
for i in range(0,tam): #9 #8
    print(lista);

    for w in range(0,tam-1):
        print("w tem o valor de ",w)
        if(lista[w] > lista[w+1]):
            aux = lista[w];
            lista[w] = lista[w+1];
            lista[w+1] = aux;

print(lista);