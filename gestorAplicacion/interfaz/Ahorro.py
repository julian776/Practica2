
# Ana Guarín
# Isabela Hernandez
# Julián Álvarez
# Cristian Imbacuan

from gestorAplicacion.interfaz.Cuenta import Cuenta
from datetime import date

class Ahorro(Cuenta):

    def __init__(self, usuario, nombre, fechaRetiro):
        super().__init__(usuario, nombre)
        self._fechaRetiro = fechaRetiro
        self._disponible = 0
    
    def getDisponible(self):
        return self._disponible
    
    def getNombre(self):
        return super().getNombre()
    
    def setNombre(self, nombre):
        return super().setNombre(nombre)

    def retirar(self, monto):
        if self._fechaRetiro.isBefore(date.today()):
            return super().retirar(monto)
        return False

    def getFechaRetiro(self):
        return self._fechaRetiro

    def setFechaRetiro(self, fechaRetiro):
        self._fechaRetiro = fechaRetiro
