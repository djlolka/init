import pygame

from Board import Board

board = Board(5, 7)
board.set_view(100, 100, 50)
running = True
screen = pygame.display.set_mode((500, 500))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    board.render(screen)
    pygame.display.flip()