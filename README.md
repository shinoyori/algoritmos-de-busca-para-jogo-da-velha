## Jogo da Velha com IA

Este projeto em Python implementa o clássico **Jogo da Velha (Tic-Tac-Toe)**, onde o jogador humano compete contra a Inteligência Artificial (IA) do computador. O diferencial do projeto é a implementação de **quatro algoritmos de busca adversária** para a tomada de decisão da IA. Foi desenvolvido para a disciplina de Inteligência Artifical na UFSCar (Universidade Federal de São Carlos)

O jogador (Humano) joga com `[O]` e o computador (IA) joga com `[X]` 

### Algoritmos de IA Implementados

O jogador pode escolher entre quatro estratégias diferentes para o computador, que garantem um jogo ótimo ou quase-ótimo (dependendo da profundidade máxima):

1.  **Minimax Clássico (`classicMinmax`, `minimax`)**:

      * Algoritmo fundamental da Teoria dos Jogos.
      * A IA (Maximizer) tenta **maximizar** sua pontuação, assumindo que o oponente (Minimizer) sempre tentará **minimizar** essa pontuação.
      * No Jogo da Velha, busca a melhor jogada ao simular todas as sequências de jogo até o final.
      * A função de avaliação (`eval_state`) retorna: `+1` (Vitória IA), `-1` (Vitória Humano) ou `0` (Empate).

2.  **Minimax com Poda Alpha-Beta (`minimax_alpha_beta`)**:

      * Uma otimização do Minimax Clássico.
      * Evita calcular estados irrelevantes na árvore de busca, descartando ramos que não irão afetar a decisão final (quando o valor de $\beta$ é menor ou igual ao valor de $\alpha$).
      * **$\alpha$ (Alpha)**: O melhor valor (mais alto) que o jogador maximizador pode garantir até o momento.
      * **$\beta$ (Beta)**: O melhor valor (mais baixo) que o jogador minimizador pode garantir até o momento.
      * Resulta em um algoritmo muito mais **eficiente** em termos de tempo de execução.

3.  **Minimax com Profundidade Limitada (`depthMinmax`, `min_max`)**:

      * Versão modificada do Minimax que explora a árvore de busca até uma **profundidade máxima predefinida** (`profundidade_maxima = 9`).
      * Para o Jogo da Velha, com no máximo 9 jogadas, a profundidade máxima é suficiente para explorar o jogo completo. Em jogos mais complexos, o limite de profundidade é usado para tomar decisões em tempo razoável.

4.  **Negamax (`negamax`)**:

      * Uma variação do Minimax que explora a propriedade de **soma zero** dos jogos de dois jogadores (o valor de uma posição para um jogador é a negação do valor para o outro jogador).
      * Simplifica a implementação do algoritmo Minimax, unificando a lógica de maximização e minimização em uma única função recursiva.
      * Cada chamada recursiva nega o valor retornado pelo oponente (`val = -negamax(...)`).

### 💻 Como Executar

1.  Salve o código como `main.py`.

2.  Execute o arquivo a partir da linha de comando:

    ```bash
    python main.py
    ```

3.  O programa solicitará que você **escolha o algoritmo** de IA (1 a 4).

4.  O jogo será iniciado e você (`[O]`) fará o primeiro movimento, digitando o índice da casa (de 0 a 8) onde deseja jogar.

-----

Se precisar de ajuda para executar o código ou entender melhor algum dos algoritmos, é só perguntar\!
