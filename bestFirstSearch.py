import random
import heapq
import time
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
            if board[i][j]!= 0 and board[i][j] != (3*i + j) :
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

def boardToTuple(board):
    return tuple(tuple(row) for row in board)

def copyBoard(board) :
    newBoard = []
    for i in range(n) :
        temp = []
        for j in range(n) :
            temp.append(board[i][j])
        newBoard.append(temp)
    
    return newBoard

# there is some problem in this implementaion (Jumps diagonally)

def bestFirstSearch(board, pos) :
    pq = []
    visited = set()
    counter = 0
    heapq.heappush(pq, (evaluate(board), counter, board, pos))
    visited.add(boardToTuple(board))
    while pq :
        h, _, curr_board, empty = heapq.heappop(pq)
        printBoard(curr_board)
        time.sleep(1)
        print()
        if h == 0 :
            return
        moves = getMoves(curr_board, empty[0], empty[1])

        for move in moves:
            new_board = copyBoard(curr_board)
            new_board[empty[0]][empty[1]] = new_board[move[0]][move[1]]
            new_board[move[0]][move[1]] = 0
            key = boardToTuple(new_board)
            if key not in visited:
                visited.add(key)
                counter += 1
                heapq.heappush(
                    pq,
                    (evaluate(new_board), counter, new_board, move)
                )
    print("Could Not Find a Solution")

def play() :
    board, pos = generateBoard()
    bestFirstSearch(board, pos)

play()
