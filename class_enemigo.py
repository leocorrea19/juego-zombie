from configuraciones import *

class Enemigo:
    def __init__(self, animaciones:dict, pos_x:int, pos_y:int, tamaño:tuple[int, int], accion):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.rectangulo_enemigo = pygame.Rect(pos_x, pos_y, *tamaño)
        self.rectangulo_enemigo.x = pos_x
        self.rectangulo_enemigo.y = pos_y
        self.contador_pasos_enemigo = 0
        self.esta_muerto = False
        self.esta_mueriendo = False
        self.accion = accion
        self.animacion_actual_enemigo = self.animaciones[self.accion]
        self.flag_colision = False
        
    def animar(self, screen):
        largo = len(self.animacion_actual_enemigo)
        if self.contador_pasos_enemigo >= largo:
            self.contador_pasos_enemigo = 0
        
        screen.blit(self.animacion_actual_enemigo[self.contador_pasos_enemigo], self.rectangulo_enemigo)
        self.contador_pasos_enemigo += 1
        
        if self.esta_mueriendo and self.contador_pasos_enemigo == largo:
            self.esta_muerto = True
    
    def avanzar(self):
        if self.accion == "izquierda":
            self.rectangulo_enemigo.x -= 3
        
        else:
            self.rectangulo_enemigo.x += 3
        
    def actualizar(self, screen):
        match self.accion:
            case "izquierda":    
                self.animacion_actual_enemigo = self.animaciones["izquierda"]
                self.animar(screen)
                self.avanzar()
            
            case "derecha":    
                self.animacion_actual_enemigo = self.animaciones["derecha"]
                self.animar(screen)
                self.avanzar()
            
            case "muere":
                if self.flag_colision == True:
                    self.animacion_actual_enemigo = self.animaciones["muere_i"]
                
                else:
                    self.animacion_actual_enemigo = self.animaciones["muere_d"]
                self.animar(screen)
                self.avanzar()
    
    def colision_rect_donde_camina(self, rectangulo):
        if self.rectangulo_enemigo.colliderect(rectangulo):
            if self.flag_colision == False:
                self.accion = "izquierda"
                self.flag_colision = True
                
            else:
                self.accion = "derecha"
                self.flag_colision = False
