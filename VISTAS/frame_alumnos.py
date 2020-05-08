from tkinter import ttk
from tkinter import *
from conexion_DB.consultas_db import Conectar_DB

class VistaAlumnos(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevoRegistro ():
            self.input_nombre.config(state = "normal")
            self.input_edad.config(state = "normal")
            self.input_telefono.config(state = "normal")
            

            self.input_nombre.delete(0, END)
            self.input_edad.delete(0, END)
            self.input_telefono.delete(0, END)
            
        #Metodo para insertar datos a BD
        def insertarDatos():
            carrera = self.combo_carreras.get()
            carrera = carrera[0] + carrera[1]

            query = "insert into alumno values (null, ?, ?, ?, ?)"
            parametros = (self.input_nombre.get(), self.input_edad.get(), self.input_telefono.get(), carrera)
            conn = Conectar_DB()
            conn.run_db(query, parametros)

            ListarDatos()

        def eliminarDatos():
            codigo_eliminar = self.tablaDatos.item(self.tablaDatos.selection())['text']
            query = "delete from alumno where codigo_a = ?"
            conn = Conectar_DB()
            conn.run_db(query, (codigo_eliminar,))

            ListarDatos()

        def actualizarDatos(codigo_n, codigo_a, nombre_n, nombre_a, edad_n, edad_a, tel_n, tel_a):
            query = "update alumno set codigo_a = ?, nombre_a = ?, edad_a = ?, telefono_a = ? where codigo_a = ? and nombre_a = ? and edad_a = ? and telefono_a = ?"
            parametros = (codigo_n, nombre_n, edad_n, tel_n, codigo_a, nombre_a, edad_a, tel_a)
            conn = Conectar_DB()
            conn.run_db(query, parametros)
        
            ListarDatos()

        def editarDatos():

            codigo_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['text']
            nombre_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['values'][0]
            edad_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['values'][1]
            telefono_antiguo = self.tablaDatos.item(self.tablaDatos.selection())['values'][2]

            #Crear ventana emergente
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("EDITAR ALUMNO")
            #Label y campo codigo
            Label(self.ventana_editar, text = "Codigo De Alumno: ").grid(row = 0, column = 0, padx = 10, pady = 10)
            self.codigoAlumno = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = codigo_antiguo), state = "readonly")
            self.codigoAlumno.grid(row = 0, column = 1, padx = 10, pady = 10)
            #Label y campo nombre antiguo
            Label(self.ventana_editar, text = "Nombre De Alumno Antiguo: ").grid(row = 1, column = 0, padx = 10, pady = 10)
            self.nombreAntiguoAlumno = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_antiguo), state = "readonly")
            self.nombreAntiguoAlumno.grid(row = 1, column = 1, padx = 10, pady = 10)
            #Label y campo nombre nuevo
            Label(self.ventana_editar, text = "Nombre De Alumno Nuevo: ").grid(row = 2, column = 0, padx = 10, pady = 10)
            self.nombreNuevoAlumno = Entry(self.ventana_editar)
            self.nombreNuevoAlumno.grid(row = 2, column = 1, padx = 10, pady = 10)
            #Label y campo duracion antiguo
            Label(self.ventana_editar, text = "Edad De Alumno Antiguo: ").grid(row = 3, column = 0, padx = 10, pady = 10)
            self.edadAntiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = edad_antiguo), state = "readonly")
            self.edadAntiguo.grid(row = 3, column = 1, padx = 10, pady = 10)
            #Label y campo duracion nuevo
            Label(self.ventana_editar, text = "Edad De Alumno Nuevo: ").grid(row = 4, column = 0, padx = 10, pady = 10)
            self.edadNuevo = Entry(self.ventana_editar)
            self.edadNuevo.grid(row = 4, column = 1, padx = 10, pady = 10)
            #Label y campo telefono antiguo
            Label(self.ventana_editar, text = "Telefono De Alumno Antiguo: ").grid(row = 5, column = 0, padx = 10, pady = 10)
            self.telefonoAntiguo = Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = telefono_antiguo), state = "readonly")
            self.telefonoAntiguo.grid(row = 5, column = 1, padx = 10, pady = 10)
            #Label y campo de telefono nuevo
            Label(self.ventana_editar, text = "Telefono De Alumno Nuevo: ").grid(row = 6, column = 0, padx = 10, pady = 10)
            self.telefonoNuevo = Entry(self.ventana_editar)
            self.telefonoNuevo.grid(row = 6, column = 1, padx = 10, pady = 10)
            #Boton actualizar
            self.btn_actualizar = Button(self.ventana_editar, text = "ACTUALIZAR", command = lambda: actualizarDatos(self.codigoAlumno.get(), codigo_antiguo, self.nombreNuevoAlumno.get(), nombre_antiguo, self.edadNuevo.get(), edad_antiguo, self.telefonoNuevo.get(), telefono_antiguo ))
            self.btn_actualizar.grid(row = 7, column = 0, columnspan = 2)

        #Etiqueta titulo
        self.titulo_alumnos = Label(self, text = "REGISTRAR NUEVO ALUMNO")
        self.titulo_alumnos.grid(row = 0, column = 0) 
        #Etiqueta nombre
        self.nombre_alumno = Label(self, text = "Nombre Del Alumno: ")
        self.nombre_alumno.grid(row = 1, column = 0)
        #Input de texto
        self.input_nombre = Entry(self, state = "readonly")
        self.input_nombre.grid(row = 1, column = 1)
        #Etiqueta edad
        self.edad_alumno = Label(self, text = "Edad: ")
        self.edad_alumno.grid(row = 2, column = 0)
        #Input de edad
        self.input_edad = Entry(self, state = "readonly")
        self.input_edad.grid(row = 2, column = 1)
        #Etiqueta telefono
        self.telefono_alumno = Label(self, text = "Telefono: ")
        self.telefono_alumno.grid(row = 3, column = 0)
        #Input de telefono
        self.input_telefono = Entry(self, state = "readonly")
        self.input_telefono.grid(row = 3, column = 1)
        #Etiqueta codigoCarrer
        self.carreras_disponibles = Label(self, text = "Carreras disponibles: ")
        self.carreras_disponibles.grid(row = 4, column = 0)
        #Combo box donde se mostraran las carreras disponibles
        self.combo_carreras = ttk.Combobox(self)
        self.combo_carreras.grid(row = 4, column = 1)
        #Cargar combo con las carreras
        def cargar_combo():
            query = "select codigo_c, nombre_c from carrera"
            conn = Conectar_DB()
            datos_c = conn.run_db(query)
            
            for carrera in datos_c:
                #Guardamos los valores del combo box en una lista
                values = list(self.combo_carreras['values'])
                #A los valores del combo le concatenamos la lista de carreras
                self.combo_carreras['values'] = values + [(carrera[0], ',' , carrera[1])]
        #Ejecutamos funcion
        cargar_combo()

        #Botones
        self.btn_nuevo = Button(self, text = "Nuevo Registro", command = nuevoRegistro)
        self.btn_nuevo.grid(row = 5, column = 0)
        self.btn_guardar = Button(self, text = "Guardar", command = insertarDatos)
        self.btn_guardar.grid(row = 5, column = 1)
        #Tabla de datos
        self.tablaDatos = ttk.Treeview(self, columns = (" ", " ", " ", " "))
        self.tablaDatos.grid(row = 6, column = 0, columnspan = 9)
        self.tablaDatos.heading("#0", text = "CODIGO")
        self.tablaDatos.heading("#1", text = "NOMBRE")
        self.tablaDatos.heading("#2", text = "EDAD")
        self.tablaDatos.heading("#3", text = "TELEFONO")
        self.tablaDatos.heading("#4", text = "CARRERA")

        self.btn_editar = Button(self, text = "EDITAR", command = editarDatos)
        self.btn_editar.grid(row = 7, column = 0)
        self.btn_eliminar = Button(self, text = "ELIMINAR", command = eliminarDatos)
        self.btn_eliminar.grid(row = 7, column = 1)

        def ListarDatos():
            registros = self.tablaDatos.get_children()
            for registro in registros:
                self.tablaDatos.delete(registro)
            #Se modifico la query para traernos el nombre de la carrera del alumno
            #y hacer una consulta en dos tablas 
            query = "select alumno.codigo_a, alumno.nombre_a, alumno.edad_a, alumno.telefono_a, carrera.nombre_c \
                    from alumno inner join carrera on alumno.codigo_c1 = carrera.codigo_c"
            conn = Conectar_DB()
            datos = conn.run_db(query)

            for alumno in datos:
                self.tablaDatos.insert("",0, text=alumno[0], values = (alumno[1], alumno[2], alumno[3], alumno[4]))
            
        ListarDatos()