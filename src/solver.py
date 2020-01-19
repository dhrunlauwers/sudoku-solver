def print_board(board):
# takes a board, and prints it to console
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
# takes a board, and returns a tuple representing the position of the first available empty square
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    
    return None

def valid(board, num, pos):
#takes a board, value, and position on the board, and checks whether this entry is valid
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    #check square (3x3)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(board):
#takes a board, finds the first empty square, and checks whether there is a valid solution
    find = find_empty(board)
    if not find:
        #solution found
        return True
    else:
        #unpack empty
        row, col = find

    # iterate through possible numbers
    for i in range(1,10):
        #if valid, change number and solve again
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

