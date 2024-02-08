import mysql.connector

class EquipoDB:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cuadrangular"
        )
        self.cursor = self.connection.cursor()

    def crear_equipo(self, nombre):
        query = "INSERT INTO equipos (nombre) VALUES (%s)"
        self.cursor.execute(query, (nombre,))
        self.connection.commit()

    def obtener_equipos(self):
        query = "SELECT * FROM equipos"
        self.cursor.execute(query)
        equipos = []
        for equipo in self.cursor.fetchall():
            equipos.append(Equipo(equipo[1]))
        return equipos

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()
