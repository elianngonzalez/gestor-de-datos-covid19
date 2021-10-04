
#-------------no terminado-----------------  
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
#date time para hacer un timestamp
#import datetime
import pandas as pd
import sqlite3

con = sqlite3.connect("DB\\vacunas")
app= Flask(__name__)

#configuraciones
app.secret_key = "mysecretkey"


#-------------------------------FUNCIONES-----------------------------


def Mostrar_Vacunas():
    df2=pd.read_sql_query('SELECT nombre, dosis ,intervalo ,edad_min FROM vacunas',con)
    print('LAS VACUNAS DISPONIBLES SON:')
    print('++++++++++++++++++')
    print(df2)
    print('++++++++++++++++++')


def Buscar_vacunado():
    x=input('ingrese el DNI: ')
    datos=con.execute('SELECT nombre, dni, vacuna as vacuna_aplicada, dosis as numero_de_dosis, fecha_vacunacion FROM personas inner join registros_vac on persona.id=registros_vac.id inner join vacuna on vacuna.id=registros_vac.id where id =%s',(x))
    #datos.fetchone['dni']
    print('=' * 30)   
    print(datos)    
    print('=' * 30)
    print()


def Mostar_Personas():
    dfpersonas = pd.read_sql_query('SELECT nombre, apellido,dni,domicilio, fecha_nac AS nacido_en FROM personas order by nombre', con)
    print('LAS PERSONAS REGISTRADAS SON:')
    print('*' * 30)
    print()
    print(dfpersonas.head())
    print()
    print('*' * 30)


def Mostrar_Registro_1a_dosis():
    datos=con.execute('SELECT nombre, dni, vacuna as vacuna_aplicada, dosis as numero_de_dosis, fecha_vacunacion FROM personas inner join registros_vac on persona.id=registros_vac.id inner join vacuna on vacuna.id=registros_vac.id where dosis = 1')
    print('=' * 30)
    print(datos)
    print('=' * 30)

def Mostrar_Registro_2a_dosis():
    datos=con.execute('SELECT nombre, dni, vacuna as vacuna_aplicada, dosis as numero_de_dosis, fecha_vacunacion FROM personas inner join registros_vac on persona.id=registros_vac.id inner join vacuna on vacuna.id=registros_vac.id where dosis = 2')
    print('=' * 30)
    print(datos)
    print('=' * 30)

#esto se hace con un formulario de html
def Crear_Persona():
    new_nombre=input('ingrese el nuevo nombre:')
    new_apellido=input('ingrese el nuevo apellido: ')
    new_dni=input('ingrese el nuevo D.N.I: ')
    new_direccion=input('ingrse la nueva direccion: ')
    #no completo
    insert=pd.read_sql_query('INSERT INTO personas ( id,nombre,apellido,dni,domicilio,fecha_nac,telefono,fecha_creacion) VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);')
    
    
    #personas.append([new_nombre,new_apellido,new_dni,new_direccion])


def Mostrar_Registro():
    print('TODOS LOS REGISTRADOS SON:')
    for registrado in registro:
        print('=' * 30)
        print(f'Apellido:{registrado[0][1]} \n Nombre:{registrado[0][0]} \n D.N.I:{registrado[0][2]} \n Vacuna aplicada:{registrado[1][0]} \n N° de dosis:{registrado[2]} \n fecha de inmunizacion:{registrado[3]} ')
        print('=' * 30)


def Eliminar_Persona():
    Mostar_Personas()
    Rta=input('ingrese el DNI a eliminar: ')
    for pers in personas:
        if Rta==pers[2]:
            print(f'Se elimino a {Rta}')
            personas.pop(personas.index(pers))
        else:
            print(f'no se encontro a {Rta} ')

def Editar_Persona():
    Mostar_Personas()
    person = input('ingrese el DNI de la persona:')
    for registrado in personas:
        if person == registrado[2]:
            print('¿QUE DATO DESEA CAMBIAR?')
            print()
            print('1 --- NOMBRE ')
            print('2 --- APELLIDO ')
            print('3 --- D.N.I ')
            print('4 --- DIRECCION ')
            Rta=input('ingrese el N°: ')
            if Rta == '1':
                registrado[0] = input('ingrese el nombre: ')
            elif Rta == '2':
                registrado[1] = input('ingrese el apellido:')
            elif Rta == '3':
                registrado[2] = input('ingrese el D.N.I: ')
            elif Rta == '4':
                registrado[3] = input('ingrse la direccion')
            else:
                print(f'no se encontro a la persona {person} ')






def Crear_Registro_New():
    print('seleccione el DNI de la persona a vacunar')
    Mostar_Personas()
    persoN=input('ingrese el DNI: ')
    for pers in personas:
        if persoN==pers[2]:
            print(f'Se agrega a {pers[0][0]}')
    print('|'*30)
    print('ingrese el N° de vacuna a colocar')
    Mostrar_Vacunas()
    vacN = int(input('ingrese el N°: '))-1
    for vacu in vacunas:
        if  vacN-1 == vacunas.index(vacu):
            print(f'Se vacuna con: {vacu[0]}')
            dosisN = int(input('N° de dosis: '))
            fecha_dosis = input('Fecha del dia:')
            registro.append([pers, vacu, dosisN, fecha_dosis])
        elif vacN-1 !=  vacunas.index(vacu) :
            print('no puede colocarse una vacuna diferente')





''' ----FIJATE EL EJERCICIO DE ELIMINAR POR INDEX DE LA CLACE DE MARCELO,HACE QUE SOLO SE LECCIONE EL INDEX
    Y LO COLOCAS CON APPEND([]) EN REGISTRO...
    CORDATE QUE TENES QUE HACER EDITABLE LOS DATOS DE LAS PERSONAS(ESO TAMBIEN ESTA EN LA CLASE DE MARCELO)
    -----'''



'''------------------------DATOS--------------------------------'''

'''vacunas=[
    ['sputnik V',2,21,18],
    ['Covishield',2,56,18],
    ['Sinopharm', 2,21,18],
    ['AstraZeneca', 2, 56,18]
]
personas=[
    ['Ignacio','Gomez','21323232','Madariaga 1900'],
    ['Maria','Palma','35465454','Rivadavia 1225'],
    ['Miguel', 'Gonzalez', '43545455', 'Colon s/n']
]

registro=[
    [personas[1],vacunas[0],1,'12/06/2021'],
    [personas[0],vacunas[2],1,'01/05/2021'],
    [personas[2],vacunas[1],1,'12/05/2021'],
    [personas[1],vacunas[0],2,'20/06/2021']
]'''

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
    print(' 9 --- buscar vacunado ')
    print(' 10 --- registrar vacunado ')
    print()
    print(' 11 --- salir ')
    print('-'*30)

    respuesta = input('ingrese el número de accion que desea:')
    if respuesta == '1':
        Mostrar_Vacunas()
    elif respuesta == '2':
        Mostar_Personas()
    else:
        print('MUCHAS GRACIAS!!!')
        break
    '''
    elif respuesta == '3':
        Eliminar_Persona()
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
'''
con.close()


#------------------------------FIN, CREO--------------------------------




'''bdef Crear_Registro_New():
    print('seleccione el DNI de la persona a vacunar')
    Mostar_Personas()
    persoN=input('ingrese el DNI: ')
    for pers in personas:
        if persoN==pers[2]:
            print(f'Se agrega a {pers[0]} {pers[1]}')
    print('|'*30)
    print('ingrese el N° de vacuna a colocar')
    Mostrar_Vacunas()
    vacN = int(input('ingrese el N°: '))-1
    for vacu in vacunas:
        if vacN == vacunas.index(vacu):
            print(f'Se vacuna con: {vacu[0]}')

    dosisN=int(input('N° de dosis: '))
    fecha_dosis=input('Fecha del dia:')
    registro.append([pers,vacu,dosisN,fecha_dosis])

    '''