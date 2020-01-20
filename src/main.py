import solver
import pygame
import game

if __name__ == "__main__":
    #theGame = Game()
    #theGame.on_execute()
    

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

    solver.print_board(board)
    solver.solve(board)
    print("")
    print("")
    solver.print_board(board)