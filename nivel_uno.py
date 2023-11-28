from configuraciones import *
from class_personaje import *
from class_enemigo import *
from nivel import *


class NivelUno(Nivel):
    def __init__(self, screen:pygame.Surface):
        #PANTALLA
        ANCHO = screen.get_width()
        ALTO = screen.get_height()
        
        #FONDO 
        fondo_nivel_1 = pygame.image.load("imagenes/mapas/mapa_nivel_1.png")
        fondo_nivel_1 = pygame.transform.scale(fondo_nivel_1, (ANCHO, ALTO))

        #PERSONAJE
        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = pj_principal_quieto_d
        diccionario_animaciones["quieto_i"] = pj_principal_quieto_i
        diccionario_animaciones["derecha"] = pj_principal_caminando_d
        diccionario_animaciones["izquierda"] = pj_principal_caminando_i
        diccionario_animaciones["salta_d"] = pj_principal_salta_d
        diccionario_animaciones["salta_i"] = pj_principal_salta_i
        diccionario_animaciones["muere_d"] = pj_principal_muere_d
        diccionario_animaciones["muere_i"] = pj_principal_muere_i

        pj_principal = Personaje(diccionario_animaciones, 100, 600, (80, 70), 10, "quieto")
        
        lista_pj_principal = [pj_principal]
        
        #ENEMIGO 1
        diccionario_animaciones_enemigo_1 = {}
        diccionario_animaciones_enemigo_1["izquierda"] = enemigo_1_camina_i
        diccionario_animaciones_enemigo_1["derecha"] = enemigo_1_camina_d
        diccionario_animaciones_enemigo_1["muere_i"] = enemigo_1_muere_i
        diccionario_animaciones_enemigo_1["muere_d"] = enemigo_1_muere_d

        enemigo_1 = Enemigo(diccionario_animaciones_enemigo_1, 1000, 600, (80, 70), "derecha")
        enemigo_2 = Enemigo(diccionario_animaciones_enemigo_1, 150, 470, (80, 70), "derecha")
        enemigo_3 = Enemigo(diccionario_animaciones_enemigo_1, 290, 260, (80, 70), "derecha")
        enemigo_4 = Enemigo(diccionario_animaciones_enemigo_1, 850, 436, (80, 70), "derecha")
        enemigo_5 = Enemigo(diccionario_animaciones_enemigo_1, 1000, 198, (80, 70), "derecha")
        lista_enemigos = [enemigo_1, enemigo_2, enemigo_3, enemigo_4, enemigo_5]
        
        #PLATAFORMAS
        piso = crear_plataforma(False, ANCHO, 20, 0, 660)
        plataforma_1 = crear_plataforma(False, 340, 2, 103, 472)
        plataforma_2 = crear_plataforma(False, 415, 2, 188, 260)
        plataforma_3 = crear_plataforma(False, 365, 2, 762, 436)
        plataforma_4 = crear_plataforma(False, 418, 2, 832, 198)
        
        lista_plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4]
        
        #RECTANGULOS PARA LAS  COLISIONES EN PLATAFORMAS DONDE CAMINA EL ENEMIGO
        rectangulo_colision_piso_i = pygame.Rect(820, 640, 5, 25)
        rectangulo_colision_piso_d = pygame.Rect(1200, 640, 5, 25)
        rectangulo_colision_1_i = pygame.Rect(103, 460, 5, 25)
        rectangulo_colision_1_d = pygame.Rect(440, 460,  5, 25)
        rectangulo_colision_2_i = pygame.Rect(188, 240, 5, 25)
        rectangulo_colision_2_d = pygame.Rect(600, 240, 5, 25)
        rectangulo_colision_3_i = pygame.Rect(832, 180, 5, 25)
        rectangulo_colision_3_d = pygame.Rect(1242, 180, 5, 25)
        rectangulo_colision_4_i = pygame.Rect(762, 410, 5, 25)
        rectangulo_colision_4_d = pygame.Rect(1126, 410, 5, 25)
        
        
        lista_rectangulos_colision_donde_camina_enemigo = [rectangulo_colision_piso_i,
                                                            rectangulo_colision_piso_d,
                                                            rectangulo_colision_1_i, 
                                                            rectangulo_colision_1_d, 
                                                            rectangulo_colision_2_i, 
                                                            rectangulo_colision_2_d,
                                                            rectangulo_colision_3_i,
                                                            rectangulo_colision_3_d,
                                                            rectangulo_colision_4_i,
                                                            rectangulo_colision_4_d]
        
        #TRAMPAS
        trampas = crear_plataforma(True, 100, 50, 590, 620, "trampas/trampa_p.png")
        
        lista_trampas = [trampas]
        
        
        pj_principal.rectangulo.bottom = piso["rectangulo"].top
        
        enemigo_1.rectangulo_enemigo.bottom = piso["rectangulo"].top
        enemigo_2.rectangulo_enemigo.bottom = plataforma_1["rectangulo"].top
        enemigo_3.rectangulo_enemigo.bottom = plataforma_2["rectangulo"].top
        enemigo_4.rectangulo_enemigo.bottom = plataforma_3["rectangulo"].top
        enemigo_5.rectangulo_enemigo.bottom = plataforma_4["rectangulo"].top
        
        super().__init__(screen, lista_pj_principal, lista_plataformas, lista_enemigos, lista_rectangulos_colision_donde_camina_enemigo, lista_trampas, fondo_nivel_1)