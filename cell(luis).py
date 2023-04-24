import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.font = pygame.font.SysFont('arialblack', 4)
        self.value = value
        self.row = int(row)
        self.col = int(col)
        self.screen = screen

        self.baseimg = pygame.image.load('white.png').convert_alpha()
        self.image = pygame.transform.scale(self.baseimg, (int(200/3 - 4), int(200/3 - 4)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (int((self.col - 1) * (200/3) + 4), int((self.row - 1) * (200/3) + 4))
        self.clicked = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        if int(self.value) != 0:
            img = (self.value, True, (0, 0, 0))
            self.screen.blit(img, (int((self.col - 1) * (200/3) + 20), int((self.row - 1) * (200/3) + 20)))

        pos = pygame.mouse.get_pos()
        action = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
        elif self.rect.collidepoint(pos) is False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = False

        if action is True:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (int((self.col - 1) * (200 / 3) + 2), int((self.row - 1) * (200 / 3) + 2), 200 / 3 - 2, 200 / 3 - 2))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


