#!/bin/env python
#
# Encuesta.py
# This is unreleased propietary software (c)2019 Iñigo González Ponce

# Módulo de encuestas
# Carga el fichero de encuesta, y prepara para serializar respuestas

class encuesta

  idEncuesta = None
  ficheroPreguntas = None
  preguntas = new Hash 

  def __init__ (self):
    # inicializa encuesta
    self.idEncuesta = None

  def loadFromFile( filename ):

    idEncuesta = filename
    ficheroPreguntas = filename

    fp = open(ficheroPreguntas)
    

  def __str__ (self):
      "{idEncuesta={},\nficheroPreguntas={}, preguntas={}}" % (idEncuesta, ficheroPreguntas, preguntas)

end


