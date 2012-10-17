# -*- coding: utf-8 -*-
import persona
import profesor
import alumno

print "Ejemplo de clases"
Persona1 = persona.Persona("Pedro")
Profe1 = profesor.Profesor("Pablo")
Alumno1 = alumno.Alumno("Juanchi")
Profe1.presentar()
Profe1.materia = "Informática"
Profe1.presentar()
Alumno1.presentar()
Alumno1.saludar(Profe1)