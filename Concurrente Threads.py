#Importa módulos para Interfaz Gráfica de usuario (tkinter)
import tkinter as tk
from tkinter import ttk
import time
import threading #hacemos import a threading
#Crea la ventana principal
main_window = tk.Tk()
main_window.title("Ejemplo")
main_window.configure(width=350, height=200)

#Función que crea y posiciona el botón "Salir"
def opcionFinalizar():
    boton = ttk.Button(main_window, text="Salir", command=main_window.destroy)
    boton.place(x=170, y=170)

#Función que crea una etiqueta (label) de texto en la posición (x,y) de la pantalla.
def createLabel(a,b):
    label = ttk.Label(text="")
    label.place(x=a,y=b)
    return label

#Función que crea una etiqueta (llamando a createLabel()) y luego anima texto dentro de la misma.
def crearAnimacion(a, b, char):
    mylabel = createLabel(a,b)
    texto=""
    retardo: float=0.25
    for i in range(0,35):
        time.sleep(retardo)
        texto += char
        mylabel.config(text = texto)
        main_window.update_idletasks()
        main_window.update()

#Eliminamos las invocaciones que había en el código original, para reemplazarlo creamos tres threads, utilizando la función Thread del módulo importado.
thread_1 = threading.Thread(target=crearAnimacion, args=(10,10, "X")) #Ponemos como target a la función que crea la animación y añadimos argumentos, en el formato a,b,char
thread_2 = threading.Thread(target=crearAnimacion, args=(10,30, "Y")) #Repetimos
thread_3 = threading.Thread(target=crearAnimacion, args=(10,50, "Z")) #Repetimos


#Le damos inicio a los hilos, esto debería permitir la concurrencia.
thread_1.start()
thread_2.start()
thread_3.start()

# Mantener las siguientes líneas siempre al final del script y en el mismo orden.
#Coloca la opcion "Salir"
opcionFinalizar()

#Bucle principal de la ventana
main_window.mainloop()