board1 = [
         [0,0,6,0,0,2,0,0,0],
         [0,8,0,0,0,0,0,5,2],
         [0,9,0,0,3,0,0,0,0],
         [0,0,0,0,0,0,4,0,0],
         [1,0,4,0,0,0,0,0,6],
         [3,0,0,0,0,9,1,0,0],
         [0,0,0,6,0,0,0,7,0],
         [0,0,0,1,4,3,0,0,0],
         [0,0,0,9,0,0,8,6,0]
]

board2 = [
         [7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]
]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range (1,10):
        if find_valid(board, i, (row, col)):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
            
    return False
                
    
def find_valid(board, number, pos):
    #row
    for i in range (len(board[0])):
        if board[pos[0]][i] == number and pos[1] != i:
            return False
    #column
    for i in range (len(board)):
        if board[i][pos[1]] == number and pos[0] !=i:
            return False
    #box
    boxx = pos [1] // 3
    boxy = pos [0] // 3
    for i in range (boxy*3, boxy*3 + 3):
        for j in range (boxx*3, boxx*3 + 3):
            if board[i][j] == number and (i,j) != pos:
                return False
    return True
    

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
               print ("-----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i,j)
    return None

print_board(board1)       
print("_______")
solve(board1)
print_board(board1)

