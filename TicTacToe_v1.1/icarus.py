# -*- coding: utf-8 -*-
import cv2
import numpy as np
from funciones_tres_raya import *
from funciones_robot import *
import time
#import sys
#from functools import partial

def isin_area(x,y):
    if(x>233 and x<298 and y>272 and y<340): 
        return(1)
    if(x>298 and x<366 and y>272 and y<340): 
        return(2)
    if(x>366 and x<438 and y>272 and y<340): 
        return(3)
    if(x>233 and x<298 and y>205 and y<272): 
        return(4)
    if(x>298 and x<366 and y>205 and y<272): 
        return(5)
    if(x>366 and x<438 and y>205 and y<272): 
        return(6)
    if(x>233 and x<298 and y>135 and y<205): 
        return(7)
    if(x>298 and x<366 and y>135 and y<205): 
        return(8)
    if(x>366 and x<438 and y>135 and y<205): 
        return(9)
         #   play = True    

def color_capture(cap, higher_color, lower_color, x,y):
    ret, frame = cap.read() 
    frame = cv2.resize(frame, (640, 480))
    #frame = cv2.flip(frame, 1)
    if ret==True: # Si hay imagen de cámara
        # Utilizamos el formato HSV (Hue, Saturation, Value) porque esta diseñado para separar la iluminación de la imagen
        # de la información del color. Esto facilita el trabajo cuando necesitamos la iluminación de la imagen
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convertir de RGB a HSV
        mask = cv2.inRange(frame_hsv, lower_color, higher_color) #Crear la mascara con el rango de colores en el marco
        #Descomente la siguiente linea en caso de que use portatil y comente la siguiente.
        #_,contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Identificar el verde / Contornos azules
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Identificar el verde / Contornos azules 
        encontrados=[]
        for c in contours: # Ubicando los puntos del contorno
            area = cv2.contourArea(c) #Identificando el area del contorno
            if area > 1000 and area<2000: 
                M = cv2.moments(c)
                if (M["m00"] == 0): M["m00"]=1
                x = int(M["m10"]/M["m00"]) #Getting the x coordinate
                y = int((M["m01"] / M["m00"])) 
                cv2.circle(frame, (x,y), 7, (0,255,0), -1) 
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, '{},{}'.format(x,y),(x+50,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)#Mostrar ubicación en la pantalla
                pos=isin_area(x, y)
                if not(pos in encontrados): encontrados.append(pos)               
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3) #Dibujar el contorno
        res = cv2.bitwise_and(frame,frame, mask= mask) # muestra la imagen del color detectado
        cv2.imshow('frame',frame) # Displaying the frame with the contours and the coordinates
        #cv2.imshow('mask',mask) # Muestra la imagen binarizada
        #cv2.imshow('res',res)
    return x, y, res,encontrados

def salir(ventana):
    ventana.destroy()
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

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

amarilloBajo = np.array([15,100,20],np.uint8)
amarilloAlto = np.array([45,255,255],np.uint8)

rojoBajo1 = np.array([0,100,20],np.uint8)
rojoAlto1 = np.array([5,255,255],np.uint8)

rojoBajo2 = np.array([175,100,20],np.uint8)
rojoAlto2 = np.array([179,255,255],np.uint8)

#--------------------------------------------------------------------------
#------- 1. Creación entorno del juego: aqui iniciamos las pantallas, -----
#------- titulos y tamaños para el funcionamiento del videojuego ----------
#--------------------------------------------------------------------------


# 1.1 Inicializar cámara
cap = cv2.VideoCapture(0)   
print(cap.get(3), cap.get(4))

#--------------------------------------------------------------------------
#-------2. Correr el juego ------------------------------------------------
#--------------------------------------------------------------------------



playerLetter='X'
computerLetter='O'
run = True
while run:
    """ Main Program """
    # 2.1. Cargar condiciones.
    auto=input('Juego automatico? (yes or no)')
    done = False
    theBoard = [' '] * 10
    turn='player'
    counter=0
    counterR=0
    azules=[0]
    #rojas=[0]
    # 2.3 Jugar
    while not done:       
        #--------------------------------------------------------------------------
        #-------2.3.1. Validación de Jugador---------------------------------------
        #-------------------------------------------------------------------------- 

        # Lee la posicion del color a mostrar
        blue_validation_x, blue_validation_y, azul,fichasA = color_capture(cap, azulAlto, azulBajo, 0,0)
        cv2.imshow('res', azul)
        print(fichasA)
        #red1_validation_x, red1_validation_y, rojo1,fichasB = color_capture(cap, rojoAlto1, rojoBajo1, 0,0)
        #cv2.imshow('Rojo 1', rojo1)
        #print(fichasB)
        time.sleep(1)
        #red2_validation_x, red2_validation_y, rojo2 = color_capture(cap, rojoAlto2, rojoBajo2, 0,0)# Detectando el objeto verde
        #cv2.imshow('Rojo 2', rojo2)
        #rojo=rojo1+rojo2
        #cv2.imshow('Rojo 1', rojo)
        ret, frame = cap.read() 
        frame = cv2.resize(frame, (640, 480))
        frame = cv2.rectangle(frame, (233,135), (298,205), (0,255,0), 2)#7
        frame = cv2.rectangle(frame, (366,135), (438,205), (0,255,0), 2)#9
        frame = cv2.rectangle(frame, (298,205), (366,272), (0,255,0), 2)#5
        frame = cv2.rectangle(frame, (233,272), (298,340), (0,255,0), 2)#1
        frame = cv2.rectangle(frame, (366,272), (438,340), (0,255,0), 2)#3
        cv2.imshow('Rectangulo',frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        
        if turn == 'player':#Azules
            
#             # Player's turn.
#             drawBoard(theBoard)
#             move = getPlayerMove(theBoard)
#             makeMove(theBoard, playerLetter, move)
            for i in fichasA:
                if i==0 or i==None:
                    theBoard=theBoard
                elif i in azules:
                    theBoard=theBoard
                else:
                    move=i
                    azules.append(i)
                    print(azules)
                    makeMove(theBoard, playerLetter, move)
                    print(theBoard)
                    counter = counter + 1
                    if isWinner(theBoard, playerLetter):
                         drawBoard(theBoard)
                         print('Hooray! You have won the game!')
                         done = True
                         break
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        done = True
                        break
                    else:
                        turn = 'computer'
        if turn=='computer':
            # Computer's turn.
             if auto=='yes':
                move = getComputerMove(theBoard, computerLetter, counter)            
             else:
                move =int(input('Ingrese movimiento: '))
             makeMove(theBoard, computerLetter, move)
             RobotMove(move,counterR)
             counterR+=1
             counter=counter+1
             print(theBoard)
             drawBoard(theBoard)
             if isWinner(theBoard, computerLetter):
                 drawBoard(theBoard)
                 print('The computer has beaten you! You lose.')
                 done = True
                 break
             if isBoardFull(theBoard):
                 drawBoard(theBoard)
                 print('The game is a tie!')
                 done = True
                 break
             else:
                 turn = 'player'
    if not playAgain():
        break
#2.4 Cierra del juego y sus ventanas.
# pygame.quit()
cap.release()
cv2.destroyAllWindows()