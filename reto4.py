## Ya nos encontramos en la recta final de nuestra semana, y lo que haremos ahora, cómo ya es costumbre, será añadir más funcionalidades a nuestro programa.
## Puntualmente 4 nuevas funcionalidades. Aquí van.
## 1.- Ahora todos los valores que representan a un usuario: Nombre, apellidos, número de teléfono y correo electrónico deberán almacenarse en un diccionario.
## 2.- Se añadirá la opción de poder listar el ID de todos los usuarios registrados hasta el momento.
## 3.- Se añadirá la opción de poder ver la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID
##     y a partir de este conocer la información registrada.
## 4.- Se añadirá la opción de poder editar la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID
##     y a partir de este el programa pedirá nuevamente los valores de un registro para actualizarlos.
## Estas 3 nuevas opciones deberán ser presentadas al usuario al comienzo del programa, esto con la finalidad que sea el usuario quien defina
## que quiere hacer justo ahora: añadir nuevos usuario, consultarlos o editarlos.
## De igual forma el programa tendrán una quinta opción que le permita la usuario finalizar el programa cuando él lo desee.
## Un Tip. Para estas nuevas opciones puedes presentarle a tu usuario un pequeño menú del cual pueda elegir.
## Por ejemplo opción A.-) registrar nuevos usuarios, opción B.-) listar usuarios, Opción C.-) Editar usuarios y así sucesivamente.

Lista_usuarios=[]

opcion='Ingresar'
usuario={}
ID_usuario=0

while(opcion!='S'):

    opcion= input("Eliga una opción: \n- Agregar usuario (A) \n- Listar usuarios (L) \n- Ver usuario (V) \n- Editar usuario (E) \n- Salir (S)" )

    if opcion == 'A':
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
            email=input("Ingresa tu aorreo electrónico: ")
            cont=0
            for letra in email:
                cont=cont+1
            if cont<5:
                print("la longitud deber ser mayor a 4, ingrese nuevamente")
            elif cont>50:
                print("la longitud debe ser menor a 50, ingrese nuevamente")
            else:
                valido = False
        ID_usuario+=1
        usuario={'ID':ID_usuario, 'nombre': nombre, 'apellido': apellido, 'telefono': telefono, 'email': email}
        Lista_usuarios.append(usuario)

    elif opcion == 'L':
        for user in Lista_usuarios:
            print(user['ID'])

    elif opcion == 'V':
        identificador= int(input("Ingrese ID del usuario:"))
        for user in Lista_usuarios:
            if user['ID'] == identificador:
                print(user)
            else:
                print("No existe usuario con ese ID")

    elif opcion == 'E':
        indice=0
        identificador= int(input("Ingrese ID del usuario:"))
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
                    email=input("Ingresa tu aorreo electrónico: ")
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

    elif opcion == 'S':
        print('Gracias por utilizar nuestro sistema')

    else:
        print('Opción inexistente')



##    for usuario in range(0, cantidad_usuarios):
##
##
##        valido = True
##
##        while(valido):
##            nombre=input("Ingresa tu nombre: ")
##            cont=0
##            for letra in nombre:
##                cont=cont+1
##            if cont<5:
##                print("la longitud deber ser mayor a 4, ingrese nuevamente")
##            elif cont>50:
##                print("la longitud debe ser menor a 50, ingrese nuevamente")
##            else:
##                valido = False
##
##        valido = True
##
##        while(valido):
##            apellido=input("Ingresa tu apellido: ")
##            cont=0
##            for letra in apellido:
##                cont=cont+1
##            if cont<5:
##                print("la longitud deber ser mayor a 4, ingrese nuevamente")
##            elif cont>50:
##                print("la longitud debe ser menor a 50, ingrese nuevamente")
##            else:
##                valido = False
##
##        valido = True
##
##        while(valido):
##            telefono=int(input("Ingresa tu número de teléfono: "))
##            if telefono%10 != 0:
##                print("El número de teléfono debe tener 10 dígitos, ingrese nuevamente")
##            else:
##                valido = False
##
##        valido = True
##
##        while(valido):
##            email=input("Ingresa tu aorreo electrónico: ")
##            cont=0
##            for letra in email:
##                cont=cont+1
##            if cont<5:
##                print("la longitud deber ser mayor a 4, ingrese nuevamente")
##            elif cont>50:
##                print("la longitud debe ser menor a 50, ingrese nuevamente")
##            else:
##                valido = False
##
##        nombre_completo = nombre + ' ' + apellido
##        print(nombre_completo, 'ha sido registrado correctamente. Recibirá un mensaje al correo electrónico', email)
##
##        ID=usuario+1
##
##        identificadores.append(ID)
##
##    print(identificadores)
