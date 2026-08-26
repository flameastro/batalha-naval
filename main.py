import random
from src.colors import *

# Regras
# None (■) -> Posição não jogada
# 0 (x) -> Errou (Água)
# 1 (|) -> Navio
# 2 (•) -> Acertou


def criar_mapa(linhas: int, colunas: int) -> list:
    matriz = []
    for linha in range(linhas):
        vetor = []
        for coluna in range(colunas):
            vetor.append(None)

        matriz.append(vetor)

    return matriz


def visualizar_mapa(mapa: list, linhas: int, colunas: int) -> None:
    # Linhas -> Números
    # Colunas -> Letras
    LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    print("", end="  ")

    for i in range(linhas):
        print(BLACK + str(i), end=" ")

    print("")

    for linha in range(linhas):
        print(BLACK + LETRAS[linha], end=" ")
        for coluna in range(colunas):
            valor = mapa[linha][coluna]

            if valor == None:
                print("■", end=" ")
            elif valor == 0:
                print(CYAN + "x", end=" ")
            elif valor == 1:
                print(BLUE + "|", end=" ")
            elif valor == 2:
                print(RED + "•", end=" ")

        print("")


def converter_linha(linha: str) -> int:
    LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    if linha not in LETRAS:
        return -1

    return LETRAS.index(linha)


def valida_posicao(linha: int, coluna: int):
    return (linha >= 0 and linha <= 9) and (coluna >= 0 and coluna <= 9)


def verifica_posicao(linha_inicial: int, coluna_inicial: int, linha: int, coluna: int, i: int):
    pos = None
    if coluna_inicial + i == coluna:
        pos = "direita"
    elif coluna_inicial - i == coluna:
        pos = "esquerda"
    elif linha_inicial + i == linha:
        pos = "baixo"
    elif linha_inicial - i == linha:
        pos = "cima"

    return pos


def conseguir_posicao():
    posicao = input("Posição do mapa (A1/B3/F6): ").upper().strip()
    linha = converter_linha(posicao[0])
    coluna = posicao[1:]

    return [linha, coluna]


def define_posicao_jogador():
    linha, coluna = conseguir_posicao()
    while not coluna.isnumeric():
        linha, coluna = conseguir_posicao()

    while not valida_posicao(linha, int(coluna)):
        linha, coluna = conseguir_posicao()

    return [linha, int(coluna)]


def inserir_navio_jogador(mapa: list, repeticoes: int):
    posicao_inicial = []
    posicao_escolhida = None
    posicao_jogada = None

    for i in range(repeticoes):
        jogada_certa = False

        while not jogada_certa:
            print("-" * 50)
            linha, coluna = define_posicao_jogador()

            if i == 0:
                mapa[linha][coluna] = 1
                posicao_inicial.append(linha)
                posicao_inicial.append(coluna)
                jogada_certa = True
            else:
                linha_inicial = posicao_inicial[0]
                coluna_inicial = posicao_inicial[1]

                if (coluna_inicial + i == coluna and linha_inicial == linha) or (coluna_inicial - i == coluna and linha_inicial == linha) or (linha_inicial + i == linha and coluna_inicial == coluna) or (linha_inicial - i == linha and coluna_inicial == coluna):
                    if i == 1:
                        posicao_escolhida = verifica_posicao(linha_inicial, coluna_inicial, linha, coluna, i)

                        if posicao_escolhida:
                            mapa[linha][coluna] = 1
                            jogada_certa = True
                    else:
                        posicao_jogada = verifica_posicao(linha_inicial, coluna_inicial, linha, coluna, i)

                        if posicao_jogada == posicao_escolhida:
                            mapa[linha][coluna] = 1
                            jogada_certa = True

            if not jogada_certa:
                print("Valor inválido. Tente novamente")

            visualizar_mapa(mapa, LINHAS, COLUNAS)


    return mapa


def inserir_navio_bot(mapa: list, repeticoes: int):
    def verifica_direcao(posicao_escolhida: str, linha: int, coluna: int):
        if posicao_escolhida == "baixo":
            linha += i
        elif posicao_escolhida == "cima":
            linha -= i
        elif posicao_escolhida == "direita":
            coluna += i
        elif posicao_escolhida == "esquerda":
            coluna -= i

        return [linha, coluna]

    primeira_jogada = []
    posicoes_disponiveis = ["cima", "baixo", "direita", "esquerda"]
    posicao_escolhida = None

    for i in range(repeticoes):
        if i == 0:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            primeira_jogada.append(linha)
            primeira_jogada.append(coluna)
            mapa[linha][coluna] = 1
        else:
            if not posicao_escolhida:
                primeira_linha = primeira_jogada[0]
                primeira_coluna = primeira_jogada[1]

                if linha + repeticoes >= 10:
                    posicoes_disponiveis.remove("baixo")
                if linha - repeticoes < 0:
                    posicoes_disponiveis.remove("cima")
                if coluna + repeticoes >= 10:
                    posicoes_disponiveis.remove("direita")
                if coluna - repeticoes < 0:
                    posicoes_disponiveis.remove("esquerda")

                posicao_escolhida = random.choice(posicoes_disponiveis)

                linha, coluna = verifica_direcao(posicao_escolhida, linha, coluna)
                mapa[linha][coluna] = 1
            else:
                linha, coluna = verifica_direcao(posicao_escolhida, primeira_linha, primeira_coluna)
                mapa[linha][coluna] = 1


    return mapa


def atacar_jogador(mapa: list):
    # Bot ataca Jogador
    novo_valor = None

    def gera_posicao():
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        valor = mapa[linha][coluna]
        return [linha, coluna, valor]

    linha, coluna, valor = gera_posicao()
    while valor == 0 or valor == 2:  # já jogado ou já acertado
        linha, coluna, valor = gera_posicao()

    if valor == None:
        novo_valor = 0
    elif valor == 1:
        novo_valor = 2

    mapa[linha][coluna] = novo_valor

    return mapa


def atacar_bot(mapa: list):
    # Jogador ataca Bot
    novo_valor = None

    while not novo_valor:
        linha, coluna = define_posicao_jogador()
        valor = mapa[linha][coluna]

        while valor == 0 or valor == 2:  # já jogado ou já acertado
            linha, coluna = conseguir_posicao()
            valor = mapa[linha][coluna]

        if valor == None:
            novo_valor = 0
        elif valor == 1:
            novo_valor = 2

        mapa[linha][coluna] = novo_valor

    return mapa


LINHAS = 10
COLUNAS = 10

# Jogador
mapa_jogador = criar_mapa(LINHAS, COLUNAS)
mapa_jogador = inserir_navio_jogador(mapa_jogador, 3)

# Bot
mapa_bot = criar_mapa(LINHAS, COLUNAS)
mapa_bot = inserir_navio_bot(mapa_bot, 3)
visualizar_mapa(mapa_bot, LINHAS, COLUNAS)


# Atacar Navios
ataque_bot = atacar_bot(mapa_bot)
visualizar_mapa(ataque_bot, LINHAS, COLUNAS)

# Atacar Navios
ataque_jogador = atacar_jogador(mapa_jogador)
visualizar_mapa(ataque_jogador, LINHAS, COLUNAS)
