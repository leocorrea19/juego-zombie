from pygame import *
import sys
import menu_inicio 

class JugadorUsuario():
    
    def __init__(self):
        self.lineas = 0
        self.caracteres = [' ' ]
        self.fuente = font.SysFont("Arial", 25)

        self.distancia = 20
        self.pos_x = 600
        self.pos_y = 350
    
    def teclas(self, evento):
        for accion in evento:
            if accion.type == KEYDOWN:
                if accion.key == K_RETURN:
                    self.caracteres.append('')
                    self.lineas += 1
                elif accion.key == K_ESCAPE:
                    sys.exit(0)
                elif accion.key == K_BACKSPACE:
                    if self.caracteres[self.lineas] == '' and self.lineas > 0:
                        self.caracteres = self.caracteres[0:-1]
                        self.lineas -= 1
                    else:
                        self.caracteres[self.lineas] = self.caracteres[self.lineas][0:-1]
                else:
                    self.caracteres[self.lineas] = str(self.caracteres[self.lineas] + accion.unicode)
    
    def mensaje(self, superficie):
        for self.lineas in range(len(self.caracteres)):
            img_letra = self.fuente.render(self.caracteres[self.lineas], True, (255, 255, 255))
            superficie.blit(img_letra, (self.pos_x, self.pos_y + self.distancia * self.lineas))

    def imagen_ingreso(self, screen):
        imagen = image.load("juego zombie/imagenes/cartel_ingreso_nombre.png")
        imagen = screen.blit(imagen, (320,150))

    def boton_tilde(self, screen):
        imagen = image.load("juego zombie/imagenes/tilde.png")
        #imagen = screen.blit(imagen, (260, 250))
        
        rectangulo = imagen.get_rect()
        rectangulo.centerx = 560
        rectangulo.centery = 420
        screen.blit(imagen, rectangulo)
        
        # rectangulo = Rect((540, 420), (20, 20))
        # rectangulo = draw.rect(screen, (255, 255, 0), rectangulo)
        
        return rectangulo
        
    def boton_x(self, screen):
        rectangulo = Rect((720, 420), (20, 20))
        rectangulo = draw.rect(screen, (255, 255, 0), rectangulo)
        
        imagen = image.load("juego zombie/imagenes/x.png")
        imagen = screen.blit(imagen, (380, 250))
        
        return rectangulo