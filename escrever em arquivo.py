arquivo=open("C:/Users/Aluno/exercio.txt",'w')
pessoas=int(input("Digite o numero de pessoas : "))

for x in range (pessoas):
    nome=str(input("Digite o nome "));
    idade=int(input("Digite a idade : "));
    telefone=int(input("Digite o telefone:"))
arquivo.write(nome+'\n'+str(idade)+'\n'+str (telefone))


arquivo.close()

