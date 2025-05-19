import tkinter as tk
from conexion_sqlserver import obtener_videojuegos

#Obtener datos de la BD
datos = obtener_videojuegos()

#Crear una ventana
ventana = tk.Tk()
ventana.title("Catálogo de Videojuegos")
ventana.geometry("700x400")

#Título
titulo = tk.Label(ventana, text="🎮 Listado de Videojuegos 🎮", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

#Area de texto
texto = tk.Text(ventana, height=15, width=70, font=("Courier", 10))
texto.pack()

#Mostrar los datos
for row in datos:
    nombre, genero, precio, plataforma = row
    texto.insert(tk.END, f"{nombre:25} | {genero:15} | ${precio:8.0f} | {plataforma}\n")

#Boton cerrar
cerrar_btn = tk.Button(ventana, text="cerrar", command=ventana.destroy)
cerrar_btn.pack(pady=10)

#Ejecutar la interfaz
ventana.mainloop()