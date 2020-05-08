from tkinter import *
from tkinter import ttk
from conexion_DB.consultas_db import Conectar_DB


class VistaCarrera(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Metodo para nuevo registro
        def nuevoRegistro():
            self.nombreCarrera.config(state = "normal")
            self.duracionCarrera.config(state = "normal")
            self.nombreCarrera.delete(0,END)
            self.duracionCarrera.delete(0, END)

        #Metodo para insertar datos a BD
        def insertarDatos():
            query = "insert into carrera values (null, ?, ?)"
            #Obtenemos los datos que hay en los entry´s
            parametros = (self.nombreCarrera.get(), self.duracionCarrera.get())
            #Objeto de coneccion
            conn = Conectar_DB()
            conn.run_db(query, parametros)

            ListarDatos()
            


        def eliminarDatos():
            codigo_eliminar = self.tabla.item(self.tabla.selection())['text']
            query = "delete from carrera where codigo_c = ?"
            conn = Conectar_DB()
            conn.run_db(query, (codigo_eliminar,))

            ListarDatos()
            
        def actualizarDatos(codigo_n, codigo_a, nombre_n, nombre_a, duracion_n, duracion_a):
            query = "update carrera set codigo_c = ?, nombre_c = ?, duracion_c = ? where codigo_c = ? and nombre_c = ? and duracion_c = ?"
            parametros = (codigo_n, nombre_n, duracion_n, codigo_a, nombre_a, duracion_a)
            conn = Conectar_DB()
            conn.run_db(query, parametros)
            
            ListarDatos()


        def editarDatos():

            codigo_ = self.tabla.item(self.tabla.selection())['text']
            nombre_antiguo = self.tabla.item(self.tabla.selection())['values'][0]
            duracion_antiguo = self.tabla.item(self.tabla.selection())['values'][1]

            #Crear ventana emergente
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("EDITAR CARRERA")
            #Label y campo codigo
            Label(self.ventana_editar, text = "Codigo De Carrera: ").grid(row = 0, column = 0, padx = 10, pady = 10)
            self.codigoCarrera = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo_), state = "readonly")
            self.codigoCarrera.grid(row = 0, column = 1, padx = 10, pady = 10)
            #Label y campo nombre antiguo
            Label(self.ventana_editar, text = "Nombre De Carrera Antiguo: ").grid(row = 1, column = 0, padx = 10, pady = 10)
            self.nombreAntiguoCarrera = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_antiguo), state = "readonly")
            self.nombreAntiguoCarrera.grid(row = 1, column = 1, padx = 10, pady = 10)
            #Label y campo nombre nuevo
            Label(self.ventana_editar, text = "Nombre De Carrera Nuevo: ").grid(row = 2, column = 0, padx = 10, pady = 10)
            self.nombreNuevoCarrera = Entry(self.ventana_editar)
            self.nombreNuevoCarrera.grid(row = 2, column = 1, padx = 10, pady = 10)
            #Label y campo duracion antiguo
            Label(self.ventana_editar, text = "Duracion De Carrera Antiguo: ").grid(row = 3, column = 0, padx = 10, pady = 10)
            self.duracionAntiguoCarrera = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = duracion_antiguo), state = "readonly")
            self.duracionAntiguoCarrera.grid(row = 3, column = 1, padx = 10, pady = 10)
            #Label y campo duracion nuevo
            Label(self.ventana_editar, text = "Duracion De Carrera Nuevo: ").grid(row = 4, column = 0, padx = 10, pady = 10)
            self.duracionNuevoCarrera = Entry(self.ventana_editar)
            self.duracionNuevoCarrera.grid(row = 4, column = 1, padx = 10, pady = 10)
            #Boton actualizar
            self.btn_actualizar = Button(self.ventana_editar, text = "ACTUALIZAR", command = lambda : actualizarDatos(self.codigoCarrera.get(), codigo_, self.nombreNuevoCarrera.get(), nombre_antiguo, self.duracionNuevoCarrera.get(), duracion_antiguo))
            self.btn_actualizar.grid(row = 5, column = 0, columnspan = 2)

        self.titulo = Label(self, text = "REGISTRAR NUEVA CARRERA")
        self.titulo.grid(row = 0, column = 0, columnspan = 3)
        #Campo nombre de carrera
        Label(self, text = "Nombre De Carrera: ").grid(row = 1, column = 0)
        self.nombreCarrera = Entry(self, state = "readonly")
        self.nombreCarrera.grid(row = 1, column = 1, padx = 10)

        #Campo duracion de carrera
        Label(self, text = "Duracion De Carrera: ").grid(row = 2, column = 0)
        self.duracionCarrera = Entry(self, state = "readonly")
        self.duracionCarrera.grid(row = 2, column = 1, padx = 10)

        #Boton nuevo registro
        Button(self, text = "Nuevo Registro", command = nuevoRegistro).grid(row = 3, column = 0)

        #Boton guardar
        Button(self, text = "Guardar Registro", command = insertarDatos).grid(row = 3, column = 1)

        #Tabla de datos
        self.tabla = ttk.Treeview(self, columns = (" ", " "))
        self.tabla.grid(row = 5, column = 0, columnspan = 4)
        self.tabla.heading("#0", text = "CODIGO DE CARRERA")
        self.tabla.heading("#1", text = "NOMBRE DE CARRERA")
        self.tabla.heading("#2", text = "DURACION DE CARRERA")

        self.btn_editar = Button(self, text = "EDITAR", command = editarDatos)
        self.btn_editar.grid(row = 7, column = 0)
        self.btn_eliminar = Button(self, text = "ELIMINAR", command = eliminarDatos)
        self.btn_eliminar.grid(row = 7, column = 1)
                
        #Metodo para listar datos en la tabla desde la BD
        def ListarDatos():
            #Elimina los registros de la tabla en caso de haber
            registros = self.tabla.get_children()
            for registro in registros:
                self.tabla.delete(registro)
            #Creamos el objeto de la clase de conexion y pasamos la query a ejecutar
            query = "select * from carrera"
            conn = Conectar_DB()
            #guardamos los datos traidos de la query
            datos = conn.run_db(query)
            #Recorremos los datos y los insertamos en la tabla
            for carrera in datos:
                self.tabla.insert("",0, text = carrera[0], values = (carrera[1], carrera[2]))

            
        ListarDatos()
