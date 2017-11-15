# Experimento de analisis de la gestualidad del ojo humano en relacion a un robot industrial colaborativo. 
# Ignacio Fourmentel, Universidad Nacional de Tres de Febrero.
# contact: ignacio.fourmentel@gmail.com
# ULTIMA  Version 8 de Noviembre 2017

import os
import socket
import time

from constants import *

from pygaze.libscreen import Display, Screen
from pygaze.libinput import Keyboard
from pygaze.eyetracker import EyeTracker
from pygaze.liblog import Logfile
import pygaze.libtime as timer

# # # # #
# SETUP
# visuals
disp = Display()
scr = Screen()

# input
kb = Keyboard() 
kb = Keyboard(keylist=['space'],timeout=None)
tracker = EyeTracker(disp)

# outputmeout=None)  
#log = Logfile()
#log.write(["NumeroDePrueba","Imagen","TiempoDeImagen"])

# # # # # 
# Preparacion del expermiento  
# Cargamos las instrucciones desde un archivo. 
instfile = open(INSTFILE)
instructions = instfile.read()
instfile.close()

# Leemos el directorio de las imagenes.
images = os.listdir(IMGDIR)

# Instrucciones.
scr.draw_text(text="Presiona cualquier tecla para comenzar la calibracion.", fontsize=TEXTSIZE)
disp.fill(scr)
disp.show()

# Esperamos la tecla.
kb.get_key(keylist=None, timeout=None, flush=True)

# Etapa de Calibracion
tracker.calibrate()

# # # # # # #  # # # # # #
# Comienza el experimento.
# Display de instrucciones.
scr.clear()
scr.draw_text(text=instructions, fontsize=TEXTSIZE)
disp.fill(scr)
disp.show()

# Esperamos tecla puede ser CUALQUIERA
kb.get_key(keylist=None, timeout=None, flush=True)

# drift check  se puede sacar a posteiori. 
tracker.drift_correction()
	


#Variables para controlar los trials
key = None
trialnr = 0
count = 0
vueltas = 0

# CORRE EL  TRIAL
# Comenzamos el recording

# Definimos el logeo.
#tracker.log("TRIAL NRO %d" % trialnr) 
#tracker.log("NOMBRE DE IMAGEN %s" % images[trialnr])
#tracker.status_msg("Trial.. %d/%d" % (trialnr+1, ntrials))

#SETEO EL TIEMPO DEL EXPERIMENTO
#timepo transcurrido desde que se llama la variable start
start = time.time()
time.clock()
elapsed = 0

# PREPARAMOS IMAGENES
#ELEGIMOS LAS IMAGENES
Imagenes = [2,4,2]
# Numero de TRIALS en funcion de cantidad de imagenes.
ntrials = len(Imagenes)
#PUNTERO QUE RECORRE LA LISTA
X = 0

while elapsed < TRIALTIME and not key == 'space':
	
	#tracker.start_recording()	
	key, presstime = kb.get_key(timeout=1)
	
	#Cargamos archivos	
	Carga = Imagenes[X]	
	# presentamos imagen.
	scr.clear()
	scr.draw_image(os.path.join(IMGDIR,images[Carga]))
	disp.show()
	
	#SAMPLES
	gazepos = tracker.sample()
	# Presentamos fijaciones
	scr.draw_fixation(fixtype='dot', pos=gazepos, pw=5, diameter=15)
    	disp.fill(scr)
	gazeposSTR = str(gazepos)
	
	gazeposX = gazepos[0]
	gazeposY = gazepos[1]
 
	FactorX = (X_a4_mm / X_pantalla_mm)
	FactorY = (Y_a4_mm / Y_pantalla_mm)
	
	PX_mm_X = (X_pantalla_mm / DISPSIZE[0])
	PX_mm_Y = (Y_pantalla_mm / DISPSIZE[1])
	
	#CUENTA FINAL	
	PosX = (PX_mm_X * (gazeposX * FactorX))
	PosY = (PX_mm_Y * (gazeposY * FactorY))
	
	# ??
	PosFinalTuple = (PosX/1000,PosY/1000)
	
	PosFinalSTR = str(PosFinalTuple)
	print PosFinalSTR
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  		 #definir el socket
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 		 #lo mismo
	s.bind((HOST, PORT))                  
	s.listen(1)                     						# Cuantas conexiones puede dejar en espera.
	c, addr = s.accept()                					# Aceptar conexion
		   	
	msg = c.recv(1024)            						# Buffer recibir mensajes 1024
	time.sleep(0.001) 								#0.001
	if msg == "Esperando_Waypoint":	                            
		              c.send(PosFinalSTR);   		 		#ENVIO la posicion en string	              																					
	
	elapsed = time.time() - start
	
	if elapsed >= TRIALTIME:	
		X = X + 1
		TRIALTIME = TRIALTIME + 10
		timer.pause(ITI)

	if X == ntrials:
			break
		
# Limpiamos el screen
disp.fill()
t1 = disp.show()
#tracker.log("image offline at %d" % t1)

# Frenamos el recording del eyetracker.
#tracker.stop_recording()
	
# FIN TRIAL
# logeo..
#log.write([trialnr, images[trialnr])

# # # # #
# CIERRE
# MENSAJE..
scr.clear()
scr.draw_text(text="Gracias por participar.", fontsize=TEXTSIZE)
disp.fill(scr)
disp.show()
timer.pause(1000)
scr.clear()
scr.draw_text(text="Transfiriendo data files... Espere.", fontsize=TEXTSIZE)
disp.fill(scr)
disp.show()
timer.pause(1)

# cerramos conexion con el tracker
# enviamos los datos a la pc.
tracker.close()

# cerramos el log.
log.close()

# Mensaje de salida.
scr.clear()
scr.draw_text(text="Este es el final de el experimento. Gracias por participar! !\n\n(Presione cualquier tecla para salir)", fontsize=TEXTSIZE)
disp.fill(scr)
disp.show()

# Esperamos tecla..
kb.get_key(keylist=None, timeout=None, flush=True)

# Cierra display
disp.close()
