import sqlite3

class Conectar_DB():
    nombre_db = "DATA_BASE/BD_SistemaEscuela.db"

    def run_db(self, query, parametros = ()):
        with sqlite3.connect(self.nombre_db) as conn:
            cursor = conn.cursor()
            datos = cursor.execute(query, parametros)

            conn.commit()
        return datos