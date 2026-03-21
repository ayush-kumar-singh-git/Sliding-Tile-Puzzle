import random

n = 3

def generateBoard() :
    board = []
    options = []
    empty = []
    for i in range(n**2) :
        options.append(i)
    for i in range(n) :
        temp = []
        for j in range(n) :
            option = random.choice(options)
            if option == 0 :
                empty.append(i)
                empty.append(j)
            temp.append(option)
            options.remove(option)
        board.append(temp)
    return board, empty

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

def getMoves(board, i ,j) :
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    moves = []
    for k in range(4) :
        x = i + dx[k]
        y = j + dy[k]
        if x >= 0 and x < n and y >= 0 and y < n :
            moves.append([x,y])
    return moves

def playRandomGame()  :
    board, empty = generateBoard()
    printBoard(board)
    print()
    cnt = 0
    while(evaluate(board) != 0) :
        cnt += 1
        moves = getMoves(board, empty[0], empty[1])
        move = random.choice(moves)
        board[empty[0]][empty[1]] = board[move[0]][move[1]]
        board[move[0]][move[1]] = 0
        empty = move
        printBoard(board)
        print()
    print(f"Moves : {cnt}")
playRandomGame()
