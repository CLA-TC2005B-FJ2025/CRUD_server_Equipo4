CREATE TABLE Usuario (
    email VARCHAR(60) NOT NULL,
    NombreUsuario VARCHAR(60) NOT NULL,
    PRIMARY KEY (email)
);
GO

INSERT INTO Usuario (email, NombreUsuario) VALUES
('admin@game.com', 'AdminPrincipal'),
('jugador1@email.com', 'PixMaster'),
('jugador2@email.com', 'GrixelHunter');
GO

CREATE TABLE Pregunta (
    idPregunta INTEGER IDENTITY(1,1) PRIMARY KEY,
    pregunta VARCHAR(200) NOT NULL
);
GO

INSERT INTO Pregunta (pregunta) VALUES
('¿Qué animal aparece en este píxel?'), 
('¿Cuál es el nombre de esta obra famosa?'), 
('¿Qué color predominante ves?');
GO

CREATE TABLE Imagen (
    ImagenID INTEGER IDENTITY(1,1) PRIMARY KEY,
    Activo BIT NOT NULL,
    Respuesta VARCHAR(50) NOT NULL,
    fechaInicio DATETIME NOT NULL,
    fechaFinalizacion DATETIME NOT NULL,
    ImagenURL VARCHAR(200) NOT NULL,
    email_Usuario VARCHAR(60),
    FOREIGN KEY (email_Usuario) REFERENCES Usuario(email)
);
GO

INSERT INTO Imagen (Activo, Respuesta, fechaInicio, fechaFinalizacion, ImagenURL, email_Usuario) VALUES
(1, 'La Mona Lisa', GETDATE(), DATEADD(day, 7, GETDATE()), 'https://ejemplo.com/mona_lisa_pixelada.jpg', 'admin@game.com');
GO

CREATE TABLE Respuesta (
    RespuestaID INTEGER IDENTITY(1,1) PRIMARY KEY,
    Respuesta VARCHAR(150) NOT NULL,
    Correcta BIT NOT NULL,
    idPregunta INTEGER NOT NULL,
    FOREIGN KEY (idPregunta) REFERENCES Pregunta(idPregunta)
);
GO

INSERT INTO Respuesta (Respuesta, Correcta, idPregunta) VALUES

('León', 1, 1),
('Pájaro', 0, 1), 

('La Mona Lisa', 1, 2),
('El Grito', 0, 2), 

('Azul', 1, 3),
('Rojo', 0, 3); 
GO

CREATE TABLE Grixel (
    IDgrixel INTEGER IDENTITY(1,1),
    ImagenID INTEGER NOT NULL,
    CoorX INTEGER NOT NULL,
    CoorY INTEGER NOT NULL,
    email_Usuario VARCHAR(60),
    idPregunta_Pregunta INTEGER NOT NULL,
    PRIMARY KEY (IDgrixel, ImagenID),
    FOREIGN KEY (ImagenID) REFERENCES Imagen(ImagenID),
    FOREIGN KEY (email_Usuario) REFERENCES Usuario(email),
    FOREIGN KEY (idPregunta_Pregunta) REFERENCES Pregunta(idPregunta)
);
GO

INSERT INTO Grixel (ImagenID, CoorX, CoorY, email_Usuario, idPregunta_Pregunta) VALUES
(1, 10, 10, NULL, 1), 
(1, 10, 11, NULL, 3),
(1, 11, 10, 'jugador1@email.com', 1); 
GO

CREATE TABLE Responde (
    IDregistro INTEGER IDENTITY(1,1) PRIMARY KEY,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    email_Usuario VARCHAR(60) NOT NULL,
    RespuestaID INTEGER NOT NULL,
    FOREIGN KEY (email_Usuario) REFERENCES Usuario(email),
    FOREIGN KEY (RespuestaID) REFERENCES Respuesta(RespuestaID)
);
GO

-- Insertar respuestas de jugadores (registro de intentos)
INSERT INTO Responde (Fecha, Hora, email_Usuario, RespuestaID) VALUES
(GETDATE(), GETDATE(), 'jugador1@email.com', 1), 
(GETDATE(), GETDATE(), 'jugador2@email.com', 4); 
GO
