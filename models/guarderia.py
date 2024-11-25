from typing import List
from models.concentrado import Concentrado

class Guarderia:
    def __init__(self):
        self.concentrados: List[Concentrado] = []

    def agregar_concentrado(self, concentrado: Concentrado):
        self.concentrados.append(concentrado)

    def listar_concentrados(self) -> List[str]:
        return [concentrado.get_informacion() for concentrado in self.concentrados]
