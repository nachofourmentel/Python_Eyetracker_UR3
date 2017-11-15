# Experimento de analisis de la gestualidad del ojo humano en relacion a un robot industrial colaborativo. 
# Ignacio Fourmentel, Universidad Nacional de Tres de Febrero.
# contact: ignacio.fourmentel@gmail.com
# ULTIMA  Version 8 de Noviembre 2017

import os.path

#DEFINICION DE DIRECTORIOS
#DIR contiene el path del directorio donde estan todos los archivos.
DIR = os.path.dirname(__file__)
#Directorio de archivos de DATA
DATADIR = os.path.join(DIR, 'data')
#IMGDIR directorio de archivos de imagenees
IMGDIR = os.path.join(DIR, 'images/track')
# INSTFILE archivo de instrucciones.
INSTFILE = os.path.join(DIR, 'instructions.txt')
# NOMBRE DE ARCHIVO = NOMBRE DE PARTICIPANTE.
LOGFILENAME = "Pruebas" #input("Nombre del sujeto:  ") 
# Crea el archivo de log con ese nombre.
LOGFILE = os.path.join(DATADIR, LOGFILENAME)

#DISPLAY
#Display 'pygame' o 'psychopy'; 
#psychopy tiene mejor resolucion de tiempo en ms, pygame usa menos recursos.
DISPTYPE = 'psychopy'

#Resolucion  LABO (1366,768) BENQ (1080,1920) PORTRAIT
DISPSIZE = (1024,768)

#Tamano fisico de la pantalla. Centimetros.
SCREENSIZE = (532.0,299.0)

#Distancia en cm entre pantalla y el sujeto experimental.
#SCREENDIST = 60.0

#FULLSCREEN
FULLSCREEN = False

#COLORES background y foreground. RGB.
BGC = (0,0,0)
FGC = (255,255,255)

#Tamano de texto.
TEXTSIZE = 24

#VARIABLES DE TIEMPO
#Tiempo por imagen
TRIALTIME = 5 # segundos
#Tiempo entre imagenes. intervalo
ITI = 2000 # ms

#EYE TRACKING
#Tipo de eyetracker. 'eyelink' 'dummy'
TRACKERTYPE = 'dummy'
#Beep durante calibracion.
EYELINKCALBEEP = True
#Dummymode cuando no hay eyetracker conectado
DUMMYMODE = True

#SETUP HOST
#IP y Puerto de la PC HOST donde se corre el experimento.
HOST = '192.168.0.5'
PORT = 30000

#Datos de pantalla
#Datos del display del eyetracker.

#Pantalla del labo
X_pantalla_mm = 405.0
Y_pantalla_mm = 230.0

#Pantalla BENQ
X_pantalla_mm = 299.0
Y_pantalla_mm = 532.0

#Datos de Hoja A4
X_a4_mm = 210.0
Y_a4_mm = 245.0

#Datos de Hoja A3
X_a3_mm = 297.0
Y_a3_mm = 420.0