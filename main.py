import pygame
from pong import Game

class PongGame:
    def __init__(self, window, width, height) -> None:
        self.game = Game(window, width, height)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball
        
    def test_ai(self) -> None:
        running = True
        clock = pygame.time.Clock()
        while running:
            # clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                
                # keys = pygame.key.get_pressed()
                # if keys[pygame.K_w]:
                #     game.move_paddle(left=True, up=True)
                # if keys[pygame.K_s]:
                #     game.move_paddle(left=True, up=False)
                
            game_info = self.game.loop()
            self.game.draw()
            pygame.display.update()
        pygame.quit()

width, height = 700, 500
window = pygame.display.set_mode((width, height))

game = PongGame(window, width, height)

game.test_ai()