from excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionNoAhorros(ErrorAplicacion):
    
    # Constructor
    def __init__(self):
        super().__init__(f"El usuario no tiene Ahorros disponibles")