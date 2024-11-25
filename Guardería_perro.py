from typing import List
from concentrado import Concentrado

class Guarderia:
    def __init__(self):
        self.concentrados: List[Concentrado] = []  # Lista de concentrados

    def agregar_concentrado(self, concentrado: Concentrado):
        self.concentrados.append(concentrado)

    def listar_concentrados(self) -> List[str]:
        return [concentrado.get_informacion() for concentrado in self.concentrados]

class Perro:
    def __init__(self, nombre: str, concentrado_preferido: Concentrado):
        self.nombre = nombre                        
        self.concentrado_preferido = concentrado_preferido  

    def dar_nombre(self) -> str:
        return self.nombre

    def dar_concentrado_preferido(self) -> str:
        return self.concentrado_preferido.get_nombre()


if __name__ == "__main__":
    # Crear concentrados
    concentrado1 = Concentrado("Concentrado xyz", 534.0, 50540, "INVIMA1")
    concentrado2 = Concentrado("Concentrado abc", 678.0, 34560, "INVIMA6")

    # Crear guardería y agregar concentrados
    guarderia = Guarderia()
    concentrados = [concentrado1, concentrado2]  # Lista de concentrados

    for concentrado in concentrados:
        guarderia.agregar_concentrado(concentrado)

    # Crear un perro con un concentrado preferido
    perro = Perro("Koki", concentrado1)
    print(f"{perro.dar_nombre()} prefiere: {perro.dar_concentrado_preferido()}")