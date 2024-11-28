from models.guarderia import Guarderia
from models.perro.py import Perro
from models.concentrado import Concentrado
from views.view import View
from models.animal import Animal

class MainController:
    def __init__(self):
        self.guarderia = Guarderia()
        self.view = View()

    def agregar_concentrados_iniciales(self):
        concentrado1 = Concentrado("Concentrado xyz", 534.0, 50540, "INVIMA1")
        concentrado2 = Concentrado("Concentrado abc", 678.0, 34560, "INVIMA6")
        self.guarderia.agregar_concentrado(concentrado1)
        self.guarderia.agregar_concentrado(concentrado2)

    def mostrar_concentrados(self):
        concentrados = self.guarderia.listar_concentrados()
        self.view.mostrar_concentrados(concentrados)

    def crear_perro(self):
        concentrado1 = self.guarderia.concentrados[0]
        perro = Perro("Koki", concentrado1)
        self.view.mostrar_perro(perro.dar_concentrado_preferido())

class AnimalController:
    def __init__(self):
        # Definir los animales y sus sonidos
        self.animales = {
            "gato": Animal("Gato", "miau"),
            "perro": Animal("Perro", "guau"),
            "huron": Animal("Hurón", "chirp"),
            "boa": Animal("Boa constrictor", "ssss")
        }

    def obtener_sonido(self, animal: str) -> dict:
        # Buscar el animal por su nombre
        animal_obj = self.animales.get(animal.lower())
        if animal_obj:
            return {"nombre": animal_obj.nombre, "sonido": animal_obj.get_sonido()}
        return {"error": "Animal no encontrado"}
