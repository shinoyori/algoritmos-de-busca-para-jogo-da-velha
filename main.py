import random

NUM_ACTIONS = 9
gameEnded = False
profundidade_maxima = 9

## JOGO DA VELHA ---------------------------------------------------------------

def print_symbol(s):
    if s == 1:
        return "[X]"
    elif s == 2:
        return "[O]"
    else:
        return "[ ]"

def print_grid_moves():
    for i in range(9):
        print(f"[{i}]", end="")
        if i in {2, 5, 8}:
            print()
    print("")

def print_grid(state):
    for i in range(9):
        print(print_symbol(state[i]), end="")
        if i in {2, 5, 8}:
            print()
    print("")

def eval_state(state):
    # Player 1 (Computador) = MAXIMIZER = +1
    # Player 2 (Humano) = MINIMIZER = -1
    # Empate = 0
    if is_winner(state, 1):
        return 1
    elif is_winner(state, 2):
        return -1
    else:
        return 0

def is_winner(state, player):
    return ((state[0] == state[1] == state[2] == player) or
            (state[3] == state[4] == state[5] == player) or
            (state[6] == state[7] == state[8] == player) or
            (state[0] == state[3] == state[6] == player) or
            (state[1] == state[4] == state[7] == player) or
            (state[2] == state[5] == state[8] == player) or
            (state[0] == state[4] == state[8] == player) or
            (state[2] == state[4] == state[6] == player))

## NEGAMAX --------------------------------------

def negamax(p, state):
    move = -1
    valid_moves = [i for i in range(len(state)) if state[i] == 0]
    # Recompensa relativa ao jogador P: 1 se P ganha, -1 se P perde, 0 se empate
    reward = eval_state(state) * (1 if p == 1 else -1) 

    if reward != 0 or len(valid_moves) < 1:
        return [reward, move]

    best_value = -float('inf') 

    for i in valid_moves:
        tmp_state = state[:]
        tmp_state[i] = p
        
        # Negação do valor retornado do oponente
        val = -negamax(2 if p == 1 else 1, tmp_state)[0] 

        if val > best_value:
            best_value = val
            move = i

    return [best_value, move]


## MINIMAX CLÁSSICO ----------------------------

def minimax(board, depth, is_maximizing):
    score = eval_state(board)
    if score != 0 or not any(cell == 0 for cell in board):
        return score

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = 1  # Maximizer (Comp, 1) joga
                best = max(best, minimax(board, depth + 1, False))
                board[i] = 0
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = 2  # Minimizer (Humano, 2) joga
                best = min(best, minimax(board, depth + 1, True))
                board[i] = 0
        return best

def classicMinmax(board):
    best_val = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            move_val = minimax(board, 0, False) 
            board[i] = 0
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_val, best_move


## MINIMAX COM ALPHA-BETA -------------------------------------

def minimax_alpha_beta(state, depth, alpha, beta, maximizing_player):
    valid_moves = [i for i in range(len(state)) if state[i] == 0]
    reward = eval_state(state)

    if reward != 0 or not valid_moves:
        return reward, -1

    if maximizing_player:
        best_value = -float('inf')
        best_move = -1
        for move in valid_moves:
            tmp_state = state[:]
            tmp_state[move] = 1
            val, _ = minimax_alpha_beta(tmp_state, depth + 1, alpha, beta, False)
            if val > best_value:
                best_value = val
                best_move = move
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value, best_move
    else:
        best_value = float('inf')
        best_move = -1
        for move in valid_moves:
            tmp_state = state[:]
            tmp_state[move] = 2
            val, _ = minimax_alpha_beta(tmp_state, depth + 1, alpha, beta, True)
            if val < best_value:
                best_value = val
                best_move = move
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value, best_move

## MINIMAX COM PROFUNDIDADE LIMITADA ----------------------

def min_max(state, profundidade, jogador):
    resultado = eval_state(state)
    if resultado != 0 or profundidade == 0:
        return resultado

    movimentos_validos = [i for i in range(len(state)) if state[i] == 0]

    if jogador == 1: # Maximizer
        melhor_valor = -float('inf')
        for i in movimentos_validos:
            estado_temp = state[:]
            estado_temp[i] = 1
            valor = min_max(estado_temp, profundidade - 1, 2)
            melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else: # Minimizer
        melhor_valor = float('inf')
        for i in movimentos_validos:
            estado_temp = state[:]
            estado_temp[i] = 2
            valor = min_max(estado_temp, profundidade - 1, 1)
            melhor_valor = min(melhor_valor, valor)
        return melhor_valor

def depthMinmax(state, jogador):
    movimentos_validos = [i for i in range(len(state)) if state[i] == 0]
    melhor_valor = -float('inf') if jogador == 1 else float('inf')
    movimento_escolhido = -1

    for i in movimentos_validos:
        estado_temp = state[:]
        estado_temp[i] = jogador
        # A profundidade inicial é profundidade_maxima - 1, pois o movimento do loop já consome uma profundidade
        valor = min_max(estado_temp, profundidade_maxima - 1, 2 if jogador == 1 else 1)

        if (jogador == 1 and valor > melhor_valor) or (jogador == 2 and valor < melhor_valor):
            melhor_valor = valor
            movimento_escolhido = i

    return melhor_valor, movimento_escolhido

## MAIN ---------------------------------------------------------------------

def main():
    global gameEnded
    cur_state = [0] * NUM_ACTIONS
    print("Você é:", print_symbol(2))
    print("O computador é:", print_symbol(1))
    print("Movimentos:")
    print_grid_moves()
    print_grid(cur_state)

    print("Escolha o algoritmo:")
    print("1 - Minimax")
    print("2 - Minimax com Podagem Alfa Beta")
    print("3 - Minimax com Profundidade Limitada")
    print("4 - Negamax")
    choice = int(input("Entre sua escolha: "))

    cur_player = 2  
    moves_remaining = NUM_ACTIONS
    gameEnded = False

    while not gameEnded:
        if cur_player == 2:
            move = int(input("Digite seu movimento: "))
            if cur_state[move] == 0:
                cur_state[move] = 2
            else:
                print("Escolha inválida. Tente novamente")
                continue
        else:
            if choice == 1:
                _, AIMOVE = classicMinmax(cur_state)
            elif choice == 2:
                _, AIMOVE = minimax_alpha_beta(cur_state, 0, -float('inf'), float('inf'), True)
            elif choice == 3:
                _, AIMOVE = depthMinmax(cur_state, 1)
            elif choice == 4:
                _, AIMOVE = negamax(1, cur_state)
            else:
                print("Escolha inválida.")
                return

            if AIMOVE > -1:
                cur_state[AIMOVE] = 1
            else:
                print("Agente não encontrou movimentos. Fim de jogo.")
                gameEnded = True
                break

        moves_remaining -= 1
        reward = eval_state(cur_state)
        print_grid(cur_state)

        if reward == 1 or reward == -1:
            print("Fim de Jogo!")
            print(f"Vencedor: {print_symbol(1) if reward == 1 else print_symbol(2)}")
            gameEnded = True
        elif moves_remaining <= 0:
            print("Empate!")
            gameEnded = True

        cur_player = 2 if cur_player == 1 else 1

if __name__ == "__main__":
    main()