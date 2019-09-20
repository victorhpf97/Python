import os;
import time;
from sorting import bubbleSort, selectionSort, mergeSort;

# cria o menu inicial do programa
menu_inicial = {
    'menu': 'Menu de opções, digite o número da opção desejada.',
    'info': 'Pesquisa de informações:\n',
    '1': '1 - Quantidade de funcionários',
    '2': '2 - Pesquisa de funcionários',
    '3': '3 - Listar média de salários',
    '4': '4 - Listar maior salário',
    '5': '5 - Ordenar lista de salários',
    '6': '6 - Sair do programa'
}

# cria o menu para pesquisa de funcionarios
menu_pesquisa = {
    'menu': 'Menu de opções, digite o número da opção desejada.',
    'info': 'Pesquisar funcionários pelo:\n',
    '1': '1 - Nome',
    '2': '2 - Cargo',
    '3': '3 - Órgão',
    '4': '4 - Voltar'
}

menu_ordenacoes = {
    'menu': 'Menu de opções, digite o número da opção desejada.',
    'info': 'Ordenar lista usando:\n',
    '1': '1 - Bubble sort',
    '2': '2 - Selection sort',
    '3': '3 - Merge sort',
    '4': '4 - Voltar'
}

def limparTela():
    if (os.name == 'nt'):
        os.system('cls');
    else:
        os.system('clear');

def pausar():
    if (os.name == 'nt'):
        os.system('pause');
    else:
        input('Aperte Enter para continuar...');

# printa um menu de opções
def printMenu(menu):
    for opcao in menu.values():
        print(opcao);

# Roda uma acao relacionada a cada opcao do menu
def executarAcao(acao, dados):
    if (acao == 1):
        print('Existem {:,} funcionários.'.format(dados['num_funcionarios']));
        print('');
        pausar();
        limparTela();
    elif (acao == 2):
        var_busca, categoria = prepararPesquisa();
        if (var_busca == 'stop'):
            limparTela();
            return;
        resultado, lista_posicoes = pesquisarLista(dados['dicionarios'], var_busca, categoria);
        limparTela();
        if (resultado):
            printResultadoPesquisa(dados['dicionarios'], var_busca, lista_posicoes, categoria);
        else:
            print('Nenhum nome, cargo ou órgão "{}" foi encontrado'.format(var_busca));
        print('');
        pausar();
        limparTela();
    elif (acao == 3):
        print('A média salarial dos funcionários é de R$ {:,}'.format(dados['media_salarios']));
        print('');
        pausar();
        limparTela();
    elif (acao == 4):
        print('O maior salário encontrado é de R$ {:,}'.format(dados['maior_salario']));
        print('');
        pausar();
        limparTela();
    elif (acao == 5):
        while (True):
            limparTela();
            printMenu(menu_ordenacoes);
            opcao = int(input('\nOpção: '));
            if (opcao >= 1 and opcao <= 3):
                lista_ordenada, tempo_execucao = ordenarUsando(opcao, dados['lista_desordenada']);
                limparTela();
                print('Uma lista com', len(dados['lista_desordenada']), 'salarios\n');
                print('foi ordenada em', tempo_execucao, 'segundos.');
                print('');
                pausar();
                limparTela();
                print(lista_ordenada);
                print('');
                pausar();
                break;
            elif (opcao == 4):
                break;

# roda o menu infinitamente ate o usuario escolher a opcao para sair do programa
def rodarMenu(dados_arquivo):
    while (True):
        limparTela();
        printMenu(menu_inicial);
        opcao = int(input('\nOpção: '));
        if (opcao >= 1 and opcao <= 5):
            limparTela();
            executarAcao(opcao, dados_arquivo);
        elif (opcao == 6):
            limparTela();
            print('Saindo do programa.');
            break;

def prepararPesquisa():
    while (True):
        limparTela();
        printMenu(menu_pesquisa);
        opcao = int(input('\nOpção: '));

        if (opcao >= 1 and opcao <= 4):
            limparTela();
            while (opcao != 4):
                print("\nColocar no mínimo nome e sobrenome!\n");
                if (opcao == 1):
                    var_busca = input('Qual o nome que deseja proucurar:\n').upper();
                    chave_dicionario = 'nome';
                    return var_busca, chave_dicionario;
                elif (opcao == 2):
                    var_busca = input('Qual o cargo que deseja proucurar:\n').upper();
                    chave_dicionario = 'cargo';
                    return var_busca, chave_dicionario;
                elif (opcao == 3):
                    var_busca = input('Qual o órgão que deseja proucurar:\n').upper();
                    chave_dicionario = 'órgão';
                    return var_busca, chave_dicionario;
            limparTela();
            return 'stop', 'stop';

def pesquisarLista(lista_dicionarios, valor_busca, chave):
    index = 0;
    lista_posicoes = [];

    for dicionario in lista_dicionarios:
        if (valor_busca in dicionario[chave]):
            lista_posicoes.append(index);
        index += 1;
    if (len(lista_posicoes) > 0):
        return True, lista_posicoes;
    return False, lista_posicoes;

# Printa o resultado da pesquisa de nome, órgaos ou cargo
def printResultadoPesquisa(lista_funcionarios, valor_proucurado, resultado, categoria):
    num_resultados = len(resultado);
    if (categoria == 'nome'): # Pesquisar por nome e mostrar informações do funcionário
        for index in range(num_resultados):
            for chave, valor in lista_funcionarios[resultado[index]].items():
                chave = chave.replace('_', ' ').title();
                print(chave + ':', valor);
            print('');
        print('{:,} funcionários com o nome "{}":\n'.format(num_resultados, valor_proucurado));
    elif (categoria == 'cargo'): # Pesquisar um cargo e mostrar todos os funcionários dele
        for index in range(num_resultados):
            print(lista_funcionarios[resultado[index]]['nome']);
        print('{:,} funcionários trabalham como "{}":\n'.format(num_resultados, valor_proucurado));
    else: # Pesquisar órgaos
        print('{:,} funcionários trabalham no órgão "{}":\n'.format(num_resultados, valor_proucurado));

def medirTempoOrdenacao(ordenador, lista_desordenada):
    inicio = time.perf_counter();
    resultado = ordenador(lista_desordenada);
    termino = time.perf_counter();
    return resultado, termino - inicio;

def ordenarUsando(sort, lista_desordenada):
    if (sort == 1):
        return medirTempoOrdenacao(bubbleSort, lista_desordenada);
    elif (sort == 2):
        return medirTempoOrdenacao(selectionSort, lista_desordenada);
    else:
        return medirTempoOrdenacao(mergeSort, lista_desordenada);

