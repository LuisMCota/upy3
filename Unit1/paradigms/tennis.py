import pygame
from random import randint

pygame.init() #area de jeugo

cancha = pygame.display.set_mode((640,480)) #estableciendo el tamaño de la ventana (display)
pygame.display.set_caption("Partido 1") #concepto del juegp

#creamos la pelota usando una imagen png
pelota = pygame.image.load("pelotita.png") #la pelota la creamos en AI y exportamos como PNG
pelotarect = pelota.get_rect()
valocidad = [randint(3,6),randint(3,6)] #valores del movimiento 
pelotarect.move_ip(0,0) #posicionando la pelota en el origen(donde iniciara el juego)

#raqueta
raquet = pygame.image.load("raqueta.png") #llamamos a la raqueta igual que la eplota usando png
raquetrect = raquet.get_rect()
raquetrect.move_ip(240,450) #posicionando la raqueta en la parte inferior d ela cancha

fuente = pygame.font.Font(None, 36)

jugando = True #bucle principal del juego
while jugando:
    for event in pygame.event.get(): #obteniendo los eventos posibles
        if event.type == pygame.QUIT: #saber si el evento ya es el fin y cerrar el primer concepto
            jugando = False #ya no hay posibles eventos

    #iterqaciones con las teclas para empezar el juego
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]: #lo que el usurario moverá será la raqueta
        raquetrect = raquetrect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        raquetrect = raquetrect.move(3,0)
    if raquetrect.colliderect(pelotarect): #iterando si hay contacto de la pelota y raqueta
        valocidad[1] = -valocidad[1]

    pelotarect = pelotarect.move(valocidad) #movivmiento de la pelota de acuerdo a la velocidad acordada
    #Empiezas las iteraciones de si la pelota toca los bordes de la ventana (cancha)
    if pelotarect.left < 0 or pelotarect.right > cancha.get_width():
        valocidad[0] = -valocidad[0]
            
    if pelotarect.top < 0:
        valocidad[1] = -valocidad[1]

    if pelotarect.bottom > cancha.get_height():
        texto = fuente.render("Pediste, looser!", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = cancha.get_width() / 2 - texto_rect.width / 2
        texto_y = cancha.get_height() / 2 - texto_rect.height / 2
        cancha.blit(texto, [texto_x, texto_y]) 

    else:
        cancha.fill((0, 30, 120)) #estableciendo el color de nuestra cancha (azulmarino)
        cancha.blit(pelota, pelotarect) #definimos la pelotra en la pantalla
        cancha.blit(raquet, raquetrect)
    
    pygame.display.flip() #actuliza el contenido en la pantalla
    pygame.time.Clock().tick(60) #tiempo de interacción

pygame.quit() #saber si el evento ya es el fin y cerrar el primer concepto

