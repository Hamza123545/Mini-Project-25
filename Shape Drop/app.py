import pygame
import streamlit as st
import numpy as np
import io
from PIL import Image


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_board = np.zeros((20, 10)) 
current_piece = np.array([[1, 1, 1], [0, 1, 0]])


def draw_board():
    screen.fill(BLACK)
    for row in range(20):
        for col in range(10):
            if game_board[row][col]:
                pygame.draw.rect(screen, GREEN, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()


def pygame_to_streamlit():
    pygame_image = pygame.Surface.convert(screen, pygame.SRCALPHA) 
    image_bytes = pygame.image.tostring(pygame_image, 'RGB')
    img = Image.open(io.BytesIO(image_bytes))
    return img


def game_loop():
    draw_board()
    st.image(pygame_to_streamlit(), use_column_width=True)
    pygame.time.delay(500)  


if st.button("Start Tetris"):
    game_loop()
