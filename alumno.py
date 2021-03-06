# -*- coding: utf-8 -*-
from persona import Persona


class Alumno(Persona):
    """Hereda de la clase Persona, es una clase hija o subclase"""

    def __init__(self, nombre="Pepe", curso="4º año"):
        self.curso = curso
        self.nombre = nombre

    def presentar(self):
        """Redefine el método *presentar* de la clase padre **Persona**.
El alumno se presenta con su *nombre* y *curso*"""
        print "Hola soy " + self.nombre + " de " + self.curso
