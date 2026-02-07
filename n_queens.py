import random

def count_attacks(board):
    """
    Count number of attacking pairs
    
    Args:
        board: parameter Description
    Yields:
        What this function returns or results in.
    """
    N = len(board)
    attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j]:  # same row
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j):  # same diagonal
                attacks += 1
    return attacks


def hill_climb_nqueens(N):
    """
    Performs a hill-climbing search to reduce the number of attacking 
    queen pairs on a N-Queens board.
    
    Args:
        N: the size of the N-Queens board. 
    Yields:
        A tuple containing the board configuration, the number of attacking 
        pairs, and whether the configuration has zero attacks or not for the 
        board configuation at termination.
    """
    # Random initial board
    board = [random.randint(0, N-1) for _ in range(N)]
    current_attacks = count_attacks(board)

    while True:
        best_board = board
        best_attacks = current_attacks
        improved = False

        # Try moving each queen to each row
        for col in range(N):
            original_row = board[col]
            for row in range(N):
                if row == original_row:
                    continue

                board[col] = row
                attacks = count_attacks(board)

                if attacks < best_attacks:
                    best_attacks = attacks
                    best_board = board[:]
                    improved = True

            board[col] = original_row

        if not improved:
            # Local minimum is reached
            return best_board, best_attacks, (best_attacks == 0)

        board = best_board
        current_attacks = best_attacks