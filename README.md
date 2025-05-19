# 🎮 PuertoGames CRUD – Módulo Videojuegos

> Proyecto realizado como parte de la **Prueba Práctica Final** del módulo Videojuegos para la tienda PuertoGames.

📅 **Fecha de entrega**: Viernes 23 de mayo de 2025  
👨‍🏫 **Docente**: Marcelo Crisóstomo Carrasco  
👤 **Integrante(s)**: [Nombre completo del o los estudiantes]

---

## 🧾 Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación CRUD en Python, con una interfaz gráfica amigable (PyGUI/Tkinter) conectada a una base de datos **SQL Server**. Se enfoca exclusivamente en la gestión de videojuegos y muestra estadísticas mediante gráficos generados con **matplotlib**.

---

## 🧩 Funcionalidades implementadas

- [ ] Crear videojuego  
- [ ] Listar videojuegos  
- [ ] Editar videojuego  
- [ ] Eliminar videojuego  
- [ ] Validaciones de campos  
- [ ] Gráfico estadístico por plataforma  
- [ ] Barra de búsqueda (opcional - bonus)

---

## 🧱 Estructura del proyecto

```

📁 puertogames/
├── main.py               # Punto de entrada
├── gui.py                # Interfaz gráfica
├── database.py           # Funciones de conexión y consultas
├── script.sql            # Creación e inserción de base de datos
├── README.md             # Este archivo
└── capturas/             # Capturas de pantalla de la aplicación

````

---

## ⚙️ Requisitos

- Python 3.x
- SQL Server
- Librerías necesarias:

```bash
pip install pyodbc matplotlib pygubu
````

---

## ▶️ Instrucciones para ejecutar

1. Crear la base de datos ejecutando `script.sql` en SQL Server.
2. Asegurarse de que el archivo `database.py` tenga la conexión correcta.
3. Ejecutar la aplicación:

```bash
python main.py
```

---

## 🖼️ Capturas de pantalla

*Agrega aquí al menos 2 capturas de pantalla de tu aplicación funcionando, incluyendo el gráfico.*

---

## 📊 Descripción del gráfico

* Tipo de gráfico: \[Ej. gráfico de barras]
* Fuente de datos: consulta SQL desde la tabla `Videojuegos`
* Representa: cantidad de videojuegos por plataforma

---

## 🧠 Conclusión

*Describe brevemente qué aprendiste, cómo fue el desarrollo del proyecto, y qué desafíos enfrentaste.*

---

## 🗃️ Repositorio GitHub

🔗 [Enlace al repositorio](https://github.com/tuusuario/puertogames-crud)

---

© 2025 - Duoc UC | Escuela de Informática y Telecomunicaciones

```
