
# Interfaz gráfica para el sintetizador


# Libreria para generar gráficos
from tkinter import *
from tkinter.font import Font
# Libreria numpy para generar los valores de la funcion seno
import numpy as np 
# Libreria para reproducir la nota
import sounddevice as sd



# Parametros: ----------------------------------------------------

# Tasa de muestreo (sampling rate)
muestreo = 44100

# Duración del sonido a generar en SEGUNDOS
duracion_s = 1.0




# Funciones: -----------------------------------------------------

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

    # FUncion para reproducir, esperar y detener el sonido
    sd.play(ondaEnteros, muestreo)
    sd.wait(duracion_s)
    sd.stop()



# Función switch para obtener el sonido cada nota Hz
def notasHz( nota ): # recibe como parametro la NOTA escogida

    switch ={ # frecuencia para cada nota
        1:  '987.7666', #B5
        2:  '932.3275', #As5
        3:  '880.0000', #A5
        4:  '830.6094', #Gs5
        5:  '783.9909', #G5
        6:  '739.9888', #Fs5
        7:  '698.4565', #F5
        8:  '659.2551', #E5
        9:  '622.2540', #Ds5
        10: '587.3295', #D5
        11: '554.3653', #Cs5
        12: '523.2511', #C5
    }
    def default(): # En caso de no recibir un valor incorrecto
        exit()

    return switch.get(nota, default) # La función regresa la frecuencia de la nota tocada
    


# Función para obtener la frecuencia y sintetizar el sonido
def tecla( nota ):
    sintetizar( float( notasHz( nota ) ) )






    
    
# Ventana: -------------------------------------------------------
ventana = Tk() # Se instancia la ventana 
ventana.geometry("1000x500") # Dimensiones
ventana.title("Sintetizador G1") # Titulo
# Marco
marco = Frame(ventana)
marco.pack()
# Texto 
titulo  = Label (ventana, text = "S I N T E T I Z A D O R  \n <- G 1 ->", font=('Arcade Interlaced', 25), fg='#ff8080') 
#estilo = Font(ventana, family=, size=25, )
titulo.pack(padx=10, pady=10) # Alinear 

# teclas del piano: .................................................................
# Margen teclas negras: .................................................................
mSuperior = Frame(ventana) # Marco superior
mSuperior.pack(side = TOP) # Alinearse abajo

# teclas negras: .................................................................
#Do#/Reb
botonCs = Button(mSuperior, padx=8, height=6, pady=8, bd=8, text="C#", bg="black", fg="white", command=lambda: tecla(11))
botonCs.pack(side = LEFT)

#espacio
espacio = Button(mSuperior, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE)
espacio.pack(side=LEFT)

#Re#/Mib
botonDs = Button(mSuperior, padx=8, height=6, pady=8, bd=8, text="D#", bg="black", fg="white", command=lambda: tecla(9))
botonDs.pack(side = LEFT)

#espacio
espacio = Button(mSuperior, state=DISABLED, height=7, width=4, padx=0, pady=0, relief=RIDGE)
espacio.pack(side=LEFT)

#Fa#/Solb
botonFs = Button(mSuperior, padx=8, height=6, pady=8, bd=8, text="F#", bg="black", fg="white", command=lambda: tecla(6))
botonFs.pack(side = LEFT)

#espacio
espacio = Button(mSuperior, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE)
espacio.pack(side=LEFT)

#Sol#/Lab
botonGs = Button(mSuperior, padx=8, height=6, pady=8, bd=8, text="G#", bg="black", fg="white", command=lambda: tecla(4))
botonGs.pack(side = LEFT)

#espacio
espacio = Button(mSuperior, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE)
espacio.pack(side=LEFT)

#La#/Sib
botonAs = Button(mSuperior, padx=8, height=6, pady=8, bd=8, text="A#", bg="black", fg="white", command=lambda: tecla(2))
botonAs.pack(side = LEFT)



# # Margen teclas blancas: .................................................................
mInferior = Frame(ventana) # Marco inferior (piano)
mInferior.pack(side = TOP) # Alinearse abajo

# teclas blancas: ...........................................................................
#Do
botonC = Button(mInferior, padx=16, height=8, pady=16, bd=8, text="C", bg="white", fg="black", command=lambda: tecla(12))
botonC.pack(side = LEFT)

#Re
botonD = Button(mInferior, padx=16, height=8, pady=16, bd=8, text="D", bg="white", fg="black", command=lambda: tecla(10))
botonD.pack(side = LEFT)

#Mi
botonE = Button(mInferior, padx=16, height=8, pady=16, bd=8, text="E", bg="white", fg="black", command=lambda: tecla(8))
botonE.pack(side = LEFT)

#Fa
botonF = Button(mInferior, padx=16, height=8, pady=16, bd=8, text="F", bg="white", fg="black", command=lambda: tecla(7))
botonF.pack(side = LEFT)

#Sol
botonG = Button(mInferior, padx=16, height=8, pady=16, bd=8, text="G", bg="white", fg="black", command=lambda: tecla(5))
botonG.pack(side = LEFT)

#La
botonA = Button(mInferior, padx=16, height=8, pady=16, bd=8, text="A", bg="white", fg="black", command=lambda: tecla(3))
botonA.pack(side = LEFT)

#Si
botonB = Button(mInferior, padx=16, height=8, pady=16, bd=8, text="B", bg="white", fg="black", command=lambda: tecla(1))
botonB.pack(side = LEFT)


# Se crea la ventana: .........................................................................
# Agregamos icono
ico = PhotoImage(file='/audio-waves.png')
ventana.iconphoto(False, ico)
ventana.mainloop() # Crear el hilo o bucle que va a recibir los eventos
