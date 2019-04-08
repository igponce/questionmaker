#!/bin/env pyhton
# 
# This is UNRELEASED PROPIETARY SOFTWARE Copyright (C) 2019, Iñigo González Ponce

cuestiones = [
     {
       "titulo": "Cual de estos factores crees que te definen mejor (señale sólo una)",
       "tipo": "opciones",
       "opciones": ["Tu edad",
                  "Tu nacionalidad",
                  "Tu lugar de nacimiento",
                  "Tu religión",
                  "Tu cultura",
                  "Tu nivel educativo",
                  "Tu profesión",
                  "Tu orientación sexual" ]
     },

    { "bloque": "Machismo",
       "titulo": "Qué porcentaje de personas de tu entorno y características\n crees que opinan que",
       "tipo": "porcentaje",
       "preguntas": [
          {"tipo":'-', "titulo": "El problema del paro en España se debe a la incorporación de la mujer al mercado laboral"},
          {"tipo":'-', "titulo": "El sexo femenino es más idóneo para desarrollar las tareas domésticas" },
          {"tipo":'+', "titulo": "Hombres y mujeres deben de compartir en el mismo porcentaje las tareas domésticas."},
          {"tipo":'+', "titulo": "La incorporación de la mujer al trabajo ha sido muy positiva."},
          {"tipo":"-", "titulo": "En caso de divorcio la custodia debe de ser de forma preferente para la madre" },
          {"tipo":"-", "titulo": "En caso de divorcio la primera opción debería ser siempre la custodia compartida"}
       ]
    },

     { "bloque": "Alcohol y drogas.",
       "titulo": "Qué porcentaje de personas de tu entorno y características\n crees que opinan que",
       "tipo": "porcentaje",
       "preguntas": [
          {"tipo":'?', "titulo": "El alcohol no es una droga tan mala como el resto.", "alt":"El Alcohol tiene efectos tan adversos como otras drogas"},
          {"tipo":'?', "titulo": "Los drogadictos son enfermos." },
          {"tipo":'?', "titulo": "El consumo de hachís no es perjudicial para la salud", "alt":"(Debería legalizarse el consumo de hachís)"},
          {"tipo":'?', "titulo": "Emborracharse la mayoría de los fines de semana no es ser alcohólico/a."},
       ]
    },

    { "bloque": "Violencia de Género",
       "titulo": "Qué porcentaje de personas de tu entorno y características crees que opinan que",
       "tipo": "porcentaje",
       "preguntas": [
          {"tipo":'?', "titulo": "El alcohol no es una droga tan mala como el resto.", "alt":"El Alcohol tiene efectos tan adversos como otras drogas"},
          {"tipo":'?', "titulo": "Los drogadictos son enfermos." },
          {"tipo":'?', "titulo": "El consumo de hachís no es perjudicial para la salud", "alt":"(Debería legalizarse el consumo de hachís)"},
          {"tipo":'?', "titulo": "Emborracharse la mayoría de los fines de semana no es ser alcohólico/a."},
       ]
    }


]

"""
El encuestador lee el fichero de enuesta, y mantiene el estado de las respuestas.
"""
class Encuesta (object):

   appState = {}
   preguntas = []
   respuestas = []

   preguntas_iter = None

   def __init__ (self, pollDefinitionFile=""):
      self.readPollDefinition( pollDefinitionFile )

   def readPollDefinition(self, pollDefinitionFile):
      self.preguntas = cuestiones # Cambiar - hardocoded

   def __iter__ (self):
      self.preguntas_iter = self.preguntas.__iter__()
      return self
   
   def __next__ (self):
      return self.preguntas_iter.__next__()


if __name__ == "__main__":
   enc = Encuesta()
   print(enc)
   for q in enc:
     print(q)
