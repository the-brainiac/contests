from collections import Counter


def winner(tictac_board, s):
    for i in range(3):
        
        if tictac_board[i][0] == tictac_board[i][1] == tictac_board[i][2] == s:
            return True
        
        if tictac_board[0][i] == tictac_board[1][i] == tictac_board[2][i] == s:
            return True
    
    
    if (tictac_board[0][0] == tictac_board[1][1] == tictac_board[2][2] == s) or (tictac_board[0][2] == tictac_board[1][1] == tictac_board[2][0] == s):
        return True
        
    return False
    
def count_symbol(tictac_board, s):
    res = 0
    for i in range(3):
        for j in range(3):
            if tictac_board[i][j] == s:
                res += 1
    return res

def case3(tictac_board):
    
    total_X = count_symbol(tictac_board, 'X')
    total_Y = count_symbol(tictac_board, 'O')
    if total_Y > total_X or (total_X-total_Y) >1:
        return True
        
    if (winner(tictac_board, 'X') and winner(tictac_board, 'O')):
        return True
    if winner(tictac_board, 'X') and (total_X==total_Y):
        return True
    if winner(tictac_board, 'O') and (total_X>total_Y):
        return True
    return False

def solve(tictac_board):
    if case3(tictac_board):
        return 3
    
    if (winner(tictac_board, 'X') or winner(tictac_board, 'O')) or count_symbol(tictac_board, '_')==0:
        return 1
    return 2
    

for t in range(int(input())):
    tictac_board = [input().strip() for i in range(3)]
    
    print(solve(tictac_board))