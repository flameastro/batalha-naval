# Criar a matriz 10x10
# Visualizar a matriz
# Verificar em quais posições o bot pode colocar os navios
# Verificar em quais posições o jogador pode colocar os navios
# Começar o jogo


# TODO: verificar se posição que o usuário insere já está ocupada no mapa. Por exemplo, A1 -> A1 (repetido)

# Regras
# None (■) -> Posição não jogada
# 0 (x) -> Errou (Água)
# 1 (•) -> Acertou


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
                print("•", end=" ")

        print("")


def converter_linha(linha):
    LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for i in range(len(LETRAS)):
        if linha == LETRAS[i]:
            linha = i
            break

    return linha


def inserir_navio_jogador(mapa, repeticoes):
    posicao_inicial = []
    posicao_escolhida = None
    posicao_jogada = None

    for i in range(repeticoes):
        print("-" * 50)
        posicao = input("Posição do mapa (A1/B3/F6): ").upper().strip()
        linha = converter_linha(posicao[0])
        coluna = int(posicao[1:])

        # posicoes_disponiveis = ["cima", "baixo", "esquerda", "direita"]

        if i == 0:
            mapa[linha][coluna] = 1
            posicao_inicial.append(linha)
            posicao_inicial.append(coluna)

            linha_inicial = posicao_inicial[0]
            coluna_inicial = posicao_inicial[1]

            # Análise das posições -> Remove direções impossíveis
            # ! Trocar caso erros
            # EDIT: Provavelmente inútil
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
        else:
            if coluna_inicial + i == coluna or coluna_inicial - i == coluna or linha_inicial + i == linha or linha_inicial - i == linha:
                if i == 1:
                    # Pega a posição escolhida do jogador
                    # ! Usar função caso necessário
                    if coluna_inicial + 1 == coluna:
                        posicao_escolhida = "direita"
                    elif coluna_inicial - 1 == coluna:
                        posicao_escolhida = "esquerda"
                    elif linha_inicial + 1 == linha:
                        posicao_escolhida = "baixo"
                    elif linha_inicial - 1 == linha:
                        posicao_escolhida = "cima"
                    print(posicao_escolhida)

                    if posicao_escolhida:
                        mapa[linha][coluna] = 1
                else:
                    # ! Usar função caso necessário
                    if coluna_inicial + i == coluna:
                        posicao_jogada = "direita"
                    elif coluna_inicial - i == coluna:
                        posicao_jogada = "esquerda"
                    elif linha_inicial + i == linha:
                        posicao_jogada = "baixo"
                    elif linha_inicial - i == linha:
                        posicao_jogada = "cima"

                    print(posicao_jogada, posicao_escolhida)
                    if posicao_jogada == posicao_escolhida:
                        mapa[linha][coluna] = 1

        visualizar_mapa(mapa_jogador, LINHAS, COLUNAS)


    return mapa


LINHAS = 10
COLUNAS = 10
mapa_jogador = criar_mapa(LINHAS, COLUNAS)
mapa_jogador = inserir_navio_jogador(mapa_jogador, 3)
