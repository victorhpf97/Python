lista=['22','15','12']
#converter lista de string para lista de inteiro
res = list(map(int, lista))

#saber a quantidade de numeros que há na lista
valor=len(res)

#função 'sum' soma os itens da lista
soma=sum(res)

final=soma/valor
print(final)