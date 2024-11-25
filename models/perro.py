from models.concentrado import Concentrado

class Perro:
    def __init__(self, nombre: str, concentrado_preferido: Concentrado):
        self.nombre = nombre
        self.concentrado_preferido = concentrado_preferido

    def dar_nombre(self) -> str:
        return self.nombre

    def dar_concentrado_preferido(self) -> str:
        return self.concentrado_preferido.get_nombre()
