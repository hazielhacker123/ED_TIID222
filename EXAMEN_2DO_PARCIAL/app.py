from flask import Flask, render_template, request, redirect, flash
import pymysql

app = Flask(__name__)

# ── Configuración ──────────────────────────────────────────────
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'mysecretkey'

DB_CONFIG = {
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'user':        'root',
    'password':    'root',
    'db':          'crud_albums',
    'charset':     'utf8mb4',
}

def get_conn():
    return pymysql.connect(**DB_CONFIG)


# ── 1
@app.route('/')
def index():
    conn = get_conn()
    con = conn.cursor()
    con.execute("SELECT * FROM tb_autos")
    listAutos = con.fetchall()
    con.close()
    conn.close()
    return render_template('index.html', listAutos=listAutos)


# ── 2
@app.route('/guardar', methods=['POST'])
def guardar():
    marca  = request.form['txtMarca']
    modelo = request.form['txtModelo']
    anio   = request.form['txtAnio']

    conn = get_conn()
    con = conn.cursor()
    con.execute("INSERT INTO tb_autos (marca, modelo, anio) VALUES (%s, %s, %s)",
                (marca, modelo, anio))
    conn.commit()
    con.close()
    conn.close()

    flash('El auto fue agregado correctamente!')
    return redirect('/')


# ── 3
@app.route('/editar/<int:id>')
def editar(id):
    conn = get_conn()
    con = conn.cursor()
    con.execute("SELECT * FROM tb_autos WHERE id = %s", (id,))
    Auto = con.fetchone()
    con.close()
    conn.close()
    return render_template('editarAuto.html', Auto=Auto)


# ── 4
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    marca  = request.form['txtMarca']
    modelo = request.form['txtModelo']
    anio   = request.form['txtAnio']

    conn = get_conn()
    con = conn.cursor()
    con.execute("UPDATE tb_autos SET marca=%s, modelo=%s, anio=%s WHERE id=%s",
                (marca, modelo, anio, id))
    conn.commit()
    con.close()
    conn.close()

    flash('Se actualizó el auto ' + marca)
    return redirect('/')


# ── 5
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_conn()
    con = conn.cursor()
    con.execute("SELECT * FROM tb_autos WHERE id = %s", (id,))
    Auto = con.fetchone()
    con.close()
    conn.close()
    return render_template('eliminarAuto.html', Auto=Auto)


# ── 6
@app.route('/borrar/<int:id>', methods=['POST'])
def borrar(id):
    marca = request.form['txtMarca']

    conn = get_conn()
    con = conn.cursor()
    con.execute("DELETE FROM tb_autos WHERE id = %s", (id,))
    conn.commit()
    con.close()
    conn.close()

    flash('Se eliminó el auto ' + marca)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
