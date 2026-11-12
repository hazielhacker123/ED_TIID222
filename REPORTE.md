# Reporte de Práctica: Introducción al Microframework Flask

**Universidad:** Universidad Politécnica de Querétaro (UPQ)  
**Materia:** Seguridad Informática — Examen 1er Parcial  
**Carrera:** Ingeniería en Tecnologías de la Información e Innovación Digital  

---

## 1. Introducción
Flask es un microframework minimalista de código abierto desarrollado en Python, diseñado para la construcción ágil de aplicaciones web, APIs REST y microservicios. A diferencia de frameworks como Django, Flask mantiene un núcleo ligero y modular, permitiendo extender sus capacidades mediante paquetes adicionales como conectores a bases de datos (`Flask-MySQLdb`) y motores de plantillas (`Jinja2`).

---

## 2. Requisitos y Preparación del Entorno

### 2.1 Verificación de Python y PIP
- **Python Version:** 3.10+ (en este entorno: `Python 3.15.0`)
- **PIP Version:** Gestor oficial de paquetes de Python (`pip 26.2.1`)

```bash
python --version
python -m pip install -U pip
pip -V
```

---

## 3. Instalación de Paquetes y Dependencias

### 3.1 Instalación de Flask
Instalación del núcleo del microframework Flask junto con su motor de plantillas Jinja2 y utilidades WSGI:
```bash
pip install Flask
```
Paquetes instalados:
- `Flask` (3.1.3)
- `Werkzeug` (3.1.9)
- `Jinja2` (3.1.6)
- `click` (8.5.0)
- `blinker` (1.9.0)
- `itsdangerous` (2.2.0)
- `MarkupSafe` (3.0.4)

### 3.2 Instalación de Flask-MySQLdb
Instalación de la extensión para conectar aplicaciones Flask con bases de datos MySQL/MariaDB:
```bash
pip install Flask-MySQLdb
```
Paquetes instalados:
- `Flask-MySQLdb` (2.0.0)
- `mysqlclient` (2.3.0)

### 3.3 Verificación de Librerías (`pip list`)
```text
Package       Version
------------- -------
blinker       1.9.0
click         8.5.0
Flask         3.1.3
Flask-MySQLdb 2.0.0
itsdangerous  2.2.0
Jinja2        3.1.6
MarkupSafe    3.0.4
mysqlclient   2.3.0
pip           26.2.1
Werkzeug      3.1.9
```

---

## 4. Desarrollo de la Aplicación (`prueba.py`)

Se creó el archivo `prueba.py` con el siguiente código base:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Flask!"

if __name__ == "__main__":
    app.run(port=5000)
```

---

## 5. Ejecución y Pruebas

### 5.1 Ejecutar el servidor de desarrollo
```bash
flask --app prueba.py run
```
Salida en consola:
```text
 * Serving Flask app 'prueba.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### 5.2 Verificación en Navegador
Al ingresar a la URL `http://127.0.0.1:5000`, la aplicación responde exitosamente mostrando el mensaje:
> **¡Hola, Flask!**

---

## 6. Conclusiones

1. **Simplicidad y Eficiencia:** Flask permite levantar un servicio web funcional con un número mínimo de líneas de código y una arquitectura limpia, ideal tanto para prototipado como para arquitecturas de microservicios.
2. **Modularidad y Extensibilidad:** A través de herramientas como PIP y paquetes como `Flask-MySQLdb`, Flask se integra de forma directa y flexible con sistemas gestores de bases de datos relacionales sin sobrecargar el proyecto con configuraciones innecesarias.
3. **Perspectiva de Seguridad Informática:** Comprender el ciclo de vida de peticiones HTTP, rutas y el manejo de variables de entorno en microframeworks es un pilar fundamental para auditar y mitigar vulnerabilidades comunes (como inyección SQL, XSS y configuraciones inadecuadas en modo debug de servidores en producción).
