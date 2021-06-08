import time
from datetime import datetime

class Controlador:

    def __init__(self):
        self.fetch_policy = ""
        self.placement_policy = ""
        self.replacement_policy = ""
        self.size = ""
        self.replacement_scope = ""
        self.cleaning_policy = ""
        self.load_control="Degree of multiprogramming"
        self.leerTexto = LectorTxt()
        self.listaComandos = self.leerTexto.read()

    def runCommands(self):
        for line in self.listaComandos:
            line = "self."+line
            eval(line)

    def create(self, fetch_policy="Demand",
                placement_policy="First available",
                replacement_policy="LRU",
                size="Fixed",
                replacement_scope="Global",
                cleaning_policy="Demand"):
        self.fetch_policy = fetch_policy
        self.placement_policy = placement_policy
        self.replacement_policy = replacement_policy
        self.size = size
        self.replacement_scope = replacement_scope
        self.cleaning_policy = cleaning_policy



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
