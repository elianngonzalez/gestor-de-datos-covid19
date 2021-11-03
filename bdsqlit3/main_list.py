
#-------------no terminado-----------------  
from flask import Flask, render_template, request, redirect, url_for, flash, make_response 
#date time para hacer un timestamp
#import datetime
#import pandas as pd
import sqlite3



con = sqlite3.connect("DB\\vacunas")
app= Flask(__name__)

#configuraciones
app.secret_key = "mysecretkey"


#-------------------------------FUNCIONES y RUTAS-----------------------------
def get_db_biblioteca():
    con = sqlite3.connect("DB/vacunas")
    con.row_factory = sqlite3.Row
    return con

def get_db():
    con = sqlite3.connect("DB/vacunas")
    return con


# routes
@app.route('/')
def deciciones():
    return render_template('index.html')
    #return render_template('login/index_login.html')


#-----------------------------VACUNAS-----------------------------------------
@app.route('/vacunas')
def Vacunas():
    con = get_db()
    data=con.execute('SELECT id, nombre, dosis,edad_min,estado_id,intervalo FROM vacunas')
    est=con.execute('SELECT * FROM estado ')
    print(est)
    return render_template('vacunas/index.html', vacunas = data, estados=est)

@app.route('/add_vacuna', methods=['POST'])
def add_vacuna():
    if request.method == 'POST':
        nombre = request.form['fullname']
        dosis = request.form['dosis']
        intervalo = request.form['intervalo']
        edad_minima = request.form['edad_minima']
        estado = request.form['estado']
        con = sqlite3.connect("DB/vacunas")
        con.execute("INSERT INTO vacunas (nombre, dosis ,intervalo,edad_min,estado_id) VALUES (?,?,?,?,?)", (nombre,dosis,intervalo,edad_minima,estado))
        con.commit()
        flash('Vacuna agregada correctamente')
        return redirect(url_for('Vacunas'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_vacuna(id):
    con = sqlite3.connect("DB/vacunas")
    cur=con.cursor() 
    cur.execute('SELECT * FROM vacunas WHERE id = ?', (id))
    data=cur.fetchall()
    cur.execute('SELECT * FROM estado WHERE id')
    est=cur.fetchall()
    cur.close()
    print(data)
    return render_template('vacunas/edit-vacuna.html', vacuna = data[0], estados=est)

@app.route('/update/<id>', methods=['POST'])
def update_vacuna(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        dosis = request.form['dosis']
        intervalo = request.form['intervalo'] 
        edad = request.form['edad_minima']
        estado = request.form['estado']   
        con = sqlite3.connect("DB/vacunas")
        cur = con.cursor()
        cur.execute("UPDATE vacunas SET nombre = ?,dosis = ?,intervalo = ?, edad_min=? , estado_id=? WHERE id = ?", (fullname, dosis, intervalo,edad,estado, id))
        con.commit()
        flash('Vacuna editada correctamente')
        return redirect(url_for('Vacunas'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    con = sqlite3.connect("DB/vacunas")
    cur = con.cursor()
    cur.execute('DELETE FROM vacunas WHERE id = {0}'.format(id))
    con.commit()
    flash('Vacuna Removida Correctamente')
    return redirect(url_for('Vacunas'))

#------------------PERSONAS----------------------

@app.route('/personas')
def IndexPersonas():
    con = sqlite3.connect("DB/vacunas")
    data=con.execute('SELECT id,nombre,apellido,dni,domicilio,fecha_nac,telefono FROM personas ')
    return render_template('personas/index-personas.html', personas = data)

@app.route('/consulta', methods = ['POST','GET'])
def indexConsulta():
    filtro1 = [request.form.get('bus')]
    #input error none
    print(filtro1)
    con=get_db()
    cur=con.cursor()
    dato=cur.execute("SELECT id,nombre,apellido,dni,domicilio,fecha_nac,telefono FROM personas WHERE nombre LIKE '{0}%'".format(filtro1)) 
    return render_template('personas/index-personas copy.html', personas = dato)

@app.route('/consulta2', methods = ['POST'])
def indexConsulta2():
    print(request.form)
    filtro = "where 1=1 "
    valores = []
    filtro_nombre =  request.form['bus']
    if filtro_nombre != "":
        filtro = filtro +  " and nombre LIKE '%'||?||'%'" 
        valores.append(filtro_nombre)


    filtro_apellido =  request.form['bus_apell']
    if filtro_apellido != "":
        filtro = filtro +  " and apellido LIKE '%'||?||'%'" 
        valores.append(filtro_apellido)
    
    
    print(filtro)
    con=get_db()
    cur=con.cursor()
    dato=cur.execute("SELECT id,nombre,apellido,dni,domicilio,fecha_nac,telefono FROM personas "+filtro,(valores)) 
    return render_template('personas/index-personas.html', personas = dato)


@app.route('/add_persona', methods = ['POST'])
def add_Personas():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        domicilio = request.form['domicilio']
        fech_nac = request.form['fecha']
        telef = request.form['telefono']
        con = sqlite3.connect("DB/vacunas")
        con.execute("INSERT INTO personas (nombre,apellido,dni,domicilio,fecha_nac,telefono) VALUES (?,?,?,?,?,?)", (nombre,apellido,dni,domicilio,fech_nac,telef))
        con.commit()
        flash('Persona agregada correctamente')
        return redirect(url_for('IndexPersonas'))

@app.route('/edit_persona/<id>', methods = ['POST', 'GET'])
def get_Personas(id):
    con = sqlite3.connect("DB/vacunas")
    cur=con.cursor() 
    cur.execute('SELECT * FROM personas WHERE id = ?', (id))
    data=cur.fetchall()
    cur.close()
    print(data)
    return render_template('personas/edit-personas.html', vacuna = data[0])


@app.route('/update_persona/<id>', methods = ['POST'])
def update_Personas(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        domicilio = request.form['domicilio']
        fech_nac = request.form['fecha_d_nac']
        telefono = request.form['telefono']   
        con = sqlite3.connect("DB/vacunas")
        cur = con.cursor()
        cur.execute("UPDATE personas SET nombre=?,apellido=?,dni=?,domicilio=?,fecha_nac=?,telefono=? WHERE id = ?", (nombre,apellido,dni,domicilio,fech_nac,telefono, id))
        con.commit()
        flash('Vacuna editada correctamente')
        return redirect(url_for('IndexPersonas'))


@app.route('/delete_persona/<string:id>', methods = ['POST', 'GET'])
def delete_Personas(id):
    con = sqlite3.connect("DB/vacunas")
    cur = con.cursor()
    cur.execute('DELETE FROM personas WHERE id = {0}'.format(id))
    con.commit()
    flash('Persona Removida Correctamente')
    return redirect(url_for('IndexPersonas'))


#-------------------------------------------REGISTROS----------------------------

@app.route('/registros' , methods = ['POST','GET'])
def IndexRegistros():
    con = get_db()
    data=con.execute('select registros_vac.id, registros_vac.fecha_vacunacion, registros_vac.dosis ,personas.nombre ,personas.apellido, vacunas.nombre ,vacunatorio_id, lote FROM ((registros_vac INNER JOIN personas on registros_vac.persona_id=personas.id) INNER JOIN vacunas on vacunas.id=registros_vac.vacuna_id)')
    est=con.execute('SELECT * FROM estado WHERE id')
    pers = con.execute('SELECT id,nombre , apellido FROM personas') 
    #fitrar registros por consulta de fecha
    if request.method == 'POST':
        print(request.form)
        filtro = "where 1=1 "
        valores = []
        filtro_nombre =  request.form['bus']
        if filtro_nombre != "":
            filtro = filtro +  " and personas.nombre LIKE '%'||?||'%'" 
            valores.append(filtro_nombre)


        filtro_apellido =  request.form['bus_apell']
        if filtro_apellido != "":
            filtro = filtro +  " and personas.apellido LIKE '%'||?||'%'" 
            valores.append(filtro_apellido)


        valor_fecha = []
        filtro_fecha =  " and registros_vac.fecha_vacunacion "
        
        fecha_desde = request.form['fecha_desde']
        fecha_hasta = request.form['fecha_hasta']
        if fecha_desde != "" and fecha_hasta != "":
            filtro_fecha = filtro_fecha + " BETWEEN ? AND ? "
            valores.append(fecha_desde)
            valores.append(fecha_hasta)


        
        
        print(valor_fecha , valores)
        cur=con.cursor()
        dato=cur.execute("select registros_vac.id, registros_vac.fecha_vacunacion, registros_vac.dosis ,personas.nombre ,personas.apellido, vacunas.nombre ,vacunatorio_id, lote FROM ((registros_vac INNER JOIN personas on registros_vac.persona_id=personas.id) INNER JOIN vacunas on vacunas.id=registros_vac.vacuna_id) "+ filtro + filtro_fecha,(valores)) 
        print(dato)
        return render_template('registros/index.html', registros = dato)
    
    return render_template('registros/index.html', registros = data , estados=est , personas=pers)


@app.route('/group_by', methods = ['POST' ,'GET'])
def By_Grupos():
    con = get_db_biblioteca()
    dato = con.execute('SELECT nombre_vacunatorio , count(nombre) as inmunizados FROM registros_completos GROUP by nombre')
    pass



@app.route('/add_registro', methods = ['POST'])
def add_registro():
    #mostar la tabla de personas, hacer un search para buscarla
    #si no se encuentra que me permita realizar un alta de la persona  
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        domicilio = request.form['domicilio']
        fech_nac = request.form['fecha']
        telef = request.form['telefono']
        con = sqlite3.connect("DB/vacunas")
        con.execute("INSERT INTO personas (nombre,apellido,dni,domicilio,fecha_nac,telefono) VALUES (?,?,?,?,?,?)", (nombre,apellido,dni,domicilio,fech_nac,telef))
        con.commit()
        flash('Persona agregada correctamente')
        return redirect(url_for('IndexRegistros'))

@app.route('/edit_registro/<id>', methods = ['POST', 'GET'])
def get_registro(id):
    con = sqlite3.connect("DB/vacunas")
    cur=con.cursor() 
    cur.execute('SELECT * FROM personas WHERE id = ?', (id))
    data=cur.fetchall()
    cur.close()
    print(data)
    return render_template('personas/edit-personas.html', vacuna = data[0])


@app.route('/update_registro/<id>', methods = ['POST'])
def update_registro(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        domicilio = request.form['domicilio']
        fech_nac = request.form['fecha_d_nac']
        telefono = request.form['telefono']   
        con = sqlite3.connect("DB/vacunas")
        cur = con.cursor()
        cur.execute("UPDATE personas SET nombre=?,apellido=?,dni=?,domicilio=?,fecha_nac=?,telefono=? WHERE id = ?", (nombre,apellido,dni,domicilio,fech_nac,telefono, id))
        con.commit()
        flash('Vacuna editada correctamente')
        return redirect(url_for('IndexPersonas'))


@app.route('/delete_persona/<string:id>', methods = ['POST', 'GET'])
def delete_registros(id):
    con = sqlite3.connect("DB/vacunas")
    cur = con.cursor()
    cur.execute('DELETE FROM personas WHERE id = {0}'.format(id))
    con.commit()
    flash('Persona Removida Correctamente')
    return redirect(url_for('IndexPersonas'))

#--------------------------------------------PRUEVAS---------------------------SECIONES-------------


#COoKIES

@app.route('/setcookie', methods = ['POST'])
def set_cookie():
    user = request.form.get('emailuser')
    
    resp = make_response(render_template('login/cookie.html'))
    
    resp.set_cookie('userID', user)
    
    print('resp:', resp)
    
    return resp

@app.route('/getcookie')
def get_cookie():
    name = request.cookies.get('userID')
    if (name == None):
        return 'no hay Cookie de usuario'
    else:
        return '<h1>BIENVENIDO ' + name + '</h1>'



# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)

