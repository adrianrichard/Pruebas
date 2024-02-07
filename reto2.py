##Para este segundo reto de la semana tu objetivo será incrementar el funcionamiento del programa del día de ayer.
##Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema.
##Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.
##Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.
##Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores:
##Nombre, apellidos, número de teléfono y correo electrónico.
##Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.
##Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50.
##Así mismo el número de teléfono será a 10 dígitos.
##Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.

cantidad_usuarios= int(input("¿Cuántos nuevos usuarios pretende registrar?: "))
for usuario in range(0, cantidad_usuarios):
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

    nombre_completo = nombre + ' ' + apellido
    print(nombre_completo, 'ha sido registrado correctamente. Recibirá un mensaje al correo electrónico', email)
