from pygame import *

def menu_principal(screen:str):
    """
    Crea el fondo de la ventana con una imagen
    
    Recibe un str con los datos de la ventana
    
    Devuelve la ventana con la imagen
    """
    fondo_menu = image.load("juego zombie/imagenes/fondo_menu.png")    
    fondo_menu = screen.blit(fondo_menu, (0, 0))
    
    return fondo_menu

def boton_iniciar_juego(screen:str):
    rectangulo_inicio = Rect((505, 205), (265, 55))
    rectangulo_inicio = draw.rect(screen, (255, 255, 0), rectangulo_inicio)
    
    imagen_boton = image.load("juego zombie/imagenes/botones-menu-juego.png")
    imagen_boton = transform.scale(imagen_boton, (275, 65))
    imagen_boton = screen.blit(imagen_boton, (500, 200))
    
    inicio_boton = font.SysFont("aniMe Matrix - MB_EN", 28)
    inicio_txt = inicio_boton.render("Iniciar juego", True, (255, 255, 255))
    inicio_txt = screen.blit(inicio_txt, (510, 215))
    
    return rectangulo_inicio
    
def boton_score(screen:str):
    rectangulo_score = Rect((505, 305), (265, 55))
    rectangulo_score = draw.rect(screen, (255, 255, 0), rectangulo_score)

    imagen_boton = image.load("juego zombie/imagenes/botones-menu-juego.png")
    imagen_boton = transform.scale(imagen_boton, (275, 65))
    imagen_boton = screen.blit(imagen_boton, (500, 300))
    
    score_boton = font.SysFont("aniMe Matrix - MB_EN", 40)
    score_txt = score_boton.render("Score", True, (255, 255, 255))
    score_txt = screen.blit(score_txt, (545, 310))
    
    return rectangulo_score
    
def boton_salir(screen:str):
    rectangulo_salir = Rect((505, 405), (265, 55))
    rectangulo_salir = draw.rect(screen, (255, 255, 0), rectangulo_salir)

    imagen_boton = image.load("juego zombie/imagenes/botones-menu-juego.png")
    imagen_boton = transform.scale(imagen_boton, (275, 65))
    imagen_boton = screen.blit(imagen_boton, (500, 400))
    
    score_salir = font.SysFont("aniMe Matrix - MB_EN", 40)
    salir_txt = score_salir.render("Salir", True, (255, 255, 255))
    salir_txt = screen.blit(salir_txt, (560, 410))
    
    return rectangulo_salir

def boton_sonido(screen:str, tipo_flag:str):
    circulo_sonido = draw.circle(screen, (0, 0, 25), (1200, 680), 40)

    if tipo_flag == True:
        sonido_imagen = image.load("juego zombie/imagenes/sonido_activado.png")
        sonido_imagen = transform.scale(sonido_imagen, (80, 80))
        sonido_imagen = screen.blit(sonido_imagen, (1160, 640))
    
    else:
        sonido_imagen = image.load("juego zombie/imagenes/sonido_desactivado.png")
        sonido_imagen = transform.scale(sonido_imagen, (80, 80))
        sonido_imagen = screen.blit(sonido_imagen, (1160, 640))
    
    return circulo_sonido

