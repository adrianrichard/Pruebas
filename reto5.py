##Para el reto de hoy vamos a definir 5 nuevas funciones; esto con la finalidad de poder separar nuestro código
##y que este sea fácil de leer, comprender y sobre todo mantener.
##Las 5 nuevas funciones serán las siguientes.
##new_user
##show_user
##edit_user
##delete_user
##list_users
##Las funciones, como bien sus nombre nos indican, nos permitirán seperar nuestra lógica
##para poder crear nuevos usuarios, consultarlos, editarlos, eliminarlos (Que es una nueva acción) y listarlos.
##Con Excepción de list_users y new_user, cada una de estas funciones deberá recibir como parámetro el ID de usuario con el cual se desea trabajar.
##Un pro Tip. Recuerda que las opciones puedas almacenarlas en como llaves en un diccionario y que, quizás,
##puedas almacenar las funciones en valores de esas llaves.

Lista_usuarios=[]
usuario={}
ID_usuario=0

def new_user(ID_usuario):
    valido = True

    while(valido):
        nombre=input("Ingresa tu nombre: ")
        cont=0
        for letra in nombre:
            cont=cont+1
        if cont<5:
            print("la longitud deber ser mayor a 4, ingrese nuevamente")
        elif cont>50:
            print("la longitud debe ser menor a 50, ingrese nuevamente")
        else:
            valido = False

    valido = True

    while(valido):
        apellido=input("Ingresa tu apellido: ")
        cont=0
        for letra in apellido:
            cont=cont+1
        if cont<5:
            print("la longitud deber ser mayor a 4, ingrese nuevamente")
        elif cont>50:
            print("la longitud debe ser menor a 50, ingrese nuevamente")
        else:
            valido = False

    valido = True

    while(valido):
        telefono=int(input("Ingresa tu número de teléfono: "))
        if telefono%10 != 0:
            print("El número de teléfono debe tener 10 dígitos, ingrese nuevamente")
        else:
            valido = False

    valido = True

    while(valido):
        email=input("Ingresa tu correo electrónico: ")
        cont=0
        for letra in email:
            cont=cont+1
        if cont<5:
            print("la longitud deber ser mayor a 4, ingrese nuevamente")
        elif cont>50:
            print("la longitud debe ser menor a 50, ingrese nuevamente")
        else:
            valido = False

    usuario={'ID':ID_usuario, 'nombre': nombre, 'apellido': apellido, 'telefono': telefono, 'email': email}
    Lista_usuarios.append(usuario)

def show_user(identificador):
    for user in Lista_usuarios:
        if user['ID'] == identificador:
            print(user)
        else:
            print("No existe usuario con ese ID")

def edit_user(identificador):
    indice=0
    for user in Lista_usuarios:
        if user['ID'] == identificador:
            valido = True

            while(valido):
                nombre=input("Ingresa tu nombre: ")
                cont=0
                for letra in nombre:
                    cont=cont+1
                if cont<5:
                    print("la longitud deber ser mayor a 4, ingrese nuevamente")
                elif cont>50:
                    print("la longitud debe ser menor a 50, ingrese nuevamente")
                else:
                    valido = False

            valido = True

            while(valido):
                apellido=input("Ingresa tu apellido: ")
                cont=0
                for letra in apellido:
                    cont=cont+1
                if cont<5:
                    print("la longitud deber ser mayor a 4, ingrese nuevamente")
                elif cont>50:
                    print("la longitud debe ser menor a 50, ingrese nuevamente")
                else:
                    valido = False

            valido = True

            while(valido):
                telefono=int(input("Ingresa tu número de teléfono: "))
                if telefono%10 != 0:
                    print("El número de teléfono debe tener 10 dígitos, ingrese nuevamente")
                else:
                    valido = False

            valido = True

            while(valido):
                email=input("Ingresa tu correo electrónico: ")
                cont=0
                for letra in email:
                    cont=cont+1
                if cont<5:
                    print("la longitud deber ser mayor a 4, ingrese nuevamente")
                elif cont>50:
                    print("la longitud debe ser menor a 50, ingrese nuevamente")
                else:
                    valido = False

            Lista_usuarios[indice]['nombre']= nombre
            Lista_usuarios[indice]['apellido']= apellido
            Lista_usuarios[indice]['telefono']= telefono
            Lista_usuarios[indice]['email']= email

        else:
            print("No existe usuario con ese ID")
        indice+=1

def list_users():
    if len(Lista_usuarios) != 0:
        for user in Lista_usuarios:
            print(user['ID'])
    else:
        print("No hay usuarios registrados")

def delete_user(identificador):
    indice=0
    for user in Lista_usuarios:
        if user['ID'] == identificador:
            Lista_usuarios.remove(indice)
        indice+=1

opcion='Ingresar'
ID_usuario=0

while(opcion!='S'):

    opcion= input("Eliga una opción: \n- Agregar usuario (A) \n- Listar usuarios (L) \n- Ver usuario (V) \n- Editar usuario (E) \n- Salir (S)" )

    if opcion == 'A':
        ID_usuario+=1
        new_user(ID_usuario)

    elif opcion == 'L':
        list_users()

    elif opcion == 'V':
        identificador= int(input("Ingrese ID del usuario:"))
        show_user(identificador)

    elif opcion == 'E':
        identificador= int(input("Ingrese ID del usuario:"))
        edit_user(identificador)

    elif opcion == 'B':
        identificador= int(input("Ingrese ID del usuario:"))
        delete_user(identificador)

    elif opcion == 'S':
        print('Gracias por utilizar nuestro sistema')

    else:
        print('Opción inexistente')