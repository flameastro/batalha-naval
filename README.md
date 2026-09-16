# 🚢 batalha-naval

Batalha Naval simples desenvolvido em Python 🐍, executado diretamente no terminal.

O projeto simula uma partida entre o jogador e o computador, permitindo posicionar um navio no tabuleiro e realizar ataques até que um dos lados acerte todas as posições do navio adversário.

## 🎮 Como Jogar

### 1. Execute o jogo

No terminal, execute o arquivo principal:

```bash
python main.py
```

ou caso tenha python3:

```bash
python3 main.py
```

### 2. Posicione seu navio

O jogo exibirá um mapa de 10×10 e solicitará uma posição inicial para o seu navio.

Informe a posição utilizando uma letra e um número.

Exemplos:

* `A1`
* `B3`
* `F6`

O navio possui **3 posições** e deve ser colocado em linha reta, na horizontal ou na vertical.

### 3. Ataque o computador

Após posicionar seu navio, você poderá escolher as posições do mapa do computador para realizar ataques.

O computador também realizará ataques aleatórios ao seu mapa.

### 4. Vença a partida

O primeiro jogador a acertar as **3 posições do navio adversário** vence a partida 🏆

## 🗺️ Legenda do Mapa

| Símbolo | Significado                        |
| ------- | ---------------------------------- |
| ■       | Posição não jogada ou navio oculto |
| x       | Água — ataque que errou            |
| |       | Navio                              |
| •       | Ataque que acertou o navio         |

## 🛠️ Tecnologias

* Python 3
