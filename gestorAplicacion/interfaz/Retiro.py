
# Ana Guarín
# Isabela Hernandez
# Julián Álvarez
# Cristian Mena

from gestorAplicacion.interfaz.Transaccion import Transaccion
from gestorAplicacion.interfaz.Categoria import Categoria

class Retiro(Transaccion):
    def __init__(self, monto, fechaCreacion, cuentaOrigen, cuantaDestino, categoria):
        super().__init__(monto, fechaCreacion)
        self._cuentaOrigen = cuentaOrigen
        self._cuentaDestino = cuantaDestino
        self._categoria = categoria
        
        if categoria != Categoria.Nulo:
            categoria.setSaldo(categoria.getSaldo() - monto)

    # Setters y getters
    def setCuentaOrigen(self, cuentaOrigen):
        self._cuentaOrigen = cuentaOrigen

    def getCuentaOrigen(self):
        return self._cuentaOrigen
    
    def setCuentaDestino(self, cuentaDestino):
        self._cuentaDestino = cuentaDestino

    def getCuentaDestino(self):
        return self._cuentaDestino
    
    def setCategoria(self, categoria):
        self._categoria = categoria
    
    def getCategoria(self):
        return self._categoria