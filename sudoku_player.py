import sys
import pygame
from button import Button

def draw_big_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (0, i * 200), (600, i * 200), 4)

    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (i * 200, 0), (200 * i, 600), 4)


def draw_small_lines():
    for i in range(1, 9):
        pygame.draw.line(screen, (0, 0, 0), (0, i * (200/3)), (600, i * (200/3)), 2)

    for i in range(1, 9):
        pygame.draw.line(screen, (0, 0, 0), (i * (200/3), 0), (i * (200/3), 600), 2)


pygame.font.init()
font = pygame.font.SysFont('comic sans', 35)


def menu_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((600, 600))

ez_img = pygame.image.load('easy.png').convert_alpha()
ok_img = pygame.image.load('okay.png').convert_alpha()
hard_img = pygame.image.load('hard.png').convert_alpha()
start_img = pygame.image.load('start.png').convert_alpha()
quit_img = pygame.image.load('quit.png').convert_alpha()

start_button = Button(100, 250, start_img, 1)
ez_button = Button(25, 400, ez_img, 0.5)
ok_button = Button(225, 400, ok_img, 0.5)
hard_button = Button(425, 400, hard_img, 0.5)
quit_button = Button(150, 25, quit_img, 0.75)

game = True
game_start = 'a'
while game:
    screen.fill([255, 255, 255])

    if game_start == 'a':
        menu_text("Welcome to Sudoku", font, (0, 0, 0), 140, 150)
        if start_button.draw(screen):
            game_start = 'b'
        elif quit_button.draw(screen):
            game = False

    elif game_start == 'b':
        menu_text('Choose difficulty:', font, (0, 0, 0), 140, 200)
        if ez_button.draw(screen):
            diff = 1
            game_start = 'c'
        elif ok_button.draw(screen):
            diff = 2
            game_start = 'c'
        elif hard_button.draw(screen):
            diff = 3
            game_start = 'c'
        elif quit_button.draw(screen):
            game = False

    elif game_start == 'c':
        draw_big_lines()
        draw_small_lines()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
