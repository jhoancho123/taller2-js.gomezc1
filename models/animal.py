class Animal:
    def __init__(self, nombre: str, sonido: str):
        self.nombre = nombre
        self.sonido = sonido

    def get_sonido(self) -> str:
        return f"El {self.nombre} hace: {self.sonido}"
