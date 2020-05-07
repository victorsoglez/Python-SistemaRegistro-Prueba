from tkinter import *
from tkinter import ttk
from conexion_DB.consultas_db import Conectar_DB

class VistaProfesor(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevoRegistro():
            self.input_nombre.config(state = "normal")
            self.input_telefono.config(state = "normal")
            self.input_direccion.config(state = "normal")

            self.input_nombre.delete(0, END)
            self.input_telefono.delete(0, END)
            self.input_direccion.delete(0, END)

        def insertarDatos():
            query = "insert into profesor values (null, ?, ?, ?)"
            parametros = (self.input_nombre.get(), self.input_telefono.get(), self.input_direccion.get())
            conn = Conectar_DB()
            conn.run_db(query, parametros)

            listarDatos()

        def eliminarDatos():
            codigo_eliminar = self.tablaDatos.item(self.tablaDatos.selection())['text']
            query = "delete from profesor where codigo_p = ?"
            conn = Conectar_DB()
            conn.run_db(query, (codigo_eliminar,))

            listarDatos()

        def actualizarDatos(codigo_nu, codigo_an, nombre_nu, nombre_an, telefono_nu, telefono_an, direccion_nu, direccion_an):
            query = "update profesor set codigo_p = ?, nombre_p = ?, telefono_p = ?, direccion_p = ? where codigo_p = ? and nombre_p = ? and telefono_p = ? and direccion_p = ?"
            parametros = (codigo_nu, nombre_nu, telefono_nu, direccion_nu, codigo_an, nombre_an, telefono_an, direccion_an)
            conn = Conectar_DB()
            conn.run_db(query, parametros)

            listarDatos()

        def editarDatos():

            codigo_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['text']
            nombre_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['values'][0]
            telefono_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['values'][1]
            direccion_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['values'][2]

            #Crear ventana emergente
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("EDITAR PROFESORES")
            #Label y campo codigo
            Label(self.ventana_editar, text = "Codigo De Profesor: ").grid(row = 0, column = 0, padx = 10, pady = 10)
            self.codigoProfe = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo_antiguo), state = "readonly")
            self.codigoProfe.grid(row = 0, column = 1, padx = 10, pady = 10)
            #Label y campo nombre antiguo
            Label(self.ventana_editar, text = "Nombre De Profesor Antiguo: ").grid(row = 1, column = 0, padx = 10, pady = 10)
            self.nombreAntiguoProfe = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_antiguo), state = "readonly")
            self.nombreAntiguoProfe.grid(row = 1, column = 1, padx = 10, pady = 10)
            #Label y campo nombre nuevo
            Label(self.ventana_editar, text = "Nombre De Profesor Nuevo: ").grid(row = 2, column = 0, padx = 10, pady = 10)
            self.nombreNuevoProfe = Entry(self.ventana_editar)
            self.nombreNuevoProfe.grid(row = 2, column = 1, padx = 10, pady = 10)
            #Label y campo telefono antiguo
            Label(self.ventana_editar, text = "Telefono De Profesor Antiguo: ").grid(row = 3, column = 0, padx = 10, pady = 10)
            self.telefonoAntiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = telefono_antiguo), state = "readonly")
            self.telefonoAntiguo.grid(row = 3, column = 1, padx = 10, pady = 10)
            #Label y campo telefono nuevo
            Label(self.ventana_editar, text = "Telefono De Profesor Nuevo: ").grid(row = 4, column = 0, padx = 10, pady = 10)
            self.telefonoNuevo = Entry(self.ventana_editar)
            self.telefonoNuevo.grid(row = 4, column = 1, padx = 10, pady = 10)
            #Label y campo telefono antiguo
            Label(self.ventana_editar, text = "Direccion De Profesor Antiguo: ").grid(row = 5, column = 0, padx = 10, pady = 10)
            self.direccionAntiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = direccion_antiguo), state = "readonly")
            self.direccionAntiguo.grid(row = 5, column = 1, padx = 10, pady = 10)
            #Label y campo de telefono nuevo
            Label(self.ventana_editar, text = "Direccion De Profesor Nuevo: ").grid(row = 6, column = 0, padx = 10, pady = 10)
            self.direccionNuevo = Entry(self.ventana_editar)
            self.direccionNuevo.grid(row = 6, column = 1, padx = 10, pady = 10)
            #Boton actualizar
            self.btn_actualizar = Button(self.ventana_editar, text = "ACTUALIZAR", command = lambda : actualizarDatos(self.codigoProfe.get(), codigo_antiguo, self.nombreNuevoProfe.get(), nombre_antiguo, self.telefonoNuevo.get(), telefono_antiguo, self.direccionNuevo.get(), direccion_antiguo ))
            self.btn_actualizar.grid(row = 7, column = 0, columnspan = 2)

        self.titulo_label = Label(self, text = "REGISTRO PROFESORES")
        self.titulo_label.grid(row = 0, column = 0)

        self.nombre_prof = Label(self, text = "Nombre: ")
        self.nombre_prof.grid(row = 1, column = 0)
        self.input_nombre = Entry(self, state = "readonly")
        self.input_nombre.grid(row = 1, column = 1)

        self.telefono_prof = Label(self, text = "Telefono: ")
        self.telefono_prof.grid(row = 2, column = 0)
        self.input_telefono = Entry(self, state = "readonly")
        self.input_telefono.grid(row = 2, column = 1)

        self.direccion_prof = Label(self, text = "Direccion: ")
        self.direccion_prof.grid(row = 3, column = 0)
        self.input_direccion = Entry(self, state = "readonly")
        self.input_direccion.grid(row = 3, column = 1)
        #Botones
        self.btn_nuevo = Button(self, text = "Nuevo Registro", command = nuevoRegistro)
        self.btn_nuevo.grid(row = 4, column = 0)
        self.btn_guardar = Button(self, text = "Guardar", command = insertarDatos)
        self.btn_guardar.grid(row = 4, column = 1)
        #Tabla de datos
        self.tablaDatos = ttk.Treeview(self, columns = (" ", " ", " "))
        self.tablaDatos.grid(row = 6, column = 0, columnspan = 9)
        self.tablaDatos.heading("#0", text = "CODIGO")
        self.tablaDatos.heading("#1", text = "NOMBRE")
        self.tablaDatos.heading("#2", text = "TELEFONO")
        self.tablaDatos.heading("#3", text = "DIRECCION")

        self.btn_editar = Button(self, text = "EDITAR", command = editarDatos)
        self.btn_editar.grid(row = 7, column = 0)
        self.btn_eliminar = Button(self, text = "ELIMINAR", command = eliminarDatos)
        self.btn_eliminar.grid(row = 7, column = 1)



        def listarDatos():
            registros = self.tablaDatos.get_children()
            for registro in registros:
                self.tablaDatos.delete(registro)
            
            query = "select * from profesor"
            conn = Conectar_DB()
            datos = conn.run_db(query)

            for profe in datos:
                self.tablaDatos.insert("",0, text = profe[0], values = (profe[1], profe[2], profe[3]))

        listarDatos()
       

       
