import mysql.connector
from productos import Producto 
class ProductoRepository:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def guardar_producto(self, producto : Producto):
        query = """
            INSERT INTO productos (nombre, cantidad)
            VALUES (%s, %s)
        """
        values = (
            producto.get_nombre(),
            producto.get_cantidad()
        )

        try:
            cursor = self.db_connector.connection.cursor()
            cursor.execute(query, values)
            self.db_connector.connection.commit()
            cursor.close()
            print("Producto guardado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al guardar el producto: {err}")

    def listar_productos(self):
        query = "SELECT * FROM productos"
        try:
            cursor = self.db_connector.connection.cursor(dictionary=True)
            cursor.execute(query)
            productos = []
            for row in cursor.fetchall():
                producto = Producto(
                    row["nombre"],
                    row["cantidad"]
                )
                productos.append(producto)
            cursor.close()
            return productos
        except mysql.connector.Error as err:
            print(f"Error al listar los productos: {err}")
            return []



    def actualizar_producto(self, producto):
        query = """
            UPDATE productos
            SET nombre = %s, cantidad = %s
            WHERE nombre = %s
        """
        values = (
            producto.get_nombre(),
            producto.get_cantidad(),
        )

        try:
            cursor = self.db_connector.connection.cursor()
            cursor.execute(query, values)
            self.db_connector.connection.commit()
            cursor.close()
            print("Producto actualizado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar el producto: {err}")