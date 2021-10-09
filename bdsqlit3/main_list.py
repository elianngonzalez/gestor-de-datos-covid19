
#-------------no terminado-----------------  
from flask import Flask, render_template, request, redirect, url_for, flash
#date time para hacer un timestamp
#import datetime
import pandas as pd
import sqlite3



con = sqlite3.connect("DB\\vacunas")
app= Flask(__name__)

#configuraciones
app.secret_key = "mysecretkey"


#-------------------------------FUNCIONES y RUTAS-----------------------------


# routes
@app.route('/')
def deciciones():
    return render_template('index.html')

@app.route('/vacunas')
def Vacunas():
    con = sqlite3.connect("DB/vacunas")
    data=con.execute('SELECT id, nombre, dosis,edad_min,estado_id,intervalo FROM vacunas')
    est=con.execute('SELECT * FROM estado WHERE id')
    return render_template('vacunas/index.html', vacunas = data, estado=est)

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
    return render_template('vacunas/edit-contact.html', vacuna = data[0], estados=est)

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


@app.route('/add_persona', methods = ['POST'])
def add_Personas():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        domicilio = request.form['domicilio']
        fech_nac = request.form['fecha_d_nac']
        telefono = request.form['telefono']
        con = sqlite3.connect("DB/vacunas")
        con.execute("INSERT INTO personas (nombre,apellido,dni,domicilio,fecha_nac,telefono) VALUES ", (nombre,apellido,dni,domicilio,fech_nac,telefono))
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



# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)

