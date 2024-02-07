import mysql.connector
#from decouple import config

class DBConnector:
    def __init__(self):
        # Cargar las variables de entorno desde el archivo .env
        self.host = config('DB_HOST')
        self.user = config('DB_USER')
        self.password = config('DB_PASSWORD')
        self.database = config('DB_NAME')

        # Establecer la conexión
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchall()

    def execute_insert(self, query, values):
        self.cursor.execute(query, values)
        self.connection.commit()




    def close(self):
        self.cursor.close()
        self.connection.close()
