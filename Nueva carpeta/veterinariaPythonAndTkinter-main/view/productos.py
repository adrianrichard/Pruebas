class Producto:
    def __init__(self, nombre, cantidad):
        self._nombre = nombre
        self._cantidad = cantidad

    # Getters
    def get_nombre(self):
        return self._nombre
    
    def get_cantidad(self):
        return self._cantidad  

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad