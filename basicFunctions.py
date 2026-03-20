import random

n = 3

def generateBoard() :
    board = []
    options = []
    for i in range(n**2) :
        options.append(i)
    for i in range(n) :
        temp = []
        for j in range(n) :
            option = random.choice(options)
            temp.append(option)
            options.remove(option)
        board.append(temp)
    return board

def evaluate(board) :
    eval = 0
    for i in range(n) :
        for j in range(n) :
            x = int(board[i][j]/3)
            y = board[i][j]%3
            if board[i][j] != (3*i + j) :
                eval += (abs(x-i) + abs(y-j))
    return eval

def printBoard(board):
    for i in range(n):
        for j in range(n):
            val = board[i][j]
            if val == 0:
                print(f"{'_':^3}", end=" ")
            else:
                print(f"{val:^3}", end=" ")
        print()  

def getMoves(board) :
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    moves = []
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 0 :
                for k in range(4) :
                    x = i + dx[k]
                    y = j + dy[k]
                    if x >= 0 and x < n and y >= 0 and y < n :
                        moves.append([x,y])
    return moves

# board = generateBoard()
# printBoard(board)
# print(evaluate(board))
# moves = getMoves(board)
# print(moves)

# for i in range (100000) :
#     board = generateBoard()
#     eval = evaluate(board)
#     if eval < 6 :
#         print(i)
#         print(eval)
#         printBoard(board)
#         print()
