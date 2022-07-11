from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

if __name__ == "__main__": app.run()

#MySQL Connection

app.config['MYSQL_HOST'] = '179.61.12.108'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'directo1_Santiago'
app.config['MYSQL_PASSWORD'] = 'directoresfunerarios1'
app.config['MYSQL_DB'] = 'directo1_funeraria'
mysql = MySQL(app)

# MySQL Session Settings

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():    
    return render_template("index.html", user=user)

user= ""

###################################### Renders P叩ginas #########

#####LOGIN#####

@app.route('/login')
def DisplayLogin():
    return render_template("login.html")

@app.route('/check_login', methods=['POST'])
def CheckLogin():
    
    if request.method == "POST":
        global user
        user = request.form['user']
        password = request.form['password']
        cur = mysql.connection.cursor()
        check = cur.execute(""" SELECT 1 FROM credenciales WHERE Usuario = %s AND Contrasena = %s""",(user, password))
        if check == 1:
            print("Usuario: " + user + "check " + str(check))
            flash ("Bienvenido " + user + " check " + str(check))
            check = 0
            return redirect(url_for('DisplayLogin'))
    return print("Usuario o contrasena incorrectos")
    
###################### LOGOUT #############################

@app.route("/logout")
def Logout():
    global user
    user = ""
    return redirect(url_for('Index'))

####################### CONOZCANOS ############################

@app.route('/conozcanos')
def DisplayConozcanos():
    return render_template("conozcanos.html")

#SERVICIOS

@app.route('/servicios')
def DisplayServicios():    
    return render_template("servicios.html")

#CUBRIMIENTO

@app.route('/cubrimiento')
def DisplayCubrimiento():    
    return render_template("conozcanos.html")

#DBADMIN

@app.route('/dbadmin')
def DisplayDbAdmin():
    return render_template('dbadmin.html')
    
##########################################################################

#TABLA_CONDOLENCIAS

@app.route('/tabla_condolencias')
def DisplayCo():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tabla_condolencias')
    data = cur.fetchall()
    return render_template('tabla_condolencias.html', contacts = data)
    

        


##########################################################################

#TABLA_EPITAFIOS

@app.route('/tabla_epitafios')
def DisplayEp():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tabla_epitafios')
    data = cur.fetchall()

    return render_template('tabla_epitafios.html', contacts= data)

#########################################################################

#TABLA_VINCULACION

@app.route('/tabla_vinculacion')
def DisplayVi():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tabla_vinculacion')
    data = cur.fetchall()

    return render_template('tabla_vinculacion.html', contacts= data)

#VINCULACION

@app.route('/vinculacion')
def DisplayVinculacion():    
    return render_template("vinculacion.html")


@app.route('/add_vinculacion', methods=['POST'])
def add_vinculacion():
    if request.method == 'POST':
        vnit = request.form['vnit']
        vrazon_social = request.form['vrazonsocial']
        vdireccion = request.form['vdireccion']
        vtelefono = request.form['vtelefono']
        vcorreo = request.form['vcorreo']
        vciudad = request.form['vciudad']
        vdpto = request.form['vdpto']
        vpais = request.form['vpais']
        vurl = request.form['vurl']
        vrep_papellido = request.form['vrep_papellido']
        vrep_sapellido = request.form['vrep_sapellido']
        vrep_nombres = request.form['vrep_nombres']
        vrep_documento = request.form['vrep_documento']
        vrep_celular = request.form['vrep_celular']
        vrep_correo = request.form['vrep_correo']
        vcodigo_contrato = request.form['vcodigo_contrato']
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO tabla_vinculacion 
        (vnit, 
        vrazon_social, 
        vdireccion, 
        vtelefono, 
        vcorreo, 
        vciudad, 
        vdpto, 
        vpais, 
        vurl, 
        vrep_papellido, 
        vrep_sapellido, 
        vrep_nombres, 
        vrep_documento,
        vrep_celular,
        vrep_correo,
        vcodigo_contrato) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
        vnit, vrazon_social, vdireccion, vtelefono, vcorreo, vciudad, vdpto, vpais, vurl, vrep_papellido, vrep_sapellido, vrep_nombres, vrep_documento, vrep_celular, vrep_correo, vcodigo_contrato))
        mysql.connection.commit()
        flash('Cliente A単adido Satisfactoriamente')
        return redirect(url_for('DisplayVi'))

@app.route('/edit-vinculacion/<id>')
def get_vinculacion(id):

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tabla_vinculacion WHERE vcodigo_contrato = {0}'.format(id))
    data = cur.fetchall()
    return render_template('edit-vinculacion.html', contact = data[0])

@app.route('/update_vinculacion/<id>', methods = {'POST'})
def update_vinculacion(id):
        
    if request.method == 'POST':
        vnit = request.form['vnit']
        vrazon_social = request.form['vrazon_social']
        vdireccion = request.form['vdireccion']
        vtelefono = request.form['vtelefono']
        vcorreo = request.form['vcorreo']
        vciudad = request.form['vciudad']
        vdpto = request.form['vdpto']
        vpais = request.form['vpais']
        vurl = request.form['vurl']
        vrep_papellido = request.form['vrep_papellido']
        vrep_sapellido = request.form['vrep_sapellido']
        vrep_nombres = request.form['vrep_nombres']
        vrep_documento = request.form['vrep_documento']
        vrep_celular = request.form['vrep_celular']
        vrep_correo = request.form['vrep_correo']
        vcodigo_contrato = request.form['vcodigo_contrato']              
        cur = mysql.connection.cursor() 
        cur.execute("""
        UPDATE tabla_vinculacion 
        SET vnit = %s, 
            vrazon_social = %s,
            vdireccion = %s,
            vtelefono = %s,
            vcorreo = %s,
            vciudad = %s,
            vdpto = %s,
            vpais = %s,
            vurl = %s,
            vrep_papellido = %s,
            vrep_sapellido = %s,
            vrep_nombres = %s,
            vrep_documento = %s,
            vrep_celular = %s,
            vrep_correo = %s, 
            vcodigo_contrato = %s           
        WHERE vcodigo_contrato = %s
        """, (vnit, vrazon_social, vdireccion, vtelefono, vcorreo, vciudad, vdpto, vpais, vurl, vrep_papellido, vrep_sapellido, vrep_nombres, vrep_documento, vrep_celular, vrep_correo, vcodigo_contrato, vcodigo_contrato))
        mysql.connection.commit()
        
        flash('Cliente Actualizado Satisfactoriamente')
        return redirect(url_for('DisplayVi'))

@app.route('/delete_vinculacion/<string:id>')
def delete_vinculacion(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tabla_vinculacion WHERE vnit = {0}'.format(id))
    mysql.connection.commit()
    flash('Cliente Eliminado Satisfactoriamente')
    return redirect(url_for('DisplayVi'))

#########################################################################

#TABLA_ETERNA

@app.route('/tabla_eterna')
def DisplayEt():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tabla_eterna')
    data = cur.fetchall()

    return render_template('tabla_eterna.html', contacts= data)

@app.route('/crear-eterna')
def CreateEt():
    return render_template('crear-eterna.html')


@app.route('/add_eterna', methods=['POST'])
def add_eterna():
    if request.method == 'POST':
        acodigo_cliente = request.form['acodigo_cliente']
        apapellido = request.form['apapellido']
        asapellido = request.form['asapellido']
        anombres = request.form['anombres']
        aid = request.form['aid']
        adir_velacion = request.form['adir_velacion']
        aciudad = request.form['aciudad']
        adpto = request.form['adpto']
        apais = request.form['apais']
        afechaora = request.form['afechaora']
        adirparroquia = request.form['adirparroquia']
        anombreparroquia = request.form['anombreparroquia']
        acementerio = request.form['acementerio']
        afecha_altas = request.form['afecha_altas']
        afecha_bajas = request.form['afecha_bajas']
        aestado = request.form['aestado']
        alocalizacion_tumba = request.form['alocalizacion_tumba']
        aciclodevida = request.form['aciclodevida']
        aactivar = request.form['aactivar']
        pie1 = request.form['pie1']
        pie2 = request.form['pie2']
        pie3 = request.form['pie3']
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO tabla_eterna 
        (acodigo_cliente, 
        apapellido, 
        asapellido, 
        anombres, 
        aid, 
        adir_velacion, 
        aciudad, 
        adpto, 
        apais, 
        afechaora, 
        adirparroquia, 
        anombreparroquia, 
        acementerio,
        afecha_altas,
        afecha_bajar,
        aestado,
        alocalizacion_tumba,
        aciclodevida,
        aactivar,
        pie1,
        pie2,
        pie3) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
        acodigo_cliente, apapellido, asapellido, anombres, aid, adir_velacion, aciudad, adpto, apais, afechaora, adirparroquia, anombreparroquia, acementerio, afecha_altas, afecha_bajas, aestado, alocalizacion_tumba, aciclodevida, aactivar, pie1, pie2, pie3))
        mysql.connection.commit()
        flash('Cliente A単adido Satisfactoriamente')
        return redirect(url_for('DisplayOb'))

@app.route('/edit-eterna/<id>')
def get_eterna(id):

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tabla_eterna WHERE acodigo_cliente = {0}'.format(id))
    data = cur.fetchall()
    return render_template('edit-eterna.html', contact = data[0])

@app.route('/update_eterna/<id>', methods = {'POST'})
def update_eterna(id):
    
    if request.method == 'POST':
        acodigo_cliente = request.form['acodigo_cliente']
        apapellido = request.form['apapellido']
        asapellido = request.form['asapellido']
        anombres = request.form['anombres']
        aid = request.form['aid']
        adir_velacion = request.form['adir_velacion']
        aciudad = request.form['aciudad']
        adpto = request.form['adpto']
        apais = request.form['apais']
        afechaora = request.form['afechaora']
        adirparroquia = request.form['adirparroquia']
        anombreparroquia = request.form['anombreparroquia']
        acementerio = request.form['acementerio']
        afecha_altas = request.form['afecha_altas']
        afecha_bajas = request.form['afecha_bajas']
        aestado = request.form['aestado']
        alocalizacion_tumba = request.form['alocalizacion_tumba']
        aciclodevida = request.form['aciclodevida']
        aactivar = request.form['aactivar']
        pie1 = request.form['pie1']
        pie2 = request.form['pie2']
        pie3 = request.form['pie3']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE tabla_eterna
        SET acodigo_cliente =%s,
            apapellido = %s,
            asapellido = %s,
            anombres = %s,
            aid = %s,
            adir_velacion = %s,
            aciudad = %s,
            adpto = %s,
            apais = %s,
            afechaora = %s,
            adirparroquia = %s,
            anombreparroquia = %s,
            acementerio = %s,
            afecha_altas = %s,
            afecha_bajas = %s,
            aestado = %s,
            alocalizacion_tumba = %s,
            aciclodevida = %s,
            aactivar = %s,
            pie1 = %s,
            pie2 = %s,
            pie3 = %s,
        WHERE id = %s
        """, (acodigo_cliente, apapellido, asapellido, anombres, aid, adir_velacion, aciudad, adpto, apais, afechaora, adirparroquia, anombreparroquia, acementerio, afecha_altas, afecha_bajas, aestado, alocalizacion_tumba, aciclodevida, aactivar, pie1, pie2, pie3, aid))
        mysql.connection.commit()
        flash('Cliente Actualizado Satisfactoriamente')
        return redirect(url_for('DisplayEt'))

@app.route('/delete_eterna/<string:id>')
def delete_eterna(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tabla_eterna WHERE acodigo_cliente = {0}'.format(id))
    mysql.connection.commit()
    flash('Cliente Eliminado Satisfactoriamente')
    return redirect(url_for('DisplayEt'))


##########################################################################

#TABLA_CLIENTES

@app.route('/clientes')
def DisplayCl():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM clientes')
    data = cur.fetchall()

    return render_template('clientes.html', contacts= data)

#######################################################################

#TABLA_OBITUARIOS

@app.route('/tabla_obituarios')
def DisplayOb():
    global user
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tabla_obituario')
    data = cur.fetchall()
    print ("Usuario: " + user)

    return render_template('tabla_obituarios.html', contacts= data, user=user)

@app.route('/crear-obituario')
def CreateOb():
    return render_template('crear-obituario.html')


@app.route('/add_obituario', methods=['POST'])
def add_obituario():
    if request.method == 'POST':
        ocodigo_cliente = request.form['ocodigo_cliente']
        opapellido = request.form['opapellido']
        osapellido = request.form['osapellido']
        onombres = request.form['onombres']
        oid = request.form['oid']
        odir_velacion = request.form['odir_velacion']
        ociudad = request.form['ociudad']
        odpto = request.form['odpto']
        opais = request.form['opais']
        ofechaora = request.form['ofechaora']
        odirparroquia = request.form['odirparroquia']
        ocementerio = request.form['ocementerio']
        oestado = request.form['oestado']
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO tabla_obituario 
        (ocodigo_cliente, 
        opapellido, 
        osapellido, 
        onombres, 
        oid, 
        odir_velacion, 
        ociudad, 
        odpto, 
        opais, 
        ofechaora, 
        odirparroquia, 
        ocementerio, 
        oestado) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
        ocodigo_cliente, opapellido, osapellido, onombres, oid, odir_velacion, ociudad, odpto, opais, ofechaora, odirparroquia, ocementerio, oestado))
        mysql.connection.commit()
        flash('Cliente A単adido Satisfactoriamente')
        return redirect(url_for('DisplayOb'))

@app.route('/edit-obituario/<id>')
def get_obituario(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tabla_obituario WHERE OCODIGO_CLIENTE = {0}'.format(id))
    data = cur.fetchall()
    return render_template('edit-obituario.html', contact = data[0])

@app.route('/update_obituario/<id>', methods = {'POST'})
def update_obituario(id):
    
    if request.method == 'POST':
        ocodigo_cliente = request.form['ocodigo_cliente']
        opapellido = request.form['opapellido']
        osapellido = request.form['osapellido']
        onombres = request.form['onombres']
        oid = request.form['oid']
        odir_velacion = request.form['odir_velacion']
        ociudad = request.form['ociudad']
        odpto = request.form['odpto']
        opais = request.form['opais']
        ofechaora = request.form['ofechaora']
        odirparroquia = request.form['odirparroquia']
        ocementerio = request.form['ocementerio']
        oestado = request.form['oestado']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE tabla_obituario
        SET ocodigo_cliente = %s,
            opapellido = %s,
            osapellido = %s,
            onombres = %s,
            oid = %s,
            odir_velacion = %s,
            ociudad = %s,
            odpto = %s,
            opais = %s,
            ofechaora = %s,
            odirparroquia = %s,
            ocementerio = %s,
            oestado = %s
        WHERE oid = %s
        """, (ocodigo_cliente, opapellido, osapellido, onombres, oid, odir_velacion, ociudad, odpto, opais, ofechaora, odirparroquia, ocementerio, oestado, oid))
        mysql.connection.commit()
        flash('Cliente Actualizado Satisfactoriamente')
        return redirect(url_for('DisplayOb'))

@app.route('/delete_obituario/<string:id>')
def delete_obituario(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tabla_obituario WHERE ocodigo_cliente = {0}'.format(id))
    mysql.connection.commit()
    flash('Cliente Eliminado Satisfactoriamente')
    return redirect(url_for('DisplayOb'))


#######################################################################

if __name__ == '__main__':
    app.run(port = 3000, debug = True)