import solver
import pygame

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640,400
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()
    
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
        
        self.on_cleanup()

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