import pickle
import pathlib
import os

class Deserializador:
    def __init__(self):
        self._usuario = None

    def deserializar(self):
        cwd = os.getcwd()
        path =  cwd + '/baseDatos/src/tmp/usuario.pkl'
        picklefile = open(path, "rb")
        usuario = pickle.load(picklefile)
        picklefile.close()
        self._usuario = usuario

    def getArgs(self):
        return self._usuario