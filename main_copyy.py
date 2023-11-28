import pygame
import menu_inicio
import datos_del_jugador
from class_personaje import *
from class_enemigo import *
from configuraciones import *
from modo import *

#PANTALLA
ANCHO, ALTO = 1280, 720
FPS = 20
flag_sonido = True
flag_inicio_juego = True

pygame.init()
SCREEN = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Zombilandia")
RELOJ = pygame.time.Clock()

#FONDO 
#fondo_menu = menu_inicio.menu_principal(SCREEN)
fondo_nivel = pygame.image.load("imagenes/mapa.png")
fondo_nivel = pygame.transform.scale(fondo_nivel, (ANCHO, ALTO))

#PERSONAJE
diccionario_animaciones = {}
diccionario_animaciones["quieto"] = pj_principal_quieto_d
diccionario_animaciones["quieto_i"] = pj_principal_quieto_i
diccionario_animaciones["derecha"] = pj_principal_caminando_d
diccionario_animaciones["izquierda"] = pj_principal_caminando_i
diccionario_animaciones["salta_d"] = pj_principal_salta_d
diccionario_animaciones["salta_i"] = pj_principal_salta_i

pj_principal = Personaje(diccionario_animaciones, 100, 600, (80, 70), 10, "quieto")

#ENEMIGO 1
diccionario_animaciones_enemigo_1 = {}
diccionario_animaciones_enemigo_1["izquierda"] = enemigo_1_camina_i
diccionario_animaciones_enemigo_1["derecha"] = enemigo_1_camina_d
diccionario_animaciones_enemigo_1["muere_i"] = enemigo_1_muere_i
diccionario_animaciones_enemigo_1["muere_d"] = enemigo_1_muere_d

enemigo_1 = Enemigo(diccionario_animaciones_enemigo_1, 1000, 600, (80, 70))

#PLATAFORMAS
piso = crear_plataforma(False, (ANCHO, 20), (0, 660))

piso_2 = crear_plataforma(False, (345, 2), (21, 515))

lista_plataformas = [piso, piso_2]

pj_principal.rectangulo.bottom = piso["rectangulo"].top

enemigo_1.rectangulo_enemigo.bottom = piso["rectangulo"].top

lista_enemigos = [enemigo_1]
#MUSICA
# sonido_fondo = pygame.mixer.Sound("juego zombie/sonidos/Alan Walker - The Spectre.mp3")
# sonido_fondo.set_volume(0.1)
# sonido_fondo.play()

datos_jugador = datos_del_jugador.JugadorUsuario()

running = True
while running:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    
    # boton_inicio = menu_inicio.boton_iniciar_juego(SCREEN)
    # boton_score = menu_inicio.boton_score(SCREEN)
    # boton_salir = menu_inicio.boton_salir(SCREEN)
    
        
    # boton_sonido = menu_inicio.boton_sonido(SCREEN, flag_sonido)
    
    for event in eventos:
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN :
            print(event.pos)
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()
            
        #     if boton_inicio.collidepoint(event.pos):
        #         flag_inicio_juego = False
                            
        #     elif flag_inicio_juego == True:
        #         if boton_salir.collidepoint(event.pos):
        #             running = False
                
        #     if boton_sonido.collidepoint(event.pos):
        #         if flag_sonido == True:
        #             sonido_fondo.stop()
        #             flag_sonido = False
        #         else:
        #             sonido_fondo.play()
        #             flag_sonido = True
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        pj_principal.accion = "derecha"
        pj_principal.estado_donde_mira = True
    elif teclas[pygame.K_LEFT]:
        pj_principal.accion = "izquierda"
        pj_principal.estado_donde_mira = False
    
    elif teclas[pygame.K_UP]:
        pj_principal.accion = "salta"
        
    else:
        pj_principal.accion = "quieto"
    
    SCREEN.blit(fondo_nivel, (0,0))
    
    pj_principal.actualizar(SCREEN, lista_plataformas)
    
    if not enemigo_1.esta_muerto:
        enemigo_1.actualizar(SCREEN)
    
    pj_principal.verificar_colision_enemigo(enemigo_1)
    
    for enemigo in lista_enemigos:
        if enemigo_1.esta_muerto:
            del enemigo
    
    if obtener_modo():
        
        pygame.draw.rect(SCREEN, "red", pj_principal.rectangulo, 3)
            
        for enemigo in lista_enemigos:
            if not enemigo.esta_muerto:
                pygame.draw.rect(SCREEN, "green", enemigo.rectangulo_enemigo, 3)
        
        for plataformas in lista_plataformas:
            pygame.draw.rect(SCREEN, "blue", plataformas["rectangulo"], 3)
        
        
    pygame.display.update()
pygame.quit() # Fin