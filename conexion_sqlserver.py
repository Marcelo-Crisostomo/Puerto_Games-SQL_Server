import pyodbc

def obtener_videojuegos():
    #Conexión a SQL Server
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'#Especificamos el driver
        'SERVER=localhost;'
        'DATABASE=PuertoGames;'
        'Trusted_Connection=yes;'
    )

    # Cursor para ejecutar las consultas
    cursor = conn.cursor()

    #Consulta JOIN
    cursor.execute("""
    SELECT v.Nombre, v.Genero, v.Precio, p.Nombre AS Plataforma
    FROM Videojuego v
    JOIN Plataforma p ON v.IDPlataforma=p.IDPlataforma
    """)
    #Recupera todos los recursos y lo guarda en una lista
    resultados= cursor.fetchall()

    conn.close()#Cerrando la conexión

    return resultados



