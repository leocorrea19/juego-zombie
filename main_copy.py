import pygame
from modo import *
from nivel_uno import *

#PANTALLA
ANCHO, ALTO = 1280, 720
FPS = 20
flag_sonido = True
flag_inicio_juego = True

pygame.init()
SCREEN = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Zombilandia")
RELOJ = pygame.time.Clock()

nivel_actual = NivelUno(SCREEN)

running = True
while running:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    
    for event in eventos:
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN :
            print(event.pos)
    
    nivel_actual.update(eventos)
        
    pygame.display.update()
pygame.quit() # Fin 