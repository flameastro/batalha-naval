import random


# Criar a matriz 10x10
# Visualizar a matriz
# Verificar em quais posições o bot pode colocar os navios
# Verificar em quais posições o jogador pode colocar os navios
# Começar o jogo


# TODO: verificar se posição que o usuário insere já está ocupada no mapa. Por exemplo, A1 -> A1 (repetido)

# Regras
# None (■) -> Posição não jogada
# 0 (x) -> Errou (Água)
# 1 (|) -> Navio
# 2 (•) -> Acertou


def criar_mapa(linhas, colunas):
    matriz = []
    for linha in range(linhas):
        vetor = []
        for coluna in range(colunas):
            vetor.append(None)

        matriz.append(vetor)

    return matriz


def visualizar_mapa(mapa, linhas, colunas):
    # Linhas -> Números
    # Colunas -> Letras
    LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    print("", end="  ")

    for i in range(linhas):
        print(i, end=" ")

    print("")

    for linha in range(linhas):
        print(LETRAS[linha], end=" ")
        for coluna in range(colunas):
            valor = mapa[linha][coluna]

            if valor == None:
                print("■", end=" ")
            elif valor == 0:
                print("x", end=" ")
            elif valor == 1:
                print("|", end=" ")
            elif valor == 2:
                print("•", end=" ")

        print("")


def converter_linha(linha):
    LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for i in range(len(LETRAS)):
        if linha == LETRAS[i]:
            linha = i
            break

    return linha


def define_posicao(linha_inicial, coluna_inicial, linha, coluna, i):
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


def define_posicao_jogador():
    posicao = input("Posição do mapa (A1/B3/F6): ").upper().strip()
    linha = converter_linha(posicao[0])
    coluna = int(posicao[1:])

    return [posicao, linha, coluna]


def inserir_navio_jogador(mapa, repeticoes):
    posicao_inicial = []
    posicao_escolhida = None
    posicao_jogada = None

    for i in range(repeticoes):
        jogada_certa = False

        while not jogada_certa:
            print("-" * 50)
            posicao, linha, coluna = define_posicao_jogador()

            if i == 0:
                mapa[linha][coluna] = 1
                posicao_inicial.append(linha)
                posicao_inicial.append(coluna)

                linha_inicial = posicao_inicial[0]
                coluna_inicial = posicao_inicial[1]
                jogada_certa = True
            else:
                if (coluna_inicial + i == coluna and linha_inicial == linha) or (coluna_inicial - i == coluna and linha_inicial == linha) or (linha_inicial + i == linha and coluna_inicial == coluna) or (linha_inicial - i == linha and coluna_inicial == coluna):
                    if i == 1:
                        posicao_escolhida = define_posicao(linha_inicial, coluna_inicial, linha, coluna, i)

                        if posicao_escolhida:
                            mapa[linha][coluna] = 1
                            jogada_certa = True
                    else:
                        posicao_jogada = define_posicao(linha_inicial, coluna_inicial, linha, coluna, i)

                        print(posicao_jogada, posicao_escolhida)
                        if posicao_jogada == posicao_escolhida:
                            mapa[linha][coluna] = 1
                            jogada_certa = True


            visualizar_mapa(mapa, LINHAS, COLUNAS)


    return mapa


def inserir_navio_bot(mapa, repeticoes):
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
            # Ver as jogadas disponíveis
            # Escolher umas dessas jogadas aleatóriamente
            # Preencher
            if not posicao_escolhida:
                primeira_linha = primeira_jogada[0]
                primeira_coluna = primeira_jogada[1]

                # if linha + repeticoes >= 10:
                #     # posicoes_disponiveis.remove("baixo")
                #     posicoes_disponiveis.remove("direita")
                # if linha - repeticoes < 0:
                #     posicoes_disponiveis.remove("esquerda")
                # if coluna + repeticoes >= 10:
                #     # posicoes_disponiveis.remove("direita")
                #     posicoes_disponiveis.remove("baixo")
                # if coluna - repeticoes < 0:
                #     posicoes_disponiveis.remove("cima")

                if linha + repeticoes >= 10:
                    posicoes_disponiveis.remove("baixo")
                if linha - repeticoes < 0:
                    posicoes_disponiveis.remove("cima")
                if coluna + repeticoes >= 10:
                    posicoes_disponiveis.remove("direita")
                if coluna - repeticoes < 0:
                    posicoes_disponiveis.remove("esquerda")

                posicao_escolhida = random.choice(posicoes_disponiveis)
                print(posicao_escolhida)

                if posicao_escolhida == "baixo":
                    linha += i
                elif posicao_escolhida == "cima":
                    linha -= i
                elif posicao_escolhida == "direita":
                    coluna += i
                elif posicao_escolhida == "esquerda":
                    coluna -= i

                mapa[linha][coluna] = 1
            else:
                if posicao_escolhida == "baixo":
                    primeira_linha += i
                elif posicao_escolhida == "cima":
                    primeira_linha -= i
                elif posicao_escolhida == "direita":
                    primeira_coluna += i
                elif posicao_escolhida == "esquerda":
                    primeira_coluna -= i

                mapa[primeira_linha][primeira_coluna] = 1


    return mapa


LINHAS = 10
COLUNAS = 10

# Jogador
mapa_jogador = criar_mapa(LINHAS, COLUNAS)
mapa_jogador = inserir_navio_jogador(mapa_jogador, 3)

# Bot
# mapa_bot = criar_mapa(LINHAS, COLUNAS)
# mapa_bot = inserir_navio_bot(mapa_bot, 3)
# visualizar_mapa(mapa_bot, LINHAS, COLUNAS)
