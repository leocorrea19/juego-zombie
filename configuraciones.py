import pygame

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    
    return lista_girada

def reescalar_imagenes(diccionario_animaciones, tamaño):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            superficie = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(superficie, tamaño)

def crear_plataforma(es_visible, tamaño_x, tamaño_y, pos_x, pos_y, path="")->dict:
    plataforma =  {}
    if es_visible:
        plataforma["superficie"] = pygame.image.load(path)
        plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"], (tamaño_x, tamaño_y))
        
    else:
        plataforma["superficie"] = pygame.Surface((tamaño_x, tamaño_y))
    
    x = pos_x
    y = pos_y
    
    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y

    return plataforma

#PERSONAJE PRINCIPAL
pj_principal_quieto_d = [pygame.image.load(r"imagenes/personaje_principal/parado pj principal/parado_Pj_p.png")]

pj_principal_quieto_i = girar_imagenes(pj_principal_quieto_d, True, False)

pj_principal_caminando_d = [pygame.image.load(r"imagenes/personaje_principal/pj principal caminando/derecha/caminando_pj_p_1.png"),
                            pygame.image.load(r"imagenes/personaje_principal/pj principal caminando/derecha/caminando_pj_p_2.png"),
                            pygame.image.load(r"imagenes/personaje_principal/pj principal caminando/derecha/caminando_pj_p_3.png"),
                            pygame.image.load(r"imagenes/personaje_principal/pj principal caminando/derecha/caminando_pj_p_4.png"),
                            pygame.image.load(r"imagenes/personaje_principal/pj principal caminando/derecha/caminando_pj_p_5.png"),
                            pygame.image.load(r"imagenes/personaje_principal/pj principal caminando/derecha/caminando_pj_p_6.png"),
                            pygame.image.load(r"imagenes/personaje_principal/pj principal caminando/derecha/caminando_pj_p_7.png"),
                            pygame.image.load(r"imagenes/personaje_principal/pj principal caminando/derecha/caminando_pj_p_8.png")]

pj_principal_caminando_i = girar_imagenes(pj_principal_caminando_d, True, False)

pj_principal_salta_d = [pygame.image.load(r"imagenes/personaje_principal/salto pj principal/salto_pj_p_3.png")]

pj_principal_salta_i = girar_imagenes(pj_principal_salta_d, True, False)

pj_principal_muere_d = [pygame.image.load(r"imagenes/personaje_principal/pj principal muerte/muerte_pj_p_1.png"),
                        pygame.image.load(r"imagenes/personaje_principal/pj principal muerte/muerte_pj_p_2.png"),
                        pygame.image.load(r"imagenes/personaje_principal/pj principal muerte/muerte_pj_p_3.png"),
                        pygame.image.load(r"imagenes/personaje_principal/pj principal muerte/muerte_pj_p_4.png"),
                        pygame.image.load(r"imagenes/personaje_principal/pj principal muerte/muerte_pj_p_5.png")]

pj_principal_muere_i = girar_imagenes(pj_principal_muere_d, True, False)

#ENEMIGO 1
enemigo_1_camina_d = [pygame.image.load(r"imagenes/zombie_1/camina/0.png"), 
                    pygame.image.load(r"imagenes/zombie_1/camina/1.png"),
                    pygame.image.load(r"imagenes/zombie_1/camina/2.png"),
                    pygame.image.load(r"imagenes/zombie_1/camina/3.png"),
                    pygame.image.load(r"imagenes/zombie_1/camina/4.png"),
                    pygame.image.load(r"imagenes/zombie_1/camina/5.png"),
                    pygame.image.load(r"imagenes/zombie_1/camina/6.png"),
                    pygame.image.load(r"imagenes/zombie_1/camina/7.png"),
                    pygame.image.load(r"imagenes/zombie_1/camina/8.png")]

enemigo_1_camina_i = girar_imagenes(enemigo_1_camina_d, True, False)

enemigo_1_muere_d = [pygame.image.load(r"imagenes/zombie_1/muere/0.png"),
                pygame.image.load(r"imagenes/zombie_1/muere/1.png"),
                pygame.image.load(r"imagenes/zombie_1/muere/2.png"),
                pygame.image.load(r"imagenes/zombie_1/muere/3.png"),
                pygame.image.load(r"imagenes/zombie_1/muere/4.png"),
                pygame.image.load(r"imagenes/zombie_1/muere/5.png"),
                pygame.image.load(r"imagenes/zombie_1/muere/6.png"),
                pygame.image.load(r"imagenes/zombie_1/muere/7.png"),
                pygame.image.load(r"imagenes/zombie_1/muere/8.png")]

enemigo_1_muere_i = girar_imagenes(enemigo_1_muere_d, True, False)

