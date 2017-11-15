############################################################################
# Programa de Python para enviar posiciones X-Y del eyetracker al PolyScope.

import socket
import time
import os

from pygaze.defaults import *
from constants import *

from pygaze.display import Display
from pygaze.screen import Screen
from pygaze.eyetracker import EyeTracker
from pygaze.keyboard import Keyboard
from pygaze.time import Time
from pygaze.logfile import Logfile


# # # # #
# directory stuff

DIR = os.path.split(os.path.abspath(__file__))[0]
imagefile = os.path.join(DIR, 'landscape.jpg')
# # # # #
#Instancias
#El eyetracker crea un SERVIDOR, al cual el robot debe conectarse como cliente.
#Por lo tanto, esta IP HOST, es la que debe ser ingresada en el POLYSCOPE.
#TCP
HOST = '192.168.10.103'     
PORT = 30000             

# Display
disp = Display() 
# Pantalla
scr = Screen()

#Iniciar eyetracker en el display.
tracker = EyeTracker(disp)

# Habilitar un teclado
kb = Keyboard(keylist=['space'],timeout=None)

# timer.
timer = Time()

# Logfile  # SIN USO PO AHORA #

#log = Logfile(filename="Resultados")
#log.write(["Tipo de Prueba", "Tiempo", "Dato"])


# # # # # Textos en pantalla.
# Texto de bienvenida
scr.draw_text("Experimento de Eye Tracking. Las posiciones en X e Y del ojo respecto a la pantalla, son enviadas en tiempo real via TCP al robot UR 3")
disp.fill(scr)
t1 = disp.show()
#log.write(["Bienvenido", t1])
kb.get_key()
# # # # #
# Comenzar experimento
scr.clear()
scr.draw_text("Cuando este listo para comenzar, aprete Espacio")
disp.fill(scr)
t1 = disp.show()
#log.write(["EyeTracker", t1])
kb.get_key()

# Calibracion

tracker.calibrate()

# Obtener muestras del ET   eyetracker.sample()
scr.clear()
#tracker.log("Comenzando el sampleo")

tracker.status_msg("Sampleando...")
tracker.start_recording()

key = None

while not key == 'space':
    # listen de una tecla
    key, presstime = kb.get_key(timeout=1)
    # Obtener posiciones XY
    gazepos = tracker.sample()
    gazeposSTR = str(gazepos)
    gazeposSTRX = gazepos[0]
    gazeposSTRY = gazepos[1]
 
    PosX = (gazeposSTRX / 1000)
    PosY = (gazeposSTRY / 1000)

    PosFinalTuple = (PosX,PosY)
    PosFinalSTR = str(PosFinalTuple)			
    scr.clear()
				
    #Carga una imagen
    scr.draw_image(imagefile)
    disp.fill(scr)
    disp.show()
    	
				
    """# Texto lorem ipsum
    scr.clear()
    scr.draw_text("Lorem Ipsum \n\nLorem ipsum dolor sit amet, consectetur adipiscing elit \
 Suspendisse vulputate sodales ipsum, sed suscipit ex elementum ac. urabitur ornare, enim ac consectetur venenatis. \nSed eu orci facilisis, tristique erat eget, elementum massa \
\n Nulla pretium, augue vitae interdum euismod, nulla lectus venenatis nisi, vel euismod justo ante non turpis\
\n Proin sagittis bibendum eros, ac aliquam arcu ultricies in. Nulla pharetra consectetur malesuada.\
\n Nulla ac molestie lorem. Nam tincidunt nunc at lobortis pretium. Nulla sed ultrices lorem.\
\n\n\n- Presiona Espacio Para finalizar\
\n- El circulo negro representa el punto donde se posa la mirada \
\n- Frenara el sample cada vez que el robot solicite la informacion. \
\n")"""


    #Dibuja fijacion.
    scr.draw_fixation(fixtype='dot', pos=gazepos, pw=5, diameter=15)
    disp.fill(scr)
    disp.show()
	

    
    #conteo para el while.     
    count = 0    
    while (count < 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #definir el socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #lo mismo
        
        s.bind((HOST, PORT))                  
        s.listen(0.5)                     	# Esperando conexion. Originalmente estaba en 5
        c, addr = s.accept()                	# Aceptar conexion
    
        try: 
             msg = c.recv(1024)            #recibir mensajes
             #time.sleep(0.001) 				#0.001
             if msg == "Esperando_Waypoin t":  
                            
                    c.send(PosFinalSTR);    #enviar la posicion en string   
                    count = count + 1 
                                        
        except socket.error as socketerror:
									print count  #Volarlo"""     
									 
										
										
    
  
tracker.stop_recording()  #finalizar el et
scr.clear()

# # # #
#Cierre de experimento
# ending screen
scr.clear()
scr.draw_text("Finalizado. Espacio para salir.")
disp.fill(scr)
t1 = disp.show()
#log.write(["ending", t1])
kb.get_key()

# close
#log.close()
tracker.close()
disp.close()
timer.expend()