# Criar a matriz 10x10
# Visualizar a matriz
# Verificar em quais posições o bot pode colocar os navios
# Verificar em quais posições o jogador pode colocar os navios
# Começar o jogo


def criar_mapa(linhas, colunas):
    matriz = []
    for linha in range(linhas):
        vetor = []
        for coluna in range(colunas):
            vetor.append(0)

        matriz.append(vetor)

    return matriz


def visualizar_mapa(mapa, linhas, colunas):
    # Linhas -> Números
    # Colunas -> Letras
    LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    print("", end="  ")

    for letra in LETRAS:
        print(letra, end=" ")

    print("")

    for linha in range(linhas):
        print(linha, end=" ")

        for coluna in range(colunas):
            if mapa[linha][coluna] == 0:
                print("■", end=" ")

        print("")



LINHAS = 10
COLUNAS = 10
mapa_jogador = criar_mapa(LINHAS, COLUNAS)
visualizar_mapa(mapa_jogador, LINHAS, COLUNAS)