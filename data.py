import mysql.connector
from mysql.connector import Error

class Error(Exception):
    """Clase base para otras excepciones"""
    pass

class AppHotel:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='tu_contraseña',  # Reemplazar por tu contraseña de MySQL
                database='HotelDB'
            )
            self.cursor = self.conexion.cursor()
            print("✔ Conexión establecida con la base de datos.")
        except mysql.connector.Error as e:
            raise Error(f"No se pudo conectar a la base de datos: {e}")

    def cerrarConexion(self):
        if self.conexion.is_connected():
            self.cursor.close()
            self.conexion.close()
            print("✔ Conexión cerrada.")

    # CRUD para Clientes
    def registrarCliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        email = input("Ingrese el email del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")

        try:
            query = "INSERT INTO Clientes (nombre, apellido, email, telefono, direccion) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (nombre, apellido, email, telefono, direccion))
            self.conexion.commit()
            print("✔ Cliente registrado exitosamente.")
        except mysql.connector.Error as e:
            print(f"❌ Error al registrar cliente: {e}")

    def mostrarClientes(self):
        try:
            query = "SELECT * FROM Clientes"
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            print("\nClientes Registrados:")
            for cliente in resultados:
                print(cliente)
        except mysql.connector.Error as e:
            print(f"❌ Error al mostrar clientes: {e}")

    # CRUD para Habitaciones
    def registrarHabitacion(self):
        numero_habitacion = int(input("Ingrese el número de habitación: "))
        tipo = input("Ingrese el tipo de habitación (Simple, Doble, Suite): ")
        precio = float(input("Ingrese el precio de la habitación: "))

        try:
            query = "INSERT INTO Habitaciones (numero_habitacion, tipo, precio) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (numero_habitacion, tipo, precio))
            self.conexion.commit()
            print("✔ Habitación registrada exitosamente.")
        except mysql.connector.Error as e:
            print(f"❌ Error al registrar habitación: {e}")

    def mostrarHabitaciones(self):
        try:
            query = "SELECT * FROM Habitaciones"
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            print("\nHabitaciones Disponibles:")
            for habitacion in resultados:
                print(habitacion)
        except mysql.connector.Error as e:
            print(f"❌ Error al mostrar habitaciones: {e}")

    # CRUD para Reservas
    def realizarReserva(self):
        id_cliente = int(input("Ingrese el ID del cliente: "))
        id_habitacion = int(input("Ingrese el ID de la habitación: "))
        fecha_entrada = input("Ingrese la fecha de entrada (YYYY-MM-DD): ")
        fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")

        try:
            query = "INSERT INTO Reservas (id_cliente, id_habitacion, fecha_entrada, fecha_salida) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (id_cliente, id_habitacion, fecha_entrada, fecha_salida))
            self.conexion.commit()
            print("✔ Reserva realizada exitosamente.")
        except mysql.connector.Error as e:
            print(f"❌ Error al realizar reserva: {e}")

    def mostrarReservas(self):
        try:
            query = "SELECT * FROM Reservas"
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            print("\nReservas Realizadas:")
            for reserva in resultados:
                print(reserva)
        except mysql.connector.Error as e:
            print(f"❌ Error al mostrar reservas: {e}")

    # CRUD para Pagos
    def registrarPago(self):
        id_reserva = int(input("Ingrese el ID de la reserva: "))
        metodo_pago = input("Ingrese el método de pago (Tarjeta, Efectivo, Transferencia): ")
        monto = float(input("Ingrese el monto del pago: "))
        fecha_pago = input("Ingrese la fecha de pago (YYYY-MM-DD): ")

        try:
            query = "INSERT INTO Pagos (id_reserva, metodo_pago, monto, fecha_pago) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (id_reserva, metodo_pago, monto, fecha_pago))
            self.conexion.commit()
            print("✔ Pago registrado exitosamente.")
        except mysql.connector.Error as e:
            print(f"❌ Error al registrar pago: {e}")

    def mostrarPagos(self):
        try:
            query = "SELECT * FROM Pagos"
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            print("\nPagos Realizados:")
            for pago in resultados:
                print(pago)
        except mysql.connector.Error as e:
            print(f"❌ Error al mostrar pagos: {e}")


def appHotelCocolon():
    return None
