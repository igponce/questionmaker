#!/bin/env pyhton
# 
# This is UNRELEASED PROPIETARY SOFTWARE Copyright (C) 2019, Iñigo González Ponce

from encuesta import Encuesta
import tkinter as tk

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

class Application(tk.Frame):

   appState = {  }
   respuestas = []

   def __init__(self, master=None, **options):
      super().__init__(master, options)
      self.master = master
      self.pack()
      # self.create_widgets()    
      self.pantalla_encuesta(cuestiones, 1)
      self.appState["question"] = 0

   # Pantalla de la encuesta

   def pantalla_encuesta(self, encuesta, num):

      cc = cuestiones[num]
      #self.titulo = tk.Label(self, master=None, cnf={"height": 2})
      #self.titulo[text] = cc['titulo']

      titulo_pregunta = cc['titulo']
      cuestion = cc['preguntas'][num]['titulo']

      print(cc)
      print(titulo_pregunta)
      print(cuestion)

      v = -1

      self.titulo = tk.Label(self, height=4, font=("Helvetica", 12) )
      self.titulo["text"] = titulo_pregunta
      self.titulo.grid(column=1, row=1, columnspan=20)

      self.cuestion = tk.Label(self, height=4, font=("Helvetica", 12) )
      self.cuestion["text"] = cuestion
      self.cuestion.grid(column=1,row=2, columnspan=20)

      for i in range(0,11):
         self.pct0 = tk.Radiobutton(self, text="{}%".format(10*i), variable=v, value=i, indicatoron=0, width=8)
         self.pct0.grid(column=1+i, row=3, sticky="EW")
         # self.pct0.pack(side="left")

      self.nsnc = tk.Radiobutton(self,text="No sabe\nNo desea contestar", variable=v, value=-1, indicatoron=0)
      self.nsnc.grid(column=13, row=3, sticky="EW")
      self.nsnc.select()

      # Opciones preguntas y columnspan de cada pregunta
      descripciones_preguntas = [
         ('nadie', 1),
         ('casi nadie', 2),
         ('algunas personas\npero pocas', 2),
         ('la mitad', 1),
         ('la mayoria pero\nno todos', 2),
         ('casi todos',2),
         ('todos', 1),
         ('',1)
        ]
        
      column = 1
      for (descr,colspan) in descripciones_preguntas:
         tk.Label(self, text=descr).grid(row=4,column=column, columnspan = colspan, sticky="EW")
         column += colspan 

      self.quit = tk.Button(self, text="EXIT", fg="red", command=self.master.destroy)\
                    .grid(row=6, column=2,columnspan=2, sticky="EW")
      self.news = tk.Button(self, text="Siguiente >>")  \
                    .grid(row=6, column=10, columnspan=2, sticky="EW", pady=10) 

if __name__ == "__main__":
   root = tk.Tk( )
   scrW = root.winfo_screenwidth()
   scrH = root.winfo_screenheight()
   root.title ("Encuestador") # Hardcoded ?
   root.geometry("{}x{}".format(scrW, scrH))

   app = Application(master=root, bd=25, relief="flat")
   app.mainloop()
   pass
