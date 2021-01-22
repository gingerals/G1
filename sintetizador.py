# Librerias: -----------------------------------------------

# Libreria numpy para generar los valores de la funcion seno
import numpy as np 
# Libreria para reproducir la nota
import sounddevice as sd


# Parametros: ----------------------------------------------

# Tasa de muestreo (sampling rate)
muestreo = 44100

# Duración del sonido a generar en SEGUNDOS
duracion_s = 5.0



# Funciones: ------------------------------------------------

# Instrucciones: 
def instrucciones():
    print ("Ingrese que nota quiere tocar")
    print ("1.   B4 ")
    print ("2.   As4")
    print ("3.   A4 ")
    print ("4.   Gs4")
    print ("5.   G4 ")
    print ("6.   Fs4")
    print ("7.   F4 ")
    print ("8.   E4 ")
    print ("9.   Ds4")
    print ("10.   D4 ")
    print ("11.   Cs4")
    print ("12.   C4 ")
    print ("-Presione 0 para salir-")



# Función switch para obtener el sonido cada nota Hz
def notasHz():

    seleccion = int(input('Selección: ')) # Seleccion


    switch ={ # frecuencia para cada nota
        1: '493.883',
        2: '466.164',
        3: '440.000',
        4: '415.305',
        5: '391.995',
        6: '369.994',
        7: '349.228',
        8: '329.628',
        9: '311.127',
        10: '293.665',
        11: '277.183',
        12: '261.626'
    }

    def default(): #
        exit()

    return switch.get(seleccion, default)


# Metodo para crear la onda dado determinada frecuencia y duración
def sintetizar( frecHz ):
 
    # La función ARANGE regresa valores separados uniformemente en un cierto intervalo
    # por lo que para obtener las muestras totales y sus valores de 5 segundos es bastante util
    muestras = np.arange(duracion_s * muestreo) 

    # La funcion SIN retorna el seno de cada X dado, al ingresar un arreglo de muestras multiplicado por 
    # el valor de un ciclo completo y la frecuencia nos regresara las cordenadas de todos los puntos y de cada muestra
    onda = np.sin(2 * np.pi * muestras * frecHz / muestreo)

    # Se tiene que atenuar la onda ya que los valores en y ocupan toda la profundidad del bit rate o 
    # la amplitud, es decir el volumen máximo
    ondaTenue = onda * 0.3

    # Obtenemos los valores en enteros validos para el formato de audio estándard
    ondaEnteros = np.int16(ondaTenue * 32767)

    sd.play(ondaEnteros, muestreo)
    sd.wait(duracion_s)
    sd.stop()



# Loop:-----------------------------------------------------

# se repetira hasta que el usuario ingrese algun valor no valido
loop = 1
while loop != 0 :

    instrucciones()

    sintetizar( float( notasHz() ) )