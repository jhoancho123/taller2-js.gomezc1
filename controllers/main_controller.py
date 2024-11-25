from models.guarderia import Guarderia
from models.perro.py import Perro
from models.concentrado import Concentrado
from views.view import View

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
