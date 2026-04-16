"""
app.py
------
Punto de entrada de la aplicación Flask.
Solo configura la app e importa los módulos de rutas.
"""

import os
from flask import Flask, render_template
from routes import api

# ---------------------------------------------------------------------------
# Configuración de Flask
# ---------------------------------------------------------------------------

TEMPLATE_DIR = os.path.abspath("../frontend/templates")
STATIC_DIR  = os.path.abspath("../frontend/static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.register_blueprint(api)


# ---------------------------------------------------------------------------
# Vistas
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------------------------------------------------------
# Arranque
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)