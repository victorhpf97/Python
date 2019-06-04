lista=input("Digite palavra para codificar: ")

alfabeto=["abcdefghijklmnopqrstuvwxyz "]

#              0    1     2     3      4     5     6     7     8     9    10   11     12   13     14    15    16    17     18    19   20    21    22    23    24    25    26
#              A    B     C     D      E     F     G     H     I     J    K     L     M     N     O     P      Q     R     S     T     U     V     W     X    Y     Z     ESPAÇO
codificação=["@##","&68","uoi","$#%","*jk","kkk","!@m","´pç","!(@","(i)","zxc","9pl","132","78v","vvv","23@","çpo","&¨g","...","<.,","_+3","plk","$%#","po:","fd!","_@#","___"]
### espaço na lista alfabeto[0][25]

valor=0
listaM=lista
letras=len(listaM)
num=30
for x in range(0, 30):
        for y in range(0, num):
            print("lista m:",lista)
            if (alfabeto[0][y] in listaM):
                lista= lista.replace(alfabeto[0][y],codificação[y])
                valor+=1
                print("Codificação:",codificação[y])
                print("alfabeto[0][y]:",alfabeto[0][y])
                print("lista:",lista)
                print("listam",listaM)
            if (valor == letras):
                    break;

        print("len da lista:",len(listaM))
print(lista)
