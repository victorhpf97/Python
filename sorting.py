def bubbleSort(lista):
    lista_ordenada = lista.copy();
    tamanho = len(lista_ordenada)
    ordenado = False;
    while (not ordenado):
        ordenado = True;
        for posicao in range(tamanho - 1):
            if (lista_ordenada[posicao] > lista_ordenada[posicao + 1]):
                temp = lista_ordenada[posicao + 1];
                lista_ordenada[posicao + 1] = lista_ordenada[posicao];
                lista_ordenada[posicao] = temp;
                ordenado = False;
    return lista_ordenada;

def selectionSort(lista):
    lista_ordenada = lista.copy();
    tamanho_array = len(lista_ordenada);
    for index in range(tamanho_array):
        menor = lista_ordenada[index];
        pos_menor = index;
        for posicao in range(index + 1, tamanho_array):
            if (lista_ordenada[posicao] < menor):
                menor = lista_ordenada[posicao];
                pos_menor = posicao;
        if (index != pos_menor):
            temp = lista_ordenada[index];
            lista_ordenada[index] = menor;
            lista_ordenada[pos_menor] = temp;
    return lista_ordenada;

def mergeSort(lista):
    if (len(lista) > 1):
        metade = len(lista) // 2;
        esquerda = lista[:metade];
        direita = lista[metade:];

        esquerda = mergeSort(esquerda);
        direita = mergeSort(direita);
        return merge(esquerda, direita);
    return lista;

def merge(esquerda, direita):
    lista_ordenada = [];

    if (len(esquerda) == 1 and len(direita) == 1):
        if (esquerda[0] < direita[0]):
            lista_ordenada = [esquerda[0], direita[0]];
            return lista_ordenada;
        lista_ordenada = [direita[0], esquerda[0]];
        return lista_ordenada;

    while ((len(esquerda)) and (len(direita))):
        if (esquerda[0] <= direita[0]):
            lista_ordenada.append(esquerda.pop(0));
        else:
            lista_ordenada.append(direita.pop(0));

    if (len(esquerda) > 0):
        lista_ordenada.extend(esquerda);
    if (len(direita) > 0):
        lista_ordenada.extend(direita);
    return lista_ordenada;
