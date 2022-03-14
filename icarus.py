import cv2
import numpy as np
import pygame
import tkinter as tk
import time
import sys
from functools import partial


def color_capture(cap, higher_color, lower_color, x,y):
    ret, frame = cap.read() 
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)
    if ret==True: # Si hay imagen de cámara
        # Utilizamos el formato HSV (Hue, Saturation, Value) porque esta diseñado para separar la iluminación de la imagen
        # de la información del color. Esto facilita el trabajo cuando necesitamos la iluminación de la imagen
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convertir de RGB a HSV
        mask = cv2.inRange(frame_hsv, lower_color, higher_color) #Crear la mascara con el rango de colores en el marco
        #Descomente la siguiente linea en caso de que use portatil y comente la siguiente.
        #_,contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Identificar el verde / Contornos azules
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Identificar el verde / Contornos azules 
        for c in contours: # Ubicando los puntos del contorno
            area = cv2.contourArea(c) #Identificando el area del contorno
            if area > 1000: 
                M = cv2.moments(c)
                if (M["m00"] == 0): M["m00"]=1
                x = int(M["m10"]/M["m00"]) #Getting the x coordinate
                y = int((M["m01"] / M["m00"])) 
                cv2.circle(frame, (x,y), 7, (0,255,0), -1) 
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)#Mostrar ubicación en la pantalla
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3) #Dibujar el contorno
        res = cv2.bitwise_and(frame,frame, mask= mask) # muestra la imagen del color detectado
        cv2.imshow('frame',frame) # Displaying the frame with the contours and the coordinates
        #cv2.imshow('mask',mask) # Muestra la imagen binarizada
        #cv2.imshow('res',res)
    return x, y

def salir(ventana):
    ventana.destroy()
    pygame.quit()
    cap.release()
    cv2.destroyAllWindows()

def salir2(ventana2):
    ventana2.destroy()


#--------------------------------------------------------------------------
#-------- 0. Iniciacion de colores y Constantes ---------------------------
#--------------------------------------------------------------------------

WHITE  = ( 255, 255, 255)
GREENL  = (181, 230,  29)
RED    = ( 255,   0,   0)

# Inicializando coordenadas
x = 0
y = 0

# Umbrales de la máscara

lower_green = np.array ([40, 40, 40],np.uint8) # Color verde minimo del rango
higher_green = np.array([70,255, 255],np.uint8) # Color verde maximo del rango

#--------------------------------------------------------------------------
#------- 1. Creación entorno del juego: aqui iniciamos las pantallas, -----
#------- titulos y tamaños para el funcionamiento del videojuego ----------
#--------------------------------------------------------------------------


# 1.1 Inicializar cámara
cap = cv2.VideoCapture(0)   
print(cap.get(3), cap.get(4))

# 1.2 Inicializar el juego con la libreria pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])# Crear una ventana con un tamaño de pantalla definido
pygame.display.set_caption('ICARUS')# titulo de la ventana

# 1.3 Creacion y llamada del jugador
player = Player(60, 233) #Posición inicial del jugador
movingsprites = pygame.sprite.Group()
movingsprites.add(player)

# 
background_position = [0, 0] # posicion del fondo de pantalla
background_image1 = pygame.image.load("Ground_1.png").convert()# Cargar imagenes

# Variable de tiempo restante
segundos_maximos = 200
timer = 0

#Estilo de fuente para Temporizador

font = pygame.font.SysFont("monospace", 24) 

#--------------------------------------------------------------------------
#-------2. Correr el juego ------------------------------------------------
#--------------------------------------------------------------------------

run = True

while run:
    """ Main Program """
    # 2.1. Cargar condiciones.
   
    done = False
    play = False # Variable de confirmación de Captura
    
    # 2.3 Jugar
    while not done:       
        #--------------------------------------------------------------------------
        #-------2.3.1. Validación de Jugador---------------------------------------
        #-------------------------------------------------------------------------- 

        # Lee la posicion del color a mostrar
        green_validation_x, green_validation_y = color_capture(cap, higher_green, lower_green, 0,0) # Detectando el objeto verde
        #Da inicio de arranque (Mi objeto debe estar en esas posiciones para iniciar)
        if(green_validation_x>55 and green_validation_x<85 and green_validation_y>80 and green_validation_y<280): play = True
        # Actualización de la posición
        if(play):
            player.rect.x = green_validation_x
            player.rect.y = green_validation_y


        #--------------------------------------------------------------------------
        #------- 2.3.2. Lógica del juego ------------------------------------------
        #--------------------------------------------------------------------------

        # Juego en marcha
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        

    break

#2.4 Cierra del juego y sus ventanas.
pygame.quit()
cap.release()
cv2.destroyAllWindows()


