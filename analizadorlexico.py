import tkinter as tk
from tkinter import ttk
import re
palabras=[]
tokens=[]
palabras_reservadas_cpp = [
    'alignas', 'alignof', 'and', 'and_eq', 'asm', 'auto', 'bitand', 'bitor', 'bool', 'break',
    'case', 'catch', 'char', 'char8_t', 'char16_t', 'char32_t', 'class', 'compl', 'concept', 'const', 'consteval', 'constexpr', 'constinit', 'const_cast', 'continue',
    'cout','co_await', 'co_return', 'co_yield','decltype', 'default', 'delete', 'do', 'double', 'dynamic_cast',
    'else','endl', 'enum', 'explicit', 'export', 'extern','false', 'float', 'for', 'friend','goto','if', 'inline', 'int', 'long',
    'mutable', 'namespace', 'new', 'noexcept', 'not', 'not_eq', 'nullptr', 'operator', 'or', 'or_eq',
    'private', 'protected', 'public', 'register', 'reinterpret_cast', 'requires', 'return',
    'short', 'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'struct', 'switch',
    'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid', 'typename',
    'union', 'unsigned', 'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while', 'xor', 'xor_eq'
]

operadores_cpp = [
    '+', '-', '*', '/', '%',     '=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=',
    '++', '--', '==', '!=', '<', '>', '<=', '>=','&&', '||', '!', '&', '|', '^', '~', '<<', '>>',
    '?', ':', '*', '&', '.', '->','sizeof'
    ]
class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        
class Lexer:
    def __init__(self, codigo_completo):
        self.codigo = codigo_completo        
        self.posicion = 0

    def avanzar(self):
        self.posicion += 1

    def leer_caracter(self):
        if self.posicion < len(self.codigo):
            return self.codigo[self.posicion]
        else:
            return None

    def hacer_tokens(self):
        tokens = []
        
        while self.posicion < len(self.codigo):
            caracter_actual = self.leer_caracter()

            if caracter_actual is None:
                break
            elif caracter_actual.isspace():
                self.avanzar()
            elif caracter_actual.isalpha():
                palabra = self.leer_palabra()
                tipo_token = self.tipo_palabra_reservada(palabra)
                tokens.append(Token(tipo_token, palabra))
            elif caracter_actual.isdigit():
                numero = self.leer_numero()
                tokens.append(Token("NUMERO", numero))
            elif caracter_actual == '"':
                self.avanzar()
                cadena = self.leer_cadena()
                tokens.append(Token("CADENA", cadena))
                #print (cadena)
                self.avanzar()
            elif caracter_actual in operadores_cpp:
                tokens.append(Token("OPERADOR", caracter_actual))
                self.avanzar()
            else:
                self.avanzar()

        return tokens

    def leer_palabra(self):
        palabra = ""
        while self.posicion < len(self.codigo):
            caracter_actual = self.leer_caracter()
            if caracter_actual is not None and caracter_actual.isalnum():
                palabra += caracter_actual
                self.avanzar()
            else:
                break
        return palabra

    def tipo_palabra_reservada(self, palabra):
        if palabra in palabras_reservadas_cpp:
            return "PALABRA RESERVADA"
        else:
            return "IDENTIFICADOR"

    def leer_numero(self):
        numero = ""
        while self.posicion < len(self.codigo):
            caracter_actual = self.leer_caracter()
            if caracter_actual is not None and (caracter_actual.isdigit() or caracter_actual == '.'):
                numero += caracter_actual
                self.avanzar()
            else:
                break
        return numero

#CREAR FUNCIONES PARA CADENAS Y OPERADORES COMPUESTOS
    def leer_cadena(self):
        cadena = ""
        #print("posicion",self.posicion, self.leer_caracter())
        while self.posicion < len(self.codigo):
            caracter_actual = self.leer_caracter()
            #print(caracter_actual)
            if caracter_actual != '"':
                cadena+=caracter_actual                
                self.avanzar()
            else:
                break
        return cadena

def analizar():    
    texto = cuadro_texto.get("1.0", "end-1c")
    lexer = Lexer(texto)
    tokens = lexer.hacer_tokens()
    i = 0
    tabla_token.delete(*tabla_token.get_children())
    for token in tokens:       
        tabla_token.insert("", "end", i, text=token.tipo, values=(token.valor, token.tipo))
        i+=1
    del lexer
    
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador léxico")

#Titulo
Titulo = tk.Label(ventana, text= "Analizador léxico C++ - Arrejin-Richard", width=40)
Titulo.grid(column=0, row=0, columnspan=2)
#Cuadro de texto
cuadro_texto = tk.Text(ventana, width=40)
cuadro_texto.grid(column=0, row=1)
#tabla
tabla_token = ttk.Treeview(columns=("Tokens", "Identificador"), height=18, show='headings')
tabla_token.grid(column=1, row=1)
tabla_token.heading("Tokens", text="Tokens")
tabla_token.heading("Identificador", text="Identificador")
tabla_token.column("Tokens", width=150)
tabla_token.column("Identificador", width=150)
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla_token.yview)
tabla_token.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=2, sticky='ns')
# Crear el botón para cargar el contenido del widget Text en un vector
boton_analizar = tk.Button(ventana, text="Analizar código", command=analizar)
boton_analizar.grid(column=0, row=2)

ventana.mainloop()

'''#include <iostream>
using namespace std;

class MiClase {
private:
    int numero;

public:
    MiClase(int n) {
        numero = n;
    }

    void imprimirNumero() {
        cout << "El número almacenado es: " << numero << endl;
    }
};

int main() {
    for (int i = 1; i <= 5; ++i) {
        cout << "Número: " << i << endl;
    }

    MiClase objeto(10);

    objeto.imprimirNumero();

    return 0;
}
'''