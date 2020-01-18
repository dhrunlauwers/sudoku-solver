board = [
    [3,0,1,0,0,4,0,5,0],
    [4,0,7,0,0,0,6,9,0],
    [0,9,0,0,3,0,0,7,1],
    [0,2,8,0,1,0,9,0,7],
    [0,0,0,2,0,7,0,0,0],
    [1,0,6,0,5,0,2,4,0],
    [7,5,0,0,6,0,0,2,0],
    [0,1,3,0,0,0,5,0,9],
    [0,4,0,5,0,0,7,0,6]
]

def print_board(board):

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
# pick empty square

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

#print_board(board)

print(find_empty(board))


# try a number

# find one that works

# repeat until no options work

# backtrack to try something else

#print(board)