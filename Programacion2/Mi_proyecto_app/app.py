import os
import sys
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta de solo lectura para recursos empaquetados (templates, etc.)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Ruta temporal con PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")  # Ruta normal en desarrollo
    return os.path.join(base_path, relative_path)

# Ruta de escritura segura (directorio actual)
data_dir = os.path.join(os.getcwd(), "data")
os.makedirs(data_dir, exist_ok=True)
data_file = os.path.join(data_dir, "nombres.txt")

# Crear el archivo si no existe
if not os.path.exists(data_file):
    with open(data_file, "w", encoding="utf-8") as f:
        pass  # Crea un archivo vacío

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""

    if request.method == "POST":
        nombre = request.form.get("nombre")
        if nombre:
            with open(data_file, "a", encoding="utf-8") as f:
                f.write(nombre + "\n")
            mensaje = "Nombre guardado con éxito."

    # Leer nombres desde el archivo
    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as f:
            nombres = f.readlines()
    else:
        nombres = []

    return render_template("index.html", nombres=nombres, mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)

