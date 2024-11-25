from flask import Flask, jsonify, render_template
from controllers.animal_controller import AnimalController

app = Flask(__name__)
controller = AnimalController()

@app.route("/")
def home():
    # Renderizar la página principal
    return render_template("index.html")

@app.route("/api/animal/<string:nombre>")
def obtener_sonido_animal(nombre):
    # Consultar el sonido del animal
    resultado = controller.obtener_sonido(nombre)
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)
