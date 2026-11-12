from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Ruta principal: muestra la vista de login
@app.route("/")
def home():
    return render_template("login.html")

# Ruta login
@app.route("/login")
def login():
    return render_template("login.html")

# Ruta guardar: muestra index.html
@app.route("/guardar")
def guardar():
    print("EJECUTANDO LA RUTA GUARDAR CORRECTA")
    return render_template("index.html")

# Ruta logout: redirige al login
@app.route("/logout")
def logout():
    return redirect("/login")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
