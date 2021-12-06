import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        self.orig_left = self.left
        self.orig_top = self.top
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, 'white', (self.left, self.top, self.cell_size, self.cell_size), 1)
                self.left += self.cell_size
            self.top += self.cell_size
            self.left = self.orig_left
        self.top = self.orig_top