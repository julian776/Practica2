
# Ana Guarín
# Isabela Hernandez
# Julián Álvarez
# Cristian Imbacuan

from gestorAplicacion.interfaz.Transaccion import Transaccion
from gestorAplicacion.interfaz.Categoria import Categoria

class Ingreso(Transaccion):

    def __init__(self, monto, fechaCreacion, cuentaOrigen, cuentaDestino, categoria):
        
        super().__init__(monto, fechaCreacion)
        self._cuentaOrigen = cuentaOrigen
        self._cuentaDestino = cuentaDestino
        self._categoria = categoria
    
        if categoria != Categoria.Nulo:
            categoria.setSaldo(categoria.getSaldo() + monto)
        #if categoria.getSaldo() >= categoria.getPresupuesto():
        #   print(Alerta.Excede(categoria))

    def getCuentaOrigen(self):
        return self._cuentaOrigen

    def setCuentaOrigen(self, cuentaOrigen):
        self._cuentaOrigen = cuentaOrigen

    def getCuentaDestino(self):
        return self._cuentaDestino

    def setCuentaDestino(self, cuentaDestino):
        self._cuentaDestino = cuentaDestino

    def setCategoria(self, categoria):
        self._categoria = categoria
    
    def getCategoria(self):
        return self._categoria

