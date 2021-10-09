

#-------------------------------FUNCIONES-----------------------------


def Mostrar_Vacunas():
    print('LAS VACUNAS DISPONIBLES SON:')
    for vacuna in vacunas:
        print('++++++++++++++++++')
        print(f'vacuna N°:{vacunas.index(vacuna) + 1}')
        print(f' nombre:{vacuna["nombre"]} \n cantidad de dosis a aplicar:{vacuna["cantidad_de_dosis"]} \n periodo de aplicacion:{vacuna["intervalo"]} \n edad minima:{vacuna["edad_minima"]}')
        print('++++++++++++++++++')



def Mostar_Personas():
    print('LAS PERSONAS REGISTRADAS SON:')
    for persona in personas:
        print('*' * 30)
        print(f' persona N°:{personas.index(persona)+1}')
        print(f' nombre:{persona["nombre"]}\n Apellido:{persona["apellido"]}\n D.N.i:{persona["dni"]}\n Domicilio:{persona["domicilio"]}')
        print('*' * 30)


def Buscar_vacunado():
 x=input('ingrese el DNI: ')
 for i in registro:
    if x == i[0]['dni']:
        print('='*30)
        print(f'Apellido:{i[0]["apellido"]} \n Nombre:{i[0]["nombre"]} \n D.N.I:{i[0]["dni"]} \n Vacuna aplicada:{i[1]["nombre"]}\n Cantidad de dosis: {i[2]} \n fecha de inmunizacion:{i[3]}')
        print('=' * 30)
        print()



def Mostrar_Registro_1a_dosis():
 for registrado in registro:
    if registrado[2] == 1:
        print('=' * 30)
        print(f'Apellido:{registrado[0]["apellido"]} \n Nombre:{registrado[0]["nombre"]} \n D.N.I:{registrado[0]["dni"]} \n Vacuna aplicada:{registrado[1]["nombre"]} \n fecha de inmunizacion:{registrado[3]}')
        print('=' * 30)

def Mostrar_Registro_2a_dosis():
 for registrad in registro:
    if registrad[2] == 2 :
        print('=' * 30)
        print(f'Apellido:{registrad[0]["apellido"]} \n Nombre:{registrad[0]["nombre"]} \n D.N.I:{registrad[0]["dni"]} \n Vacuna aplicada:{registrad[1]["nombre"]} \n fecha de inmunizacion:{registrad[3]}')
        print('=' * 30)


def Crear_Persona():
    new_nombre=input('ingrese el nuevo nombre:')
    new_apellido=input('ingrese el nuevo apellido: ')
    new_dni=input('ingrese el nuevo D.N.I: ')
    new_direccion=input('ingrse la nueva direccion: ')
    personas.append({'nombre':new_nombre,'apellido':new_apellido,'dni':new_dni,'domicilio':new_direccion})




def Mostrar_Registro():
    print('TODOS LOS REGISTRADOS SON:')
    for registrado in registro:
            print('=' * 30)
            print(f' Apellido:{registrado[0]["apellido"]} \n Nombre: {registrado[0]["nombre"]} \n D.N.I: {registrado[0]["dni"]} \n Vacuna aplicada: {registrado[1]["nombre"]}\n numero de dosis: {registrado[2]} \n fecha de inmunizacion: {registrado[3]}')
            print('=' * 30)




def Eliminar_Presona():
    Mostar_Personas()
    Rta=input('ingrese el DNI a eliminar: ')
    for pers in personas:
        if Rta==pers["dni"]:
            print(f'Se elimino a {Rta}')
            personas.pop(personas.index(pers))

def Editar_Persona():
    Mostar_Personas()
    person = input('ingrese el DNI de la persona:')
    for registrado in personas:
     if person == registrado["dni"]:
        print('¿QUE DATO DESEA CAMBIAR?')
        print()
        print('1 --- NOMBRE ')
        print('2 --- APELLIDO ')
        print('3 --- D.N.I ')
        print('4 --- DIRECCION ')
        Rta=input('ingrese el N°: ')
        if Rta == '1':
         registrado["nombre"] = input('ingrese el nombre: ')
        elif Rta == '2':
            registrado["apellido"] = input('ingrese el apellido:')
        elif Rta == '3':
            registrado["dni"] = input('ingrese el D.N.I: ')
        elif Rta == '4':
           registrado["domicilio"] = input('ingrse la direccion: ')
     else:
         print(f'no se encontro a la persona {person} ')




def Crear_Registro_New():
    print('seleccione el DNI de la persona a vacunar')
    Mostar_Personas()
    persoN=input('ingrese el DNI: ')
    for pers in personas:
        if persoN==pers["dni"]:
            print(f'Se agrega a {pers}')
    print('|'*30)
    print('ingrese el N° de vacuna a colocar')
    Mostrar_Vacunas()
    vacN = input('ingrese el N°: ')
    for vacu in vacunas:
        if vacN == vacunas.index(vacu):
            print(f'Se vacuna con: {vacu}')

    dosisN=int(input('N° de dosis: '))
    fecha_dosis=input('Fecha del dia:')

    registro.append([pers,vacu,dosisN,fecha_dosis])


''' ----FIJATE EL EJERCICIO DE ELIMINAR POR INDEX DE LA CLACE DE MARCELO,HACE QUE SOLO SE LECCIONE EL INDEX
    Y LO COLOCAS CON APPEND([]) EN REGISTRO...
    CORDATE QUE TENES QUE HACER EDITABLE LOS DATOS DE LAS PERSONAS(ESO TAMBIEN ESTA EN LA CLASE DE MARCELO)
    -----'''



'''------------------------DATOS--------------------------------'''


vacunas=[
    {
     'nombre':'sputnik V',
     'cantidad_de_dosis':2,
     'intervalo': 21,
     'edad_minima': 18
    },

    {
     'nombre':'Covishield',
     'cantidad_de_dosis':2,
     'intervalo': 56,
     'edad_minima': 18
     },

    {
     'nombre': 'Sinopharm',
     'cantidad_de_dosis': 2,
     'intervalo': 21,
     'edad_minima': 18
    },
    {
     'nombre': 'AstraZeneca',
     'cantidad_de_dosis': 2,
     'intervalo': 56,
     'edad_minima': 18
    },

]
personas=[
    {'nombre':'Ignacio','apellido':'Gomez','dni':'21323232','domicilio':'Madariaga 1900'},
    {'nombre':'Maria','apellido':'Palma','dni':'35465454','domicilio':'Rivadavia 1225'},
    {'nombre':'Miguel','apellido':'Gonzalez','dni':'43545455','domicilio':'Colon s/n'}
]



registro=[
    {'persona':personas[1],'vacuna':vacunas[0],'dosis':1,'fecha':'12/03/2021'},
    [personas[0],vacunas[2],1,'01/01/2021'],
    [personas[2],vacunas[1],1,'12/05/2021'],
    [personas[1],vacunas[0],2,'20/06/2021']
]

#-------------------INICIO DEL PROGRAMA------------------------
print('-------------------REGISTROS COVID_19--------------------')
print()
while True :

    print(' 1 --- ver los tipos de vacunas disponibles')
    print(' 2 --- ver datos de personas')
    print(' 3 --- eliminar persona ')
    print(' 4 --- cambiar datos de una persona ')
    print(' 5 --- ingresar una nueva persona')
    print(' 6 --- ver personas vacunadas con primera dosis')
    print(' 7 --- ver personas vacunadas con segunda dosis')
    print(' 8 --- ver el listado de vacunados completo')
    print(' 9 --- buscar un vacunado')
    print(' 10 --- registrar vacunado ')
    print()
    print(' 11 --- salir ')
    print('-'*30)


    respuesta = input('ingrese el número de accion que desea:')
    if respuesta == '1':
        Mostrar_Vacunas()
    elif respuesta == '2':
        Mostar_Personas()
    elif respuesta == '3':
        Eliminar_Presona()
    elif respuesta == '4':
        Editar_Persona()
    elif respuesta == '5':
        Crear_Persona()
    elif respuesta == '6':
        Mostrar_Registro_1a_dosis()
    elif respuesta == '7':
        Mostrar_Registro_2a_dosis()
    elif respuesta == '8':
        Mostrar_Registro()
    elif respuesta == '9':
        Buscar_vacunado()
    elif respuesta == '10':
        Crear_Registro_New()

    else:
        print('MUCHAS GRACIAS!!!')
        break


#------------------------------FIN, CREO--------------------------------