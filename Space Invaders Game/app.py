import pygame
import streamlit as st


pygame.init()


screen = pygame.display.set_mode((600, 400))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip() 
    
  
    pygame_image = pygame.image.tostring(screen, 'RGB')
    
    
    st.image(pygame_image)
