from tkinter import *
from ventanaInicio import VentanaInicio
import ventanaInicio
from gestorAplicacion.interfaz.Usuario import Usuario
from datetime import date, time, datetime
from baseDatos.serializador import Serializador
from baseDatos.deserializador import Deserializador

# Creación del usuario administrador
usuario = Usuario("1","Administrador","administrador@unal.edu.co",date.today(),"12345")
serializar = Serializador(usuario)
serializar.serializar()
#Se deserializa el usuario administrador
# deserializar = Deserializador()
# deserializar.deserializar()
# usuario = deserializar.getArgs()

# Ventana de inicio
ventana =  VentanaInicio(usuario)

# Ejecuta la ventana
ventana.mainloop()

#Creación del usuario administrador
#usuario = Usuario("1","Administrador","administrador@unal.edu.co",date.today(),"12345")
#serializar = Serializador(usuario)
#serializar.serializar()







