from menu import rodarMenu;

def contadorFuncionarios(lista_dicionarios): # Conta quantos funcionários existem
    count = 0;

    for nome in lista_dicionarios:
        count += 1;
    return count;

def criarDicionario():
    arquivo = open('remuneracao.txt', 'r');
    lista_dic_funcionarios = [];

    for linha in arquivo:
        linha = linha.replace('\n', '');
        lista_linha = linha.split(';');
        lista_dic_funcionarios.append({
            'nome': lista_linha[0],
            'cargo': lista_linha[1],
            'órgão': lista_linha[2],
            'remuneracao_do_mês': lista_linha[3],
            'ferias_e_13_salário': lista_linha[4],
            'pagamentos_eventuais': lista_linha[5],
            'licença_prêmio_indenizada': lista_linha[6],
            'abono_permanêncica_e_outras_indenizações': lista_linha[7],
            'redutor_salarial': lista_linha[8],
            'total_líquido': lista_linha[9]
        });
    arquivo.close();
    lista_dic_funcionarios.pop(0);
    return lista_dic_funcionarios;

def pesquisaSalarios(lista_dicionarios, num_funcionarios):
    soma_salarios = 0;
    maior_salario = 0;

    for pessoa in lista_dicionarios:
        # Troca ',' por '.', assim pode ser transformado para float
        salario_atual = float(pessoa['total_líquido'].replace(',', '.'));
        if (salario_atual > maior_salario): # Pega o maior salario
            maior_salario = salario_atual;
        soma_salarios += salario_atual;
    # Media arredondada
    media_salarios = round(soma_salarios / num_funcionarios, 2);
    return media_salarios, maior_salario;

def criarListaDesordenada(dicionarios):
    lista = [];
    for index in range(10000):
        salario_atual = dicionarios[index]['remuneracao_do_mês'].replace(',', '.');
        lista.append(float(salario_atual));
    return lista;
###################################################

dicionarios = criarDicionario();
lista_desordenada = criarListaDesordenada(dicionarios);
contagemFuncionarios = contadorFuncionarios(dicionarios);
mediaSalarios, maiorSalario = pesquisaSalarios(dicionarios, contagemFuncionarios);

informacoes = {
    'num_funcionarios': contagemFuncionarios,
    'media_salarios': mediaSalarios,
    'maior_salario': maiorSalario,
    'dicionarios': dicionarios,
    'lista_desordenada': lista_desordenada
}

rodarMenu(informacoes);