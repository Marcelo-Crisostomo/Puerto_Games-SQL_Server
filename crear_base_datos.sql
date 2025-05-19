create database PuertoGames;  
go

use PuertoGames;
go


create table Plataforma ( 
    IDPlataforma INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR (50)
);

create table Videojuego(
    IDVideojuego INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Genero NVARCHAR(100),
    Precio DECIMAL(10,2),---0987654321.12
    IDPlataforma INT,
    FOREIGN KEY (IDPlataforma) REFERENCES Plataforma (IDPlataforma)
);

INSERT INTO Plataforma (Nombre)VALUES
('Pc'),('Xbox'),('PS4'),('Nintendo'),('Atari');

INSERT INTO Videojuego(Nombre,Genero,Precio,IDPlataforma) VALUES
('GTA VI', 'OPEN WORLD',80000,1),
('Balatro','Roguelike',8500,1),
('nfs', 'racing', 45000,1),
('Super Smash Bros','Fighting Game',60000,1),
('Limbo', 'Metroidvania', 49990, 1);