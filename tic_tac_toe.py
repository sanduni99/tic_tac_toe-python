

import pygame as pg
import sys
import time
from pygame.locals import *

# Initialize constants
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10, 10, 10)
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Initialize pygame
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# Load and scale images
try:
    initiating_window = pg.image.load("modified_cover.png")
    x_img = pg.image.load("x_modified.png")
    o_img = pg.image.load("o_modified.png")
    initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
    x_img = pg.transform.scale(x_img, (80, 80))
    o_img = pg.transform.scale(o_img, (80, 80))
except pg.error as e:
    print(f"Error loading images: {e}")
    sys.exit(1)

def draw_board():
    screen.fill(white)
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)

def draw_status():
    font = pg.font.Font(None, 30)
    if winner is None:
        if draw:
            text = font.render("It's a Draw!", True, (255, 0, 0))
        else:
            text = font.render(f"{XO}'s Turn", True, (255, 0, 0))
    else:
        text = font.render(f"{winner} Wins!", True, (255, 0, 0))
    screen.blit(text, (10, height + 10))

def check_win():
    global board, winner, draw

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            winner = row[0]
            return

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            return

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        return

    # Check for draw
    draw = True
    for row in board:
        if None in row:
            draw = False
            break

def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    pg.display.update()
    time.sleep(3)

def draw_XO(row, col):
    global board
    posx = col * width / 3 + 30
    posy = row * height / 3 + 30

    if board[row][col] == 'x':
        screen.blit(x_img, (posx, posy))
    elif board[row][col] == 'o':
        screen.blit(o_img, (posx, posy))

def main_game_loop():
    global XO, winner, draw
    game_initiating_window()
    draw_board()
    draw_status()
    pg.display.update()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and winner is None:
                x, y = pg.mouse.get_pos()
                clicked_row = int(y // (height / 3))
                clicked_col = int(x // (width / 3))
                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = XO
                    draw_XO(clicked_row, clicked_col)
                    check_win()
                    if winner is None:
                        if XO == 'x':
                            XO = 'o'
                        else:
                            XO = 'x'
                draw_status()
                pg.display.update()
        CLOCK.tick(fps)

if __name__ == "__main__":
    main_game_loop()

