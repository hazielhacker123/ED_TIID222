# Importamos las herramientas necesarias de la librería Flask:
# - Flask: para crear la aplicación web.
# - render_template: para mostrar archivos HTML (como vistas o plantillas).
# - redirect: para redirigir al usuario de una ruta a otra.
from flask import Flask, render_template, redirect

# Inicializamos la aplicación de Flask
app = Flask(__name__)

# ==========================================
# CREACIÓN DE RUTAS
# ==========================================

# Ruta raíz (la página de bienvenida o inicio de tu web)
@app.route("/")
def home():
    # Función que se ejecuta al entrar a la raíz y retorna un mensaje de texto
    return "¡Hola, Flask!"






@app.route("/registro", methods=["GET", "POST"])
def register():
    # Función que maneja la ruta de registro de usuarios
    if request.method == "POST":
       nombre = request.form["nombre"]
    apellido_paterno = request.form["apellido_paterno"]
    apellido_materno = request.form["apellido_materno"]
    correo = request.form["correo"]
    password_hash = request.form["password_hash"]
    id_rol = request.form["id_rol"]

#gereramos un hash a partir de la contraseña ingresada por el usuario
password = generate_password_hash(password_hash)




#Importar la libreria de MYSQL para flask
from flask_mysqldb import MySQL


#PERMITE CARGAR LAS VISTAS CUANDO SE MODIFICAN
app.config['TEMPLATES_AUTO_RELOAD']

#importamos la libreria de hash     


#Creamos una instancia del proyecto 
app= Flask(__name__)


#Configuracion de la conexion

app.config['MYSQL_HOST'] = 'local host'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'DBFLASK'
app.secret_key = 'mysecretkey'

mysql = MYSQL(app)





# ==========================================
# EJECUCIÓN DEL SERVIDOR
# ==========================================

# Este bloque verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    # Inicia el servidor de desarrollo local en el puerto 5000
    app.run(port=5000)