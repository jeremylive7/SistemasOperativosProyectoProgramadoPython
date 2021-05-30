import time
from datetime import datetime

class Controlador:

    def __init__(self):
        self.leerTexto = LectorTxt()
        self.listaComandos = self.leerTexto.read()

    def runCommands(self):
        for line in self.listaComandos:
            line = "self."+line
            eval(line)

    #Entender replacement policy.



class LectorTxt:

    def __init__(self):
        self.txt = ""

    def read(self):
        try:
            handler = open("comandos.txt")
            return handler.readlines()
        except FileNotFoundError:
            print('Archivo no encontrado')
            exit()
