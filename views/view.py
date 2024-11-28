class View:
    @staticmethod
    def mostrar_concentrados(concentrados: list):
        print("Concentrados disponibles:")
        for concentrado in concentrados:
            print(f"- {concentrado}")

    @staticmethod
    def mostrar_perro(preferencia: str):
        print(f"Este perro prefiere el concentrado: {preferencia}")
