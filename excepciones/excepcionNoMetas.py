from excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionNoMeta(ErrorAplicacion):
    
    # Constructor
    def __init__(self):
        super().__init__(f"El usuario no tiene Metas disponibles")