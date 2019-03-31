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
       "titulo": "Qué porcentaje de personas de tu entorno y características crees que opinan que",
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
       "titulo": "Qué porcentaje de personas de tu entorno y características crees que opinan que",
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

import tkinter as tk

class Application(tk.Frame):

    appState = {  }
    respuestas = []

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()    
        self.appState["question"] = 0

    def crea_pantallas_encuesta(self, cuestiones, num):

        cc = cuestiones[num]

        #self.titulo = tk.Label(self, master=None, cnf={"height": 2})
        #self.titulo[text] = cc['titulo']

        self.cuestion= tk.Button(self)
        self.cuestion['text'] = cc['titulo']
        if (cc['tipo']=='opciones') :
            for op in cc['opciones']:
                self.radio_button = "asd" 


    def create_widgets(self):

        v = -1

        self.titulo = tk.Label(self, height=4, font=("Helvetica", 12) )
        self.titulo["text"] = cuestiones[1]['titulo']
        self.titulo.grid(column=1, row=1, columnspan=20)

        for i in range(0,11):
           self.pct0 = tk.Radiobutton(self, text="{}%".format(10*i), variable=v, value=i, indicatoron=0)
           self.pct0.grid(column=1+i, row=2)
           # self.pct0.pack(side="left")
           tk.Radiobutton(self,text="No sabe\nNo desea contestar", variable=v, value=i, indicatoron=0).grid(column=11, row=2)

        gridLabelSpan = [
            ('nadie', 1),
            ('casi nadie', 2),
            ('algunas personas', 2),
            ('la mitad', 1),
            ('la mayoria', 2),
            ('todos', 1)
        ]


        tk.Label(self,text="(nadie)").grid(row=3, column=1)
        tk.Label(self,text="(casi nadie)").grid(row=3,column=2, columnspan=2)
        tk.Label(self,text="(algunas personas, pero pocas)").grid(row=3,column=4, columnspan=2)
        tk.Label(self,text="(la mitad)").grid(row=3,column=6)
        tk.Label(self,text="(la mayoría, pero no todos)").grid(row=3,column=7, columnspan=2)
        tk.Label(self,text="(casi todos)").grid(row=3,column=9)
        tk.Label(self,text="(todos)").grid(row=3,column=10)




        if True :
          return



        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(anchor="w")

        self.hola = tk.Button(self)
        self.hola["text"] = "Hola que pasa contigo tio"
        self.hola.pack(side="bottom")

        self.caption = tk.Label(self)
        self.caption["text"]= "Lorem ipsum dolor asd asd a euuug  es y no va a aser facil ecribit tanto tiempo seguido..." 
        self.caption.pack(side="bottom")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
