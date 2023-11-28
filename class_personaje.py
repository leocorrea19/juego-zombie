from configuraciones import *
from class_enemigo import *

class Personaje:
    def __init__(self, animaciones:dict, pos_x:int, pos_y:int, tamaño:tuple[int, int], veolocidad:int, accion:str):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.rectangulo = pygame.Rect(pos_x, pos_y, *tamaño)
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.velocidad = veolocidad
        self.accion = accion
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones[self.accion]
        
        self.gravedad = 1
        self.desplazamiento_y = 0
        self.potencia_salto = -18
        self.limite_velocidad_salto = 18
        self.estado_salto = False
        
        self.estado_donde_mira = True
        
        self.vidas = 5
        self.esta_muriendo = False
            
    def aplicar_gravedad(self, screen, lista_plataformas):
        if self.estado_salto:
            self.animar(screen)
            self.rectangulo.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
            
        for plataformas in lista_plataformas:
            if self.rectangulo.colliderect(plataformas["rectangulo"]):
                self.estado_salto = False
                self.desplazamiento_y = 0
                self.rectangulo.bottom = plataformas["rectangulo"].top
                break
            else:
                self.estado_salto = True
        
        
    def desplazar(self):
        velocidad_actual = self.velocidad
        
        if self.accion == "muere":
            self.rectangulo.y = 5
            
        elif self.accion == "izquierda":
            velocidad_actual *= -1
            
        self.rectangulo.x += velocidad_actual
        
        
    def animar(self, screen):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        screen.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        
        self.contador_pasos += 1
        
        if self.esta_muriendo and self.contador_pasos == largo:
            self.estado_muerto = True
    
    def actualizar(self, screen, piso):
        match self.accion:
            case "derecha":
                if not self.estado_salto:
                    self.animacion_actual = self.animaciones["derecha"]
                    self.animar(screen)
                self.desplazar()
            
            case "quieto":
                if not self.estado_salto:
                    if self.estado_donde_mira == True:
                        self.animacion_actual = self.animaciones["quieto"]
                    
                    else:
                        self.animacion_actual = self.animaciones["quieto_i"]
                    self.animar(screen)
            
            case "izquierda":
                if not self.estado_salto:
                    self.animacion_actual = self.animaciones["izquierda"]
                    self.animar(screen)
                self.desplazar()
            
            case "salta":
                if not self.estado_salto:
                    self.estado_salto = True
                    self.desplazamiento_y = self.potencia_salto
                    if self.estado_donde_mira == True:
                        self.animacion_actual = self.animaciones["salta_d"]
                    
                    else:
                        self.animacion_actual = self.animaciones["salta_i"]
            
            case "muere":
                if not self.estado_salto:
                    if self.estado_donde_mira == True:
                        self.animacion_actual = self.animaciones["muere_d"]
                    else:
                        self.animacion_actual = self.animaciones["muere_i"]
                    self.animar(screen)                    
                    
        self.aplicar_gravedad(screen, piso)
    
    def verificar_colision_enemigo(self, enemigo:Enemigo):
        if self.rectangulo.colliderect(enemigo.rectangulo_enemigo):
            self.accion = "muere"
            self.esta_muriendo = True
            self.vidas -= 1
            self.rectangulo.x -= 150          
            self.rectangulo.y -= 100
            #self.animacion_actual = self.animaciones["muere_i"]
            print(self.vidas)