import pygame
import sys
import Constantes

#inicializando pygame
pygame.init()

#creando ventana

ventana = pygame.display.set_mode((Constantes.ANCHO_VENTANA,Constantes.ALTO_VENTANA))
pygame.display.set_caption("Duck hunt")

#cargando imagen
fondo = pygame.image.load("sprites/nuevo.png").convert
#ajustando el tamaño de la imagen a la pantalla 
fondo = pygame.transform.scale(fondo,(Constantes.ANCHO_VENTANA,Constantes.ALTO_VENTANA))

#Bucle principal

run = True

while run == True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            
    ventana.blit(fondo, (0,0)) 
    
    #aqui se colocan los personajes
    
    pygame.display.flip()          

            
#salida de reguridad
pygame.quit()
sys.exit() 