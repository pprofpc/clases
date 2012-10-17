# -*- coding: utf-8 -*-
from persona import Persona


class Alumno(Persona):
    """Hereda de la clase Persona"""

    def __init__(self, nombre="Pepe", curso="4º año"):
        self.curso = curso
        self.nombre = nombre

    def presentar(self):
        print "Hola soy " + self.nombre + " de " + self.curso