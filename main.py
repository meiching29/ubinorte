import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def mostrar_pagina(frame):
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame.pack(fill='both', expand=True)

def mostrar_seleccion():
    partida = partida_combobox.get()
    llegada = llegada_combobox.get()
    print(f"Partida: {partida}, Llegada: {llegada}")

ventana = tk.Tk()
ventana.title("ubinorte")
ventana.geometry("850x650")
ventana.minsize(850,650)
ventana.maxsize(850,650)
ventana.iconbitmap("logo.ico")

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla - 850) // 2
y = (alto_pantalla - 650) // 2
ventana.geometry(f"850x650+{x}+{y}")

frame1 = tk.Frame(ventana, width=850, height=650)
frame2 = tk.Frame(ventana, width=850, height=650)
frame3 = tk.Frame(ventana, width=850, height=650)
frame4 = tk.Frame(ventana, width=850, height=650)
frame5 = tk.Frame(ventana, width=850, height=650)

#Pagina de inicio
fondo_imagen = Image.open("inicioimg.png") 
fondo_imagen = fondo_imagen.resize((850, 650), Image.Resampling.LANCZOS) 
fondo_imagen_tk = ImageTk.PhotoImage(fondo_imagen)  
label_fondo = tk.Label(frame1, image=fondo_imagen_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1) 

boton_imagen = Image.open("qesubinorte.png")
boton_imagen = boton_imagen.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk = ImageTk.PhotoImage(boton_imagen)
boton1 = tk.Button(frame1, image=boton_imagen_tk, command=lambda: mostrar_pagina(frame2))
boton1.place(x=40, y=100) 

boton_imagen2 = Image.open("team.png")
boton_imagen2 = boton_imagen2.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk2 = ImageTk.PhotoImage(boton_imagen2)
boton2 = tk.Button(frame1, image=boton_imagen_tk2, command=lambda: mostrar_pagina(frame3))
boton2.place(x=40, y=220) 

boton_imagen3 = Image.open("meetcampus.png")
boton_imagen3 = boton_imagen3.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk3 = ImageTk.PhotoImage(boton_imagen3)
boton3 = tk.Button(frame1, image=boton_imagen_tk3, command=lambda: mostrar_pagina(frame4))
boton3.place(x=40, y=340) 

boton_imagen4 = Image.open("comenzar.png")
boton_imagen4 = boton_imagen4.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk4 = ImageTk.PhotoImage(boton_imagen4)
boton4 = tk.Button(frame1, image=boton_imagen_tk4, command=lambda: mostrar_pagina(frame5))
boton4.place(x=40, y=460) 

#Segunda página
fondo_imagen2 = Image.open("whatnorte.png") 
fondo_imagen2 = fondo_imagen2.resize((850, 650), Image.Resampling.LANCZOS) 
fondo_imagen_tk2 = ImageTk.PhotoImage(fondo_imagen2)  
fondo2 = tk.Label(frame2, image=fondo_imagen_tk2)
fondo2.place(x=0, y=0, relwidth=1, relheight=1) 

boton_imagen11 = Image.open("qesubinorte.png")
boton_imagen11 = boton_imagen11.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk11 = ImageTk.PhotoImage(boton_imagen11)
boton11 = tk.Button(frame2, image=boton_imagen_tk11, command=lambda: mostrar_pagina(frame2))
boton11.place(x=40, y=100) 

boton_imagen22 = Image.open("team.png")
boton_imagen22 = boton_imagen22.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk22 = ImageTk.PhotoImage(boton_imagen22)
boton22 = tk.Button(frame2, image=boton_imagen_tk22, command=lambda: mostrar_pagina(frame3))
boton22.place(x=40, y=220) 

boton_imagen33 = Image.open("meetcampus.png")
boton_imagen33 = boton_imagen33.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk33 = ImageTk.PhotoImage(boton_imagen33)
boton33 = tk.Button(frame2, image=boton_imagen_tk33, command=lambda: mostrar_pagina(frame4))
boton33.place(x=40, y=340) 

boton_imagen44 = Image.open("comenzar.png")
boton_imagen44 = boton_imagen44.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk44 = ImageTk.PhotoImage(boton_imagen44)
boton44 = tk.Button(frame2, image=boton_imagen_tk44, command=lambda: mostrar_pagina(frame5))
boton44.place(x=40, y=460)

#Tercera página
fondo_imagen3 = Image.open("equipo.png") 
fondo_imagen3 = fondo_imagen3.resize((850, 650), Image.Resampling.LANCZOS) 
fondo_imagen_tk3 = ImageTk.PhotoImage(fondo_imagen3)  
fondo3 = tk.Label(frame3, image=fondo_imagen_tk3)
fondo3.place(x=0, y=0, relwidth=1, relheight=1) 

boton_imagen1111 = Image.open("qesubinorte.png")
boton_imagen1111 = boton_imagen1111.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk1111 = ImageTk.PhotoImage(boton_imagen1111)
boton1111 = tk.Button(frame3, image=boton_imagen_tk1111, command=lambda: mostrar_pagina(frame2))
boton1111.place(x=40, y=100) 

boton_imagen2222 = Image.open("team.png")
boton_imagen2222 = boton_imagen2222.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk2222 = ImageTk.PhotoImage(boton_imagen2222)
boton2222 = tk.Button(frame3, image=boton_imagen_tk2222, command=lambda: mostrar_pagina(frame3))
boton2222.place(x=40, y=220) 

boton_imagen3333 = Image.open("meetcampus.png")
boton_imagen3333 = boton_imagen3333.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk3333 = ImageTk.PhotoImage(boton_imagen3333)
boton3333 = tk.Button(frame3, image=boton_imagen_tk3333, command=lambda: mostrar_pagina(frame4))
boton3333.place(x=40, y=340) 

boton_imagen4444 = Image.open("comenzar.png")
boton_imagen4444 = boton_imagen4444.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk4444 = ImageTk.PhotoImage(boton_imagen4444)
boton4444 = tk.Button(frame3, image=boton_imagen_tk4444, command=lambda: mostrar_pagina(frame5))
boton4444.place(x=40, y=460)

#Cuarta página
fondo_imagen4 = Image.open("campus.png") 
fondo_imagen4 = fondo_imagen4.resize((850, 650), Image.Resampling.LANCZOS) 
fondo_imagen_tk4 = ImageTk.PhotoImage(fondo_imagen4)  
fondo4 = tk.Label(frame4, image=fondo_imagen_tk4)
fondo4.place(x=0, y=0, relwidth=1, relheight=1) 

boton_imagen111 = Image.open("qesubinorte.png")
boton_imagen111 = boton_imagen111.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk111 = ImageTk.PhotoImage(boton_imagen111)
boton111 = tk.Button(frame4, image=boton_imagen_tk111, command=lambda: mostrar_pagina(frame2))
boton111.place(x=40, y=100) 

boton_imagen222 = Image.open("team.png")
boton_imagen222 = boton_imagen222.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk222 = ImageTk.PhotoImage(boton_imagen222)
boton222 = tk.Button(frame4, image=boton_imagen_tk222, command=lambda: mostrar_pagina(frame3))
boton222.place(x=40, y=220) 

boton_imagen333 = Image.open("meetcampus.png")
boton_imagen333 = boton_imagen333.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk333 = ImageTk.PhotoImage(boton_imagen333)
boton333 = tk.Button(frame4, image=boton_imagen_tk333, command=lambda: mostrar_pagina(frame4))
boton333.place(x=40, y=340) 

boton_imagen444 = Image.open("comenzar.png")
boton_imagen444 = boton_imagen444.resize((250, 70), Image.Resampling.LANCZOS)  
boton_imagen_tk444 = ImageTk.PhotoImage(boton_imagen444)
boton444 = tk.Button(frame4, image=boton_imagen_tk444, command=lambda: mostrar_pagina(frame5))
boton444.place(x=40, y=460)

#Quinta Página
fondo_imagen5 = Image.open("eleccion.png") 
fondo_imagen5 = fondo_imagen5.resize((850, 650), Image.Resampling.LANCZOS) 
fondo_imagen_tk5 = ImageTk.PhotoImage(fondo_imagen5)  
fondo5 = tk.Label(frame5, image=fondo_imagen_tk5)
fondo5.place(x=0, y=0, relwidth=1, relheight=1) 

# Lista de lugares
lugares = [
    "1966", "Admisión", "Bamboo Funcionarios", "Bamboo J", "Bamboo K", "Biblioteca", "Bloque A", "Bloque B", 
    "Bloque C", "Bloque D", "Bloque E", "Bloque F", "Bloque G", "Bloque I", "Bloque J", "Bloque K", "Bloque L", 
    "Bolque M", "Bocas de Ceniza", "Café DuNord", "Cancha de Futbol", "Canchas de Tenis", "Casa Estudio", 
    "Centro Médico", "Coliseo", "Emisora Uninorte", "Express", "Fuente", "Graphic", "Km5", "La Creperia", 
    "La Esquina", "Laboratorio de Pedagogia", "Laboratorios de Física", "Laboratorios Química", "Le Salón", 
    "Oficina Egresados", "Oficina Rectoria", "Parqueadero 12", "Parqueadero 8", "Parqueadero 9", "Plaza", 
    "Puerta 4", "Puerta 7", "Registro", "Store", "Terrace"
]
# Inicio
partida_combobox = ttk.Combobox(frame5, values=lugares)
partida_combobox.place(x=600, y=110)
# Destino
llegada_combobox = ttk.Combobox(frame5, values=lugares)
llegada_combobox.place(x=600, y=380)

botonrutas = Image.open("rutas.png")
botonrutas = botonrutas.resize((250, 70), Image.Resampling.LANCZOS)  
botonrutastk = ImageTk.PhotoImage(botonrutas)
botonr = tk.Button(frame5, image=botonrutastk, command=lambda: mostrar_pagina(frame5))
botonr.place(x=575, y=530)


mostrar_pagina(frame1)
ventana.mainloop()