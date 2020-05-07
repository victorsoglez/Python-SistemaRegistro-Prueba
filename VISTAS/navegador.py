from tkinter import *
from tkinter import ttk
from VISTAS.frame_carreras import VistaCarrera
from VISTAS.frame_alumnos import VistaAlumnos
from VISTAS.frame_profesores import VistaProfesor
from VISTAS.frame_materias import VistaMaterias

class Aplicacion(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.mi_ventana = ventana
        self.mi_ventana.geometry("1024x680")
        self.mi_ventana.title("SISTEMA UNIVERSITARIO")
        self.mi_ventana.iconbitmap("IMG/school.ico")

        #Crea contenedor de menu(paneles) (ttk.Notebook())
        self.menu_principal = ttk.Notebook(self)
        #Panel Inicio
        self.inicio = Label(self.menu_principal, text = "PAGINA INICIO")
        self.menu_principal.add(self.inicio, text = "INICIO")
        #Panel Carreras
        self.carreras = VistaCarrera(self.menu_principal)
        self.menu_principal.add(self.carreras, text = "CARRERAS")
        #Panel Alumnos
        self.alumnos = VistaAlumnos(self.menu_principal)
        self.menu_principal.add(self.alumnos, text = "ALUMNOS")
        #Panel Profesores
        self.profesores = VistaProfesor(self.menu_principal)
        self.menu_principal.add(self.profesores, text = "PROFESORES")
        #Panel Materias
        self.materias = VistaMaterias(self.menu_principal)
        self.menu_principal.add(self.materias, text = "MATERIAS") 
        self.menu_principal.pack()
        self.pack()


        