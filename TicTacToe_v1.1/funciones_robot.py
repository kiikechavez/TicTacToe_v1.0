# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:00:42 2022

@author: USUARIO
"""

import serial
#from serial import serial
import struct
import time
import os
import binascii

cmd_str_10 = [ 0 for i in range(10) ]
cmd_str_42 = [ '\x00' for i in range(42) ]
ser = serial.Serial(#serial connection
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,#serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,#serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS#serial.SEVENBITS
)
#ser.close()
ser.isOpen()

# Open Serial port will reset dobot, wait seconds
print ("Wait 3 seconds...")
time.sleep(3) 

def dobot_cmd_send( cmd_str_10 ):
    global cmd_str_42
    cmd_str_42 = [ '\x00' for i in range(42) ]
    cmd_str_42[0]  = '\xA5'
    cmd_str_42[41] = '\x5A'
    for i in range(10):
        str4 = struct.pack( '<f', float(cmd_str_10[i]) )
        cmd_str_42[4*i+1] = hex(str4[0])[2:].rjust(2,'0')
        cmd_str_42[4*i+2] = hex(str4[1])[2:].rjust(2,'0')
        cmd_str_42[4*i+3] = hex(str4[2])[2:].rjust(2,'0')
        cmd_str_42[4*i+4] = hex(str4[3])[2:].rjust(2,'0')
    cmd_str = str(cmd_str_42).replace("'","").replace(",","")[2:-2]
    cmd_str1 = bytes.fromhex(cmd_str)
    time.sleep(0.5)
    print(cmd_str1)
    msg=b'\xA5'
    msg1=b'\x5A'    
    time.sleep( 0.5 )
    ser.write(msg+cmd_str1+msg1)


#state 3
def dobot_cmd_send_3( x = 265, y = 0, z = -30,cap=0 ):
    global cmd_str_10
    cmd_str_10 = [ 0 for i in range(10) ]
    cmd_str_10[0] = 3
    cmd_str_10[2] = x
    cmd_str_10[3] = y
    cmd_str_10[4] = z
    cmd_str_10[6] = cap
    cmd_str_10[7] = 2 # MOVL
    dobot_cmd_send( cmd_str_10 )

def dobot_cmd_send_9():
    global cmd_str_10
    cmd_str_10 = [ 0 for i in range(10) ]
    cmd_str_10[0] = 9
    cmd_str_10[1] = 1
    cmd_str_10[2] = 200 #JointVel
    cmd_str_10[3] = 200 #JointAcc
    cmd_str_10[4] = 200 #ServoVel
    cmd_str_10[5] = 200 #ServoAcc
    cmd_str_10[6] = 800 #LinearVel
    cmd_str_10[7] = 1000 #LinearAcc
    dobot_cmd_send( cmd_str_10 )

def dobot_cmd_send_10( VelRat = 100, AccRat = 100 ):
    global cmd_str_10
    cmd_str_10 = [ 0 for i in range(10) ]
    cmd_str_10[0] = 10
    cmd_str_10[2] = VelRat
    cmd_str_10[3] = AccRat
    dobot_cmd_send( cmd_str_10 )

def TicTacToeInit():
    #ser.write(bytes.fromhex('a5000010410000804000000000000000000000000000000000000000000000000000000000000000005a'))
    ser.close()
    time.sleep(1.8) 
    ser.open()
    # #ser.write(b)
    dobot_cmd_send_9() #config
    time.sleep( 0.5 )
    #dobot_cmd_send_91() #config
    #time.sleep( 0.5 )
    dobot_cmd_send_10() #config
    time.sleep( 0.5 )

#print ("Dobot Test Begin")
#b='hello'.encode('utf-8')
ser.write(bytes.fromhex('a5000010410000804000000000000000000000000000000000000000000000000000000000000000005a'))
time.sleep(1.8) 
# #ser.write(b)
dobot_cmd_send_9() #config
time.sleep( 0.5 )
#dobot_cmd_send_91() #config
#time.sleep( 0.5 )
dobot_cmd_send_10() #config
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735) #Se ubica en Home
time.sleep( 0.5 )
TicTacToeInit()
dobot_cmd_send_3( 200, 200, 58) #Se dirije a cilindro 1
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 200,-5, 1) #Recoje cilindro 1
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735, 1 ) #Vuelve a home
time.sleep( 0.5 )
dobot_cmd_send_3( 230, -65, 18) #Ubica el cilindro 1 en la posición 1
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735) #Vuelve a home
time.sleep( 0.5 )
ser.close()
time.sleep( 1.8 )
ser.open()
dobot_cmd_send_9() #config
time.sleep( 0.5 )
dobot_cmd_send_10() #config
time.sleep( 0.5 )
dobot_cmd_send_3(150, 200, 58) #Se dirije al cilindro 2
time.sleep( 0.5 )
dobot_cmd_send_3(150, 200, -5, 1) #Recoje cilindro 2
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735 ,1) #Vuelve a home
time.sleep( 0.5 )
dobot_cmd_send_3( 230, 0, 18) #Ubica el cilindro 2 en la posición 2
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735 ) #Vuelve a home
time.sleep( 0.5 )
ser.close()
time.sleep( 1.8 )
ser.open()
dobot_cmd_send_9() #config
time.sleep( 0.5 )
dobot_cmd_send_10() #config
time.sleep( 0.5 )
dobot_cmd_send_3(150, 200, 58) #Se dirije al cilindro 3
time.sleep( 0.5 )
dobot_cmd_send_3(150, 200, -5, 1) #Recoje cilindro 3
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735 ,1) #Vuelve a home
time.sleep( 0.5 )
dobot_cmd_send_3( 230, 65, 18) #Ubica el cilindro 3 en la posición 3
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735 ) #Vuelve a home
time.sleep( 0.5 )
ser.close()
time.sleep( 1.8 )
ser.open()
dobot_cmd_send_9() #config
time.sleep( 0.5 )
dobot_cmd_send_10() #config
time.sleep( 0.5 )
dobot_cmd_send_3(150, 200, 58) #Se dirije al cilindro 4
time.sleep( 0.5 )
dobot_cmd_send_3(150, 200, -5, 1) #Recoje cilindro 4
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735 ,1) #Vuelve a home
time.sleep( 0.5 )
dobot_cmd_send_3( 200, -65, 18) #Ubica el cilindro 4 en la posición 4
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735 ) #Vuelve a home
time.sleep( 0.5 )
ser.close()
'''Configurando cilindro 5 en la posición 5 '''
time.sleep( 1.8 )
ser.open()
dobot_cmd_send_9() #config
time.sleep( 0.5 )
dobot_cmd_send_10() #config
time.sleep( 0.5 )
dobot_cmd_send_3(150, 200, 58) #Se dirije al cilindro 5
time.sleep( 0.5 )
dobot_cmd_send_3(150, 200, -5, 1) #Recoje cilindro 5
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735 ,1) #Vuelve a home
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 18) #Ubica el cilindro 5 en la posición 5
time.sleep( 0.5 )
dobot_cmd_send_3( 200, 0, 58.735 ) #Vuelve a home
time.sleep( 0.5 )
ser.close()
'''Configurando cilindro 6 en la posición 6 '''
time.sleep(1.8)
ser.open()
dobot_cmd_send_9() #config
time.sleep(0.5)
dobot_cmd_send_10() #config
time.sleep(0.5)
dobot_cmd_send_3(150, 200, 58) #Se dirije al cilindro 6
time.sleep(0.5)
dobot_cmd_send_3(150, 200, -5, 1) #Recoje cilindro 6
time.sleep(0.5)
dobot_cmd_send_3( 200, 0, 58.735 ,1) #Vuelve a home
time.sleep(0.5)
dobot_cmd_send_3( 200, 65, 18) #Ubica el cilindro 6 en la posición 6
time.sleep(0.5)
dobot_cmd_send_3( 200, 0, 58.735 ) #Vuelve a home
time.sleep(0.5)
ser.close()
'''Configurando cilindro 7 en la posición 7 '''
time.sleep(1.8)
ser.open()
dobot_cmd_send_9() #config
time.sleep(0.5)
dobot_cmd_send_10() #config
time.sleep(0.5)
dobot_cmd_send_3(150, 200, 58) #Se dirije al cilindro 7
time.sleep(0.5)
dobot_cmd_send_3(150, 200, -5, 1) #Recoje cilindro 7
time.sleep(0.5)
dobot_cmd_send_3( 200, 0, 58.735 ,1) #Vuelve a home
time.sleep(0.5)
dobot_cmd_send_3( 170, -65, 18) #Ubica el cilindro 7 en la posición 7
time.sleep(0.5)
dobot_cmd_send_3( 200, 0, 58.735 ) #Vuelve a home
time.sleep(0.5)
ser.close()
'''Configurando cilindro 8 en la posición 8 '''
time.sleep(1.8)
ser.open()
dobot_cmd_send_9() #config
time.sleep(0.5)
dobot_cmd_send_10() #config
time.sleep(0.5)
dobot_cmd_send_3(150, 200, 58) #Se dirije al cilindro 8
time.sleep(0.5)
dobot_cmd_send_3(150, 200, -5, 1) #Recoje cilindro 8
time.sleep(0.5)
dobot_cmd_send_3( 200, 0, 58.735 ,1) #Vuelve a home
time.sleep(0.5)
dobot_cmd_send_3( 170, 0, 18) #Ubica el cilindro 8 en la posición 8
time.sleep(0.5)
dobot_cmd_send_3( 200, 0, 58.735 ) #Vuelve a home
time.sleep(0.5)
ser.close()
'''Configurando cilindro 9 en la posición 9 '''
time.sleep(1.8)
ser.open()
dobot_cmd_send_9() #config
time.sleep(0.5)
dobot_cmd_send_10() #config
time.sleep(0.5)
dobot_cmd_send_3(150, 200, 58) #Se dirije al cilindro 8
time.sleep(0.5)
dobot_cmd_send_3(150, 200, -5, 1) #Recoje cilindro 8
time.sleep(0.5)
dobot_cmd_send_3( 200, 0, 58.735 ,1) #Vuelve a home
time.sleep(0.5)
dobot_cmd_send_3( 170, 65, 18) #Ubica el cilindro 8 en la posición 8
time.sleep(0.5)
dobot_cmd_send_3( 200, 0, 58.735 ) #Vuelve a home
time.sleep(0.5)
ser.close()
print ("Dobot Test End")