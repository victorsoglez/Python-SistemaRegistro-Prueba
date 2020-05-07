from tkinter import *
from tkinter import ttk
from conexion_DB.consultas_db import Conectar_DB

class VistaMaterias(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevoRegistro():
            self.input_nombre.config(state = "normal")
            self.input_creditos.config(state = "normal")

            self.input_nombre.delete(0, END)
            self.input_creditos.delete(0, END)

        def insertarDatos():
            query = "insert into materia values (null, ?, ?)"
            parametros = (self.input_nombre.get(), self.input_creditos.get())
            conn = Conectar_DB()
            conn.run_db(query, parametros)

            listarDatos()

        def eliminarDatos():
            codigo_eliminar = self.tablaDatos.item(self.tablaDatos.selection())['text']
            query = "delete from materia where codigo_m = ?"
            conn = Conectar_DB()
            conn.run_db(query, (codigo_eliminar,))

            listarDatos()

        def actualizarDatos(codigo_nu, codigo_an, nombre_nu, nombre_an, creditos_nu, creditos_an):
            query = "update materia set codigo_m = ?, nombre_m = ?, creditos_m = ? where codigo_m = ? and nombre_m = ? and creditos_m = ?"
            parametros = (codigo_nu, nombre_nu, creditos_nu, codigo_an, nombre_an, creditos_an)
            conn = Conectar_DB()
            conn.run_db(query, parametros)
            
            listarDatos()

        def editarDatos():

            codigo_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['text']
            nombre_materia_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['values'][0]
            creditos_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['values'][1]


            #Crear ventana emergente
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("EDITAR MATERIAS")
            #Label y campo codigo
            Label(self.ventana_editar, text = "Codigo De Materia: ").grid(row = 0, column = 0, padx = 10, pady = 10)
            self.codigoMateria = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo_antiguo), state = "readonly")
            self.codigoMateria.grid(row = 0, column = 1, padx = 10, pady = 10)
            #Label y campo nombre antiguo
            Label(self.ventana_editar, text = "Nombre De Materias Antiguo: ").grid(row = 1, column = 0, padx = 10, pady = 10)
            self.nombreMateriAntiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_materia_antiguo), state = "readonly")
            self.nombreMateriAntiguo.grid(row = 1, column = 1, padx = 10, pady = 10)
            #Label y campo nombre nuevo
            Label(self.ventana_editar, text = "Nombre De Materia Nuevo: ").grid(row = 2, column = 0, padx = 10, pady = 10)
            self.nombreMateriNuevo = Entry(self.ventana_editar)
            self.nombreMateriNuevo.grid(row = 2, column = 1, padx = 10, pady = 10)
            #Label y campo telefono antiguo
            Label(self.ventana_editar, text = "Creditos De Materia Antiguo: ").grid(row = 3, column = 0, padx = 10, pady = 10)
            self.creditosAntiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = creditos_antiguo), state = "readonly")
            self.creditosAntiguo.grid(row = 3, column = 1, padx = 10, pady = 10)
            #Label y campo telefono nuevo
            Label(self.ventana_editar, text = "Creditos de Materia Nuevo: ").grid(row = 4, column = 0, padx = 10, pady = 10)
            self.creditosNuevo = Entry(self.ventana_editar)
            self.creditosNuevo.grid(row = 4, column = 1, padx = 10, pady = 10)
            #Boton actualizar
            self.btn_actualizar = Button(self.ventana_editar, text = "ACTUALIZAR", command = lambda : actualizarDatos(self.codigoMateria.get(), codigo_antiguo, self.nombreMateriNuevo.get(), nombre_materia_antiguo, self.creditosNuevo.get(), creditos_antiguo))
            self.btn_actualizar.grid(row = 5, column = 0, columnspan = 2)


        self.titulo_materia = Label(self, text = "REGISTRO DE MATERIAS")
        self.titulo_materia.grid(row = 0, column = 0)

        self.nombre_mat = Label(self, text = "Nombre: ")
        self.nombre_mat.grid(row = 1, column = 0)
        self.input_nombre = Entry(self, state = "readonly")
        self.input_nombre.grid(row = 1, column = 1)

        self.creditos_mat = Label(self, text = "Creditos: ")
        self.creditos_mat.grid(row = 2, column = 0)
        self.input_creditos = Entry(self, state = "readonly")
        self.input_creditos.grid(row = 2, column = 1)

         #Botones
        self.btn_nuevo = Button(self, text = "Nuevo Registro", command = nuevoRegistro)
        self.btn_nuevo.grid(row = 4, column = 0)
        self.btn_guardar = Button(self, text = "Guardar", command = insertarDatos)
        self.btn_guardar.grid(row = 4, column = 1)
        #Tabla de datos
        self.tablaDatos = ttk.Treeview(self, columns = (" ", " "))
        self.tablaDatos.grid(row = 6, column = 0, columnspan = 9)
        self.tablaDatos.heading("#0", text = "CODIGO")
        self.tablaDatos.heading("#1", text = "NOMBRE")
        self.tablaDatos.heading("#2", text = "CREDITOS")

        self.btn_editar = Button(self, text = "EDITAR", command = editarDatos)
        self.btn_editar.grid(row = 7, column = 0)
        self.btn_eliminar = Button(self, text = "ELIMINAR", command = eliminarDatos)
        self.btn_eliminar.grid(row = 7, column = 1)

        def listarDatos():
            registros = self. tablaDatos.get_children()
            for registro in registros:
                self.tablaDatos.delete(registro)

            query = "select * from materia"
            conn = Conectar_DB()
            datos = conn.run_db(query)

            for materia in datos:
                self.tablaDatos.insert("",0, text = materia[0], values = (materia[1], materia[2]))

        listarDatos()



        