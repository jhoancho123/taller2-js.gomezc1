from models.guarderia import Guarderia
from models.concentrado import Concentrado
from models.animal import Animal


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
