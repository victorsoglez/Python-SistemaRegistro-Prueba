from tkinter import *
from tkinter import ttk
from VISTAS.navegador import Aplicacion

if __name__ == '__main__':
    ventana = Tk()
    app = Aplicacion(ventana)

    ventana.mainloop()