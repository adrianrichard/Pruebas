##Vaya, ya llegamos al reto número 3 de la semana, y para este tercer reto lo que haremos
##será añadir 2 nuevas funcionalidades a nuestro programa de registro de usuarios.
##Estas funcionalidades son las siguientes##
##.1.- Siempre que se registre un nuevo usuario de forma exitosa generaremos un identificador único para este registro/usuario.
##Te recomiendo sea un ID numérico auto incremental, que comience en 1 hasta N.
##Sin embargo siéntete libre elegir el formato o tipo que tú desees.
##2.- Todos estos nuevos identificadores deberán almacenarse en un listado que será impreso en consola
##cuando todos los registros se hayan creado. Esto de tal forma que el usuario pueda conocer y tenga certeza
##que las operaciones, en efecto, se realizaron de forma exitosa.
##Con estas 2 nuevas funcionalidades es probable te intuyas como iremos finalizando nuestro programa para el quinto día.

identificadores=[]

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

    ID=usuario+1

    identificadores.append(ID)

print(identificadores)
