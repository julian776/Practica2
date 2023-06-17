import pickle
import pathlib
import os

class Serializador:
    def __init__(self, usuario):
        self._usuario = usuario

    def serializar(self):
        path =  "./src/tmp/usuario.pkl"
        picklefile = open(path, "wb")
        pickle.dump(self._usuario, picklefile)
        picklefile.close()
