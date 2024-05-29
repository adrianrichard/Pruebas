import tkinter as tk
from tkinter import ttk
#lista de palabras reservadas
palabras_reservadas_cpp = [
    'alignas', 'alignof', 'and', 'and_eq', 'asm', 'auto', 'bitand', 'bitor', 'bool', 'break',
    'case', 'catch', 'char', 'char8_t', 'char16_t', 'char32_t', 'class', 'compl', 'concept', 'const', 'consteval', 'constexpr', 'constinit', 'const_cast', 'continue',
    'cout','co_await', 'co_return', 'co_yield','decltype', 'default', 'delete', 'do', 'double', 'dynamic_cast',
    'else','endl', 'enum', 'explicit', 'export', 'extern','false', 'float', 'for', 'friend','goto','if', 'inline', 'int', 'long',
    'mutable', 'namespace', 'new', 'noexcept', 'not', 'not_eq', 'nullptr', 'operator', 'or', 'or_eq',
    'private', 'protected', 'public', 'register', 'reinterpret_cast', 'requires', 'return',
    'short', 'signed', 'sizeof', 'static', 'std','static_assert', 'static_cast', 'struct', 'switch',
    'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid', 'typename',
    'union', 'unsigned', 'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while', 'xor', 'xor_eq'
]
#lista de operadores
operadores_cpp = [
    '+', '-', '*', '/', '%',     '=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=',
    '++', '--', '==', '!=', '<', '>', '<=', '>=','&&', '||', '!', '&', '|', '^', '~', '<<', '>>',
    '?', ':', '*', '&', '.', '->','sizeof'
    ]
class Token:
    def __init__(self, tipo, valor): #se define el elemento token
        self.tipo = tipo
        self.valor = valor

class analizador_lexico: #clase analizador lexico
    def __init__(self, codigo_completo):
        self.codigo = codigo_completo  #recibe el texto completo como string
        self.posicion = 0     #posiciona al principio

    def avanzar(self):   #para avanzar 1 posición en el texto
        self.posicion += 1

    def leer_caracter(self):  #obtiene el caracter en "posicion"
        if self.posicion < len(self.codigo):
            return self.codigo[self.posicion]
        else:
            return None #si llego al final devuelve None

    def hacer_tokens(self):
        tokens = [] #vector de tokens
        
        while self.posicion < len(self.codigo): #mientras no llegue al final
            caracter_actual = self.leer_caracter() #primer caracter

            if caracter_actual is None:
                break
            elif caracter_actual.isspace(): #si es un espacio
                while caracter_actual.isspace(): #mientras siga siendo un espacio
                    self.avanzar() #avanza 1 posición
                    caracter_actual = self.leer_caracter() #leo el sgte caracter
                tokens.append(Token("ESPACIO", '')) #guarda el token de ESPACIO
            elif caracter_actual.isalpha():     #si es una letra
                palabra = self.leer_palabra() #lee toda la palabra
                tipo_token = self.tipo_palabra_reservada(palabra) #si es una palabra
                tokens.append(Token(tipo_token, palabra)) #guarda el token de PALABRA RESERVADA o IDENTIFICADOR
            elif caracter_actual.isdigit(): #Si es un digito
                numero = self.leer_numero() #lee el número completo, incluso si es decimal
                tokens.append(Token("NUMERO", numero)) #guarda el token de NUMERO
            elif caracter_actual == '"':  #para leer una cadena
                self.avanzar()
                cadena = self.leer_cadena() #lee la cadena completa
                tokens.append(Token("CADENA", cadena)) #guarda el token de CADENA
                self.avanzar()
            elif caracter_actual in operadores_cpp: #Si es un operador
                operadores = self.leer_operador() #esta función es por si es un operador doble
                tokens.append(Token("OPERADOR", operadores)) #guarda el token de OPERADOR
                self.avanzar()
            else:
                self.avanzar()

        return tokens

    def leer_palabra(self): #lee las palabras y define si es PALABRA RESERVADA o IDENTIFICADOR
        palabra = ""
        while self.posicion < len(self.codigo): #si no llega al final
            caracter_actual = self.leer_caracter()
            if caracter_actual is not None and caracter_actual.isalnum(): #si no está vacio y es alfanumérico
                palabra += caracter_actual  #contacatena los caracteres
                self.avanzar()
            else:
                break
        return palabra #devuelve la palabra

    def tipo_palabra_reservada(self, palabra): #una vez que obtengo la palabra
        if palabra in palabras_reservadas_cpp:  #defino si es RESERVADA o IDENTIFICADOR
            return "PALABRA RESERVADA"
        else:
            return "IDENTIFICADOR"

    def leer_numero(self): #para leer en nro completo
        numero = ""
        while self.posicion < len(self.codigo):
            caracter_actual = self.leer_caracter()
            if caracter_actual is not None and (caracter_actual.isdigit() or caracter_actual == '.'):
            #si es un digito o un punto .
                numero += caracter_actual  #concatena el número
                self.avanzar()
            else:
                break
        return numero  #devuelve el número
    
    def leer_operador(self):
        operador=""
        while self.posicion < len(self.codigo):
            caracter_actual = self.leer_caracter()
            operador=caracter_actual
            if (self.posicion+1 < len(self.codigo)): #avanzo 1 posición
                self.avanzar()
                caracter_actual+=self.leer_caracter()  #concateno ambos caracteres
            if caracter_actual in operadores_cpp:  #me fijo si es un operador doble
                operador=caracter_actual
                return operador
            else:
                break
        return operador #decuelve el operador

#CREAR FUNCIONES PARA CADENAS Y OPERADORES COMPUESTOS
    def leer_cadena(self): #ingresa porque el caracter leído era un "
        cadena = ""
        while self.posicion < len(self.codigo):
            caracter_actual = self.leer_caracter()
            if caracter_actual != '"': #si el caracter es distinto de "
                cadena+=caracter_actual #concatena todo
                self.avanzar()
            else:
                break
        return cadena  #devuelve la cadena

def analizar():
    texto = cuadro_texto.get("1.0", "end-1c") #caja de texto    
    
    if texto=='':
        agregar.config(state='normal')
    else:
        agregar.config(state='disabled')
    
    lexer = analizador_lexico(texto)  #instancia del analizador lexico
    tokens = lexer.hacer_tokens() #crea los tokens
    i = 0
    tabla_token.delete(*tabla_token.get_children()) #borra la tabla
    for token in tokens: #agrega los tokens a la tabla
        tabla_token.insert("", "end", i, text='', values=(token.tipo, token.valor))
        i+=1    
    del lexer #elimina la instancia
    
# Crear la ventana principal
ventana = tk.Tk()  #crea la ventana
ventana.configure(background='slate gray') #color de fondo de la ventana
ventana.title("Analizador léxico") #titulo de la ventana
ventana.resizable(False, False)

#Titulo
Titulo = tk.Label(ventana, text= "Analizador léxico C++  -  Arrejin - Richard", width=63, borderwidth=2, relief="sunken", font=('Arial', 12, 'bold'))
Titulo.grid(column=0, row=0, columnspan=3, pady=(10, 10))
Titulo_codigo = tk.Label(ventana, text= "Código", width=60, bg='slate gray', font=('Arial', 12, 'bold'), anchor="w")
Titulo_codigo.grid(column=0, row=1, columnspan=3, pady= 10)

#Cuadro de texto
cuadro_texto = tk.Text(ventana, width=40, borderwidth=2,  relief="solid")
cuadro_texto.grid(column=0, row=2)

#formato de los headers de la tabla
style = ttk.Style()
style.configure("mystyle.Treeview.Heading", font=('Arial', 12,'bold'))

#tabla
tabla_token = ttk.Treeview(columns=("Tokens", "Identificador"), height=18, show='headings', style="mystyle.Treeview")
tabla_token.grid(column=1, row=2)
tabla_token.heading("Tokens", text="Tokens")
tabla_token.heading("Identificador", text="Identificador")
tabla_token.column("Tokens", width=150)
tabla_token.column("Identificador", width=150)
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla_token.yview)
tabla_token.configure(yscroll=scrollbar.set)
scrollbar.grid(row=2, column=2, sticky='ns')
#cartel
agregar=tk.Label(ventana,text= "¡Agregue el código!", state='disabled',fg='white',bg='slate gray', font=('Arial', 15, 'bold'))
agregar.grid(column=0, row=3, pady=(10, 10))
# Crear el botón para cargar el contenido del widget Text en un vector
boton_analizar = tk.Button(ventana, text="Analizar código", font=('Arial', 12, 'bold'), command=analizar)
boton_analizar.grid(column=1, row=3, pady=(10, 10))

ventana.mainloop()