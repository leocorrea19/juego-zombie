import pygame
from modo import *
from class_personaje import *
from class_enemigo import *
from configuraciones import *
from nivel_uno import *

class Nivel:
    def __init__(self, screen, personaje_principal, lista_plataformas, lista_enemigos, lista_colisiones_rect_direccion_enemigo, lista_trampas,imagen_fondo):
        self.pantalla = screen
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.enemigos = lista_enemigos
        self.colisiones_rect_direccion_enemigo = lista_colisiones_rect_direccion_enemigo
        self.trampas = lista_trampas
        self.img_fondo = imagen_fondo
    
    def update(self, lista_eventos):
        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    cambiar_modo()
        
        self.leer_teclas()
        self.actualizar_pantalla()   
        self.dibujar_rectangulos()
        
    def actualizar_pantalla(self):
        self.pantalla.blit(self.img_fondo, (0, 0))
        
        for jugador in self.jugador:
            jugador.actualizar(self.pantalla, self.plataformas)
            if jugador.vidas <= 0:
                self.jugador.remove(jugador)
        
        for enemigo in self.enemigos:
            enemigo.actualizar(self.pantalla)
        
        for enemigo in self.enemigos:
            for rect in self.colisiones_rect_direccion_enemigo:    
                enemigo.colision_rect_donde_camina(rect)
            
        for enemigo in self.enemigos:
            for jugador in self.jugador:
                jugador.verificar_colision_enemigo(enemigo)
            
                
        for trampa in self.trampas:
            self.img_fondo.blit(trampa["superficie"], trampa["rectangulo"])
        
    def leer_teclas(self):
        teclas = pygame.key.get_pressed()
        
        for jugador in self.jugador:
            if teclas[pygame.K_RIGHT]:
                jugador.accion = "derecha"
                jugador.estado_donde_mira = True
            elif teclas[pygame.K_LEFT]:
                jugador.accion = "izquierda"
                jugador.estado_donde_mira = False
            
            elif teclas[pygame.K_UP]:
                jugador.accion = "salta"
                
            else:
                jugador.accion = "quieto"
    
    def dibujar_rectangulos(self):
        if obtener_modo():
            for jugador in self.jugador:
                pygame.draw.rect(self.pantalla, "red", jugador.rectangulo, 3)
                
            for enemigo in self.enemigos:
                if not enemigo.esta_muerto:
                    pygame.draw.rect(self.pantalla, "green", enemigo.rectangulo_enemigo, 3)
            
            for plataformas in self.plataformas:
                pygame.draw.rect(self.pantalla, "blue", plataformas["rectangulo"], 3)
            
            for rectangulos in self.colisiones_rect_direccion_enemigo:
                pygame.draw.rect(self.pantalla, "yellow", rectangulos, 3)
                
            for trampa in self.trampas:
                pygame.draw.rect(self.pantalla, "black", trampa["rectangulo"], 3)