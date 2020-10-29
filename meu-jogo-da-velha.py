#ALGORITMO CRIADO COM O OBJETIVO DE SIMULAR UM JOGO DA VELHA PARA PRÁTICA DOS CONHECIMENTOS ADQUIRIDOS, O ÚSUARIO PODE
#JOGAR ELE COM UM AMIGO OU CONTRA O COMPUTADOR

from time import sleep
from random import choice


def cria_tabuleiro():
    """Função utilizada para montar a estrutura do tabuleiro

    sem parâmetros

    return: uma lista composta com a estrutura do tabuleiro"""

    estrutura_tab = []
    for linha in range(0, 3):
        estrutura_tab.append(['    -    ', '    -    ', '    -    '])

    return estrutura_tab


def mostra_tabuleiro():
    """Função utilizada para mostrar o tabuleiro do jogo na tela

    param tabuleiro: tabuleiro do jogo da velha

    sem return"""
    print('-' * 31)
    print('TABULEIRO DO JOGO'.center(31))
    print('-' * 31)

    for linha in range(0, 3):
        print('|', end='')
        for coluna in range(0, 3):
            print(tabuleiro[linha][coluna], end='')
            print('|', end='')

        print()

    print('-' * 31)


def verif_posicoes():
    """Função utilizada para verificar as posições disponíves no tabuleiro para o jogador jogar

    sem parâmetros

    sem return"""

    print('POSIÇÕES DISPONÍVEIS PARA JOGAR')
    print('-' * 31)
    for linha in range(0, 3):
        posicoes = []
        print(f'Linha {linha}: ', end='')
        for c in range(0, 3):
            if tabuleiro[linha][c] == '    -    ':
                posicoes.append(c)

        print(str(posicoes)[1:-1])
    print('-' * 31)


def qtde_jogadores():
    """Função recursiva utilizada para definir quantos jogadores irão jogar

    sem parâmetros

    return: quantidade  de jogadores"""

    qtde_jog = int(input('Quantos jogadores irão jogar: '))
    if 1 <= qtde_jog <= 2:
        return qtde_jog
    else:
        print('Erro!! este jogo da velha deve ser jogado por pelo menos um jogador')
        qtde_jogadores()


def criar_jogadores():
    """Função utilizada para a criação dos jogadores que irão jogar, nela o úsuario pode
       definir o nome e a peça  dos jogadores

    sem parâmetros

    return: um dicionário com os dados dos dois jogadores"""

    participantes = {}  # Armazena dados dos jogadores

    for n in range(1, 3):

        jog = {}  # Armazena dados do jogador temporariamente
        if n == 1 or n == 2 and not bot:
            jog['nome'] = input(f'jogador{n} como você se chama: ')
            jog['bot'] = False
        else:
            jog['nome'] = 'computador'
            jog['bot'] = True

        if not (n == 2):

            while True:
                jog["peca"] = str(input('qual será a sua peça no jogo? X/O: '))
                if jog["peca"] == 'X' or jog['peca'] == 'O':
                    break

                print('Erro!! Você escolheu uma peça ínvalida, tente novamente')

        else:

            if participantes['jog1']['peca'] == 'X':
                jog['peca'] = 'O'
            else:
                jog['peca'] = 'X'

        participantes[f"jog{n}"] = jog.copy()

    return participantes


def jogador_jogada():
    """Função utilizada para a definição da linha e da coluna aonde o jogador ira jogar no tabuleiro

    sem parâmetros

    return: um dicionário com o  valor da linha e da coluna definidos pelo úsuario"""
    # Definição da Linha pelo Jogador
    while True:
        linha = int(input('Escolha a linha em que você vai jogar: '))
        if 0 <= linha <= 2:
            break
        print("\033[31mErro!! linha ínvalida, tente novamente\033[m")

    # Definição da Coluna pelo Jogador
    while True:
        coluna = int(input('Agora, escolha a coluna: '))
        if 0 <= coluna <= 2:
            break
        print("\033[31mErro!! coluna ínvalida, tente novamente\033[m")

    return dict(l=linha, c=coluna)


def bot_jogada():
    """Função utilizada pelo computador para fazer uma jogada, onde o computador faz diversas analíses no tabuleiro
        para escolher o melhor local para jogar, a jogada feita pode ser para vencer ou para se defender

        AS MECANICAS DO BOT(COMPUTADOR) FUNCIONAM DA SEGUINTE FORMA:

            1 - é feita uma analíse no tabuleiro de acordo com o local aonde o úsuario jogou ou o próprio computador jogou,
                essa análise pode ser de uma linha, coluna ou diagonal onde o computador procura posições para jogar

            2 - após essa análise, as variáveis utilizadas são zeradas e o conteúdo da lista que armazena as jogadas
                temporariamente é passado para a lista que armazena as jogadas permanentemente, se ela tiver jogadas,
                e a lista temporaria também é zerada """

    # VERIFICAÇÃO DAS POSSÍVEIS JOGADAS PARA IMPEDIR O JOGADOR DE GANHAR

    # nessas verificações, é feita uma analise o tabuleiro a partir do local aonde o úsuario jogou para fazer uma
    # jogada que o impeça de ganhar

    # jogadas que o computador pode fazer para impedir que o úsuario ganhe
    jogadas_in = []
    # variável que contabiliza a quantidade de peças que o úsuario jogou em um determinado local
    contador_in = 0

    # armazena temporariamente as jogadas que o computador pode fazer para impedir que o úsuario ganhe
    posicoes_in = []

    # VERIFICAÇÃO DE POSIÇÕES DISPONIVEÍS NA LINHA EM QUE O ÚSUARIO JOGOU
    for coluna in range(0, 3):
        if tabuleiro[j_jogada['l']][coluna].strip() == '-':
            posicoes_in.append((j_jogada['l'], coluna))
        elif tabuleiro[j_jogada['l']][coluna].strip() in 'XO' and tabuleiro[j_jogada['l']][coluna].strip() != peca:
            contador_in += 1

        if contador_in == 2 and len(posicoes_in) == 1:
            return dict(l=posicoes_in[0][0], c=posicoes_in[0][1])

    contador_in = 0
    for p in posicoes_in:
        jogadas_in.append(p)
    posicoes_in.clear()

    # VERIFICAÇÃO DAS POSIÇÕES DISPONÍVEIS NA COLUNA EM QUE O ÚSUARIO JOGOU

    for linha in range(0, 3):
        if tabuleiro[linha][j_jogada['c']].strip() == '-':
            posicoes_in.append((linha, j_jogada['c']))
        elif tabuleiro[linha][j_jogada['c']].strip() in 'XO' and tabuleiro[linha][j_jogada['c']].strip() != peca:
            contador_in += 1

        if contador_in == 2 and len(posicoes_in) == 1:
            return dict(l=posicoes_in[0][0], c=posicoes_in[0][1])

    contador_in = 0
    for p in posicoes_in:
        jogadas_in.append(p)
    posicoes_in.clear()

    # VERIFICAÇÃO DAS POSIÇÕES DISPONÍVEIS NA DIAGONAL 1 \ SE O ÚSUARIO JOGOU NELA
    if j_jogada['l'] == j_jogada['c'] == 0 or j_jogada['l'] == j_jogada['c'] == 1 or j_jogada['l'] == j_jogada[
        'c'] == 2:

        linha_v = 0
        coluna_v = 0

        while linha_v < 3 and coluna_v < 3:
            if tabuleiro[linha_v][coluna_v].strip() == '-':
                posicoes_in.append((linha_v, coluna_v))
            elif tabuleiro[linha_v][coluna_v].strip() in 'XO' and tabuleiro[linha_v][coluna_v].strip() != peca:
                contador_in += 1
            linha_v += 1
            coluna_v += 1

        if contador_in == 2 and len(posicoes_in) == 1:
            return dict(l=posicoes_in[0][0], c=posicoes_in[0][1])

    contador_in = 0
    for p in posicoes_in:
        jogadas_in.append(p)
    posicoes_in.clear()

    # VERIFICAÇÃO DAS POSIÇÕES DISPONÍVEIS NA DIAGONAL 2 / SE O ÚSUARIO JOGOU NELA
    if 2 == j_jogada['l'] and j_jogada['c'] == 0 or j_jogada['l'] == j_jogada['c'] == 1 or j_jogada[
        'l'] == 0 and j_jogada['c'] == 2:

        linha_v = 2
        coluna_v = 0
        while linha_v >= 0 and coluna_v < 3:
            if tabuleiro[linha_v][coluna_v].strip() == '-':
                posicoes_in.append((linha_v, coluna_v))
            elif tabuleiro[linha_v][coluna_v].strip() in 'XO' and tabuleiro[linha_v][coluna_v].strip() != peca:
                contador_in += 1

            linha_v -= 1
            coluna_v += 1

        if contador_in == 2 and len(posicoes_in) == 1:
            return dict(l=posicoes_in[0][0], c=posicoes_in[0][1])

    for p in posicoes_in:
        jogadas_in.append(p)

    # ================================================================================

    # VERIFICAÇÃO DAS POSSÍVEIS  JOGADAS PARA  O COMPUTADOR GANHAR

    # já nessas verificações, o tabuleiro é analisado a partir da onde o computador jogou para que ele faça uma
    # jogada que o ajude a ganhar

    # jogadas que o computador pode fazer para ganhar
    jogadas_vt = []

    # variável para contabilizar a quantidade de peças que o computador jogou em um determinado local
    contador_p = 0

    # armazena temporariamente as jogadas que o computador  pode fazer para vencer
    posicoes_vt = []

    for linha in range(0, 3):
        for coluna in range(0, 3):

            # as analíses no tabuleiro  começam quando o computador encontrar sua peça em algum local nele
            # e após isso são analisadas as possibilidades de jogada de acordo com o local aonde a peça esta

            if tabuleiro[linha][coluna].strip() in 'XO' and tabuleiro[linha][coluna].strip() == peca:

                # VERIFICAÇÃO POR LINHA
                for coluna_v in range(0, 3):
                    if tabuleiro[linha][coluna_v].strip() in 'XO' and tabuleiro[linha][coluna_v].strip() != peca:
                        posicoes_vt.clear()
                        break

                    elif tabuleiro[linha][coluna_v].strip() == '-':
                        posicoes_vt.append((linha, coluna_v))

                    elif tabuleiro[linha][coluna_v].strip() == peca:
                        contador_p += 1

                    if contador_p == 2 and len(posicoes_vt) == 1:
                        return dict(l=posicoes_vt[0], c=posicoes_vt[1])

                if len(posicoes_vt) > 0:
                    for j in posicoes_vt:
                        jogadas_vt.append(j)
                    posicoes_vt.clear()

                # VERIFICAÇÃO POR COLUNA
                contador_p = 0

                for linha_v in range(0, 3):
                    if tabuleiro[linha_v][coluna].strip() in 'XO' and tabuleiro[linha_v][coluna].strip() != peca:
                        posicoes_vt.clear()
                        break

                    elif tabuleiro[linha_v][coluna].strip() == '-':
                        posicoes_vt.append((linha_v, coluna))

                    elif tabuleiro[linha_v][coluna].strip() == peca:
                        contador_p += 1

                    if contador_p == 2 and len(posicoes_vt) == 1:
                        return dict(l=posicoes_vt[0], c=posicoes_vt[1])

                if len(posicoes_vt) > 0:
                    for j in posicoes_vt:
                        if not j in jogadas_vt:
                            jogadas_vt.append(j)
                    posicoes_vt.clear()

                # VERIFICAÇÃO DIAGONAL 1 \

                if linha == coluna == 0 or linha == coluna == 1 or linha == coluna == 2:
                    contador_p = 0
                    linha_v = 0
                    coluna_v = 0
                    while linha_v < 3 and coluna_v < 3:
                        if tabuleiro[linha_v][coluna_v].strip() in 'XO' and tabuleiro[linha_v][
                            coluna_v].strip() != peca:
                            posicoes_vt.clear()
                            break
                        elif tabuleiro[linha_v][coluna_v].strip() == '-':
                            posicoes_vt.append((linha_v, coluna_v))
                        elif tabuleiro[linha_v][coluna_v].strip() == peca:
                            contador_p += 1

                        if contador_p == 2 and len(posicoes_vt) == 1:
                            return dict(l=posicoes_vt[0][0], c=posicoes_vt[0][1])

                        linha_v += 1
                        coluna_v += 1

                    if len(posicoes_vt) > 0:
                        for j in posicoes_vt:
                            if not j in jogadas_vt:
                                jogadas_vt.append(j)

                # VERIFICAÇÃO DIAGONAL 2 /
                if linha == 2 and coluna == 0 or linha == coluna == 1 or linha == 0 and coluna == 2:

                    contador_p = 0
                    linha_v = 2
                    coluna_v = 0
                    while linha_v >= 0 and coluna_v < 3:
                        if tabuleiro[linha_v][coluna_v].strip() in 'XO' and tabuleiro[linha_v][
                            coluna_v].strip() != peca:
                            posicoes_vt.clear()
                            break
                        elif tabuleiro[linha_v][coluna_v].strip() == '-':
                            posicoes_vt.append((linha_v, coluna_v))
                        elif tabuleiro[linha_v][coluna_v].strip() == peca:
                            contador_p += 1

                        if contador_p == 2 and len(posicoes_vt) == 1:
                            return dict(l=posicoes_vt[0][0], c=posicoes_vt[0][1])

                        linha_v -= 1
                        coluna_v += 1

                    if len(posicoes_vt) > 0:
                        for j in posicoes_vt:
                            if not j in jogadas_vt:
                                jogadas_vt.append(j)


    # Escolha da jogada para o computador ganhar
    if not len(jogadas_vt) == 0:
        jogada_bot = choice(jogadas_vt)
        return dict(l=jogada_bot[0], c=jogada_bot[1])


    # Escolha da jogada para o computador impedir o úsuario de ganhar

    # Isso só será feito se o computador não estiver jogado nenhuma vez no tabuleiro ou não e
    elif cont_bot == 0:
        print('a')
        jogada_bot = choice(jogadas_in)
        return dict(l=jogada_bot[0], c=jogada_bot[1])


def fazer_jogada():
    """Função utilizada para verificar se o local aonde o jogador quer jogar esta disponível, ou seja esta vazio

    sem parâmetros

    return: um valor lógico verdadeiro se o local estiver disponível ou um valor falso se ele não estiver"""

    jogar = False

    if not tabuleiro[jogada['l']][jogada['c']].strip() in 'XO':
        jogar = True

    return jogar


def procura_vencedor():
    """Função utilizada para verificar se um dos jogadores fez uma jogada que desse a vitória a ele,
       para detectar isso o tabuleiro é analisado de quatro formas:

       1 - POR LINHA
       2 - POR COLUNA
       3 - DIAGONAL 1 \
       4 - DIAGONAL 2 /

    sem parâmetros

    return: valor lógico verdadeiro se o jogador fez uma jogada que lhe dá a vitória ou valor falso se ele não fez"""

    # VERIFICAÇÃO POR LINHA
    if tabuleiro[jogada['l']][0].strip() == tabuleiro[jogada['l']][1].strip() == tabuleiro[jogada['l']][
        2].strip() == peca:
        mostra_jogada([(jogada['l'], 0), (jogada['l'], 1), (jogada['l'], 2)])
        return True

    # VERIFICAÇÃO POR COLUNA
    elif tabuleiro[0][jogada['c']].strip() == tabuleiro[1][jogada['c']].strip() == tabuleiro[2][
        jogada['c']].strip() == peca:
        mostra_jogada([(0, jogada['c']), (1, jogada['c']), (2, jogada['c'])])
        return True

    # VERIFICAÇÃO DIAGONAL 1 \
    elif tabuleiro[0][0].strip() == tabuleiro[1][1].strip() == tabuleiro[2][2].strip() == peca:
        mostra_jogada([(0, 0), (1, 1), (2, 2)])
        return True

    # VERIFICAÇÃO DIAGONAL 2 /
    elif tabuleiro[2][0].strip() == tabuleiro[1][1].strip() == tabuleiro[0][2].strip() == peca:
        mostra_jogada([(2, 0), (1, 1), (0, 2)])
        return True

    return False


def mostra_jogada(posicoes):
    """Função usada para destacar a jogada que deu a vitória ao vencedor com a cor verde

    param posicoes: as posições de cada peça da jogada no tabuleiro

    sem return"""

    for p in posicoes:
        tabuleiro[p[0]][p[1]] = f'\033[32m{tabuleiro[p[0]][p[1]]}\033[m'


# PROGRAMA PRINCIPAL


tabuleiro = cria_tabuleiro()  # tabuleiro do jogo
j_jogada = ' '  # variável que armazenara a jogada do jogador

bot = False
cont_bot = 0 # variável utilizada para contabilizar as jogadas feitas pelo computador

print('-' * 31)
print('BEM VINDOS AO JOGO DA VELHA'.center(31))
print('-' * 31)
qtde = qtde_jogadores()

if qtde == 1:
    bot = True

jogadores = criar_jogadores()

print('-' * 31)
print(f'jogador {jogadores["jog1"]["nome"]} sua peça é {jogadores["jog1"]["peca"]}')
print(f'jogador {jogadores["jog2"]["nome"]} sua peça é {jogadores["jog2"]["peca"]}')

cont_jogada = 0  # variável utilizada para contar as jogadas feitas no tabuleiro
vez_jogador = 1  # variável utilizada para definir a vez de qual jogador jogará

jogador_venceu = False  # variável lógica utiliza para definir se o jogador venceu(verdadeiro) ou se não venceu(falso)
while cont_jogada != 9 and not jogador_venceu:

    if vez_jogador == 1:
        jogador = jogadores['jog1']['nome']
        jogador_bot = jogadores['jog1']['bot']
        peca = jogadores['jog1']['peca']
    else:
        jogador = jogadores['jog2']['nome']
        jogador_bot = jogadores['jog2']['bot']
        peca = jogadores['jog2']['peca']

    print('-' * 31)
    print(f'Vez do(a) jogador(a) {jogador}')
    sleep(2)
    mostra_tabuleiro()
    while True:

        sleep(2)
        if not jogador_bot:
            verif_posicoes()
            jogada = jogador_jogada()
            j_jogada = jogada

        else:
            jogada = bot_jogada()
            cont_bot += 1

        if fazer_jogada():
            print('\033[32mJogada feita com sucesso!!\033[m')
            tabuleiro[jogada['l']][jogada['c']] = peca.center(9)
            sleep(4)

            if vez_jogador == 1:
                vez_jogador = 2
            else:
                vez_jogador = 1

            cont_jogada += 1

            if cont_jogada >= 5:
                jogador_venceu = procura_vencedor()

            break

        else:
            if not jogador_bot:
                print('\033[31mEsta posição do tabuleiro já esta ocupada, tente novamente\033[m')


print('-' * 31)
print('O JOGO ACABOU'.center(31))
print('-' * 31)

if jogador_venceu:
    print(f"\033[32mO jogador vencedor é o(a) {jogador}, parâbens\033[m")
    print("\033[32mA jogada que lhe deu a vitória esta destacada em verde no tabuleiro\033[m")
    mostra_tabuleiro()
else:
    print("\033[33mO jogo acabou em empate pois o tabuleiro ficou cheio\033[m")
    mostra_tabuleiro()
